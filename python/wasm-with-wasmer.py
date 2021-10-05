import os
from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler

__dir__ = os.path.dirname(os.path.realpath(__file__))
file = "/pkg/servus_bg.wasm"

store = Store(engine.JIT(Compiler))
wasm_bytes = open(__dir__ + file, "rb").read()
module = Module(store, wasm_bytes)
servus = Instance(module)

sum = servus.exports.sum(3, 7)
print(f"wasmer: sum of 3 and 7 is {sum}")


def allocate(data: bytes) -> int:
    """Allocate the given bytes in WASM memory. Pointer to start of the
    allocated data is returned.
    """
    length = len(data)

    # Use the memory allocator from wasm-bindgen to allocate some memory.
    offset = servus.exports.__wbindgen_malloc(length)

    for i, c in enumerate(data):
        servus.exports.memory.uint8_view()[offset + i] = c

    return offset


def free(offset: int, length: int):
    """Free WASM memory."""
    servus.exports.__wbindgen_free(offset, length)


def reverse(data: bytes) -> bytes:
    """Reverse the given bytes."""
    offset = allocate(data)
    length = len(data)

    # The second and third argument are respectively the offset in memory where
    # data starts and the length of the data
    servus.exports.reverse(8, offset, length)

    # The call to `reverse()` doesn't return a return value. Instead the offset
    # and and size of the data are written to index 2 and 3 of the 32 bit paged
    # memory.
    mem = servus.exports.memory.uint32_view()
    offset = mem[2]
    length = mem[3]

    mem = servus.exports.memory.uint8_view()
    output = mem[offset : offset + length]

    free(offset, length)

    return bytes(output)


def compress(data: bytes) -> bytes:
    """Compress the given bytes using L4Z."""
    offset = allocate(data)
    length = len(data)

    servus.exports.compress(8, offset, length)

    mem = servus.exports.memory.uint32_view()
    offset = mem[2]
    length = mem[3]

    mem = servus.exports.memory.uint8_view()

    data = mem[offset : offset + length]
    free(offset, length)

    return bytes(data)


def decompress(data: bytes) -> bytes:
    """Decompress the given bytes using L4Z."""
    offset = allocate(data)
    length = len(data)

    servus.exports.decompress(8, offset, length)

    mem = servus.exports.memory.uint32_view()
    offset = mem[2]
    length = mem[3]

    mem = servus.exports.memory.uint8_view()

    data = mem[offset : offset + length]
    free(offset, length)

    return bytes(data)


reversed = reverse(b"OrangeTux")
print(f"wasmer: the reverse of 'OrangeTux' is '{reversed}'")
compressed = compress(b"OrangeTux")
print(f"wasmer: 'OrangeTux' compresses to {compressed}")
decompressed = decompress(compressed)
print(f"wasmer: {compressed} decompresses to {decompressed}")
