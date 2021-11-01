#!/usr/bin/env python
""" lz4 archive utility using Wasm.

USAGE:
    lz4 compress <file>
    lz4 decompress <file>

FLAGS:
        --help  Prints help information

ARGS:
    <file> Path to file that needs to be (de)compressed.
"""
import os
import sys
from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler

__dir__ = os.path.dirname(os.path.realpath(__file__))
file = "/pkg/servus_bg.wasm"

store = Store(engine.JIT(Compiler))
wasm_bytes = open(__dir__ + file, "rb").read()
module = Module(store, wasm_bytes)
servus = Instance(module)


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

def compress_file(path: str):
    with open(input, 'rb') as f:
        data = f.read()
        compressed_data = compress(data)

    output = f'{path}.lz4'
    with open(output, 'wb+') as f:
        f.write(compressed_data)

    print(f'Compressed {path} ({len(data)} bytes) to {output} ({len(compressed_data)} bytes), reduction of {100 - int((len(compressed_data) / len(data)) * 100)}%.')

def decompress_file(path: str):
    with open(input, 'rb') as f:
        data = f.read()
        uncompressed_data = decompress(data)
    output = path
    if path.endswith('.lz4'):
        output = path.rsplit('.', 1)[0]

    with open(output, 'wb+') as f:
        f.write(uncompressed_data)

    print(f'Decompressed {path} to {output}.')

if __name__ == '__main__':
    try:
        if sys.argv[1] == '--help':
            print(__doc__)
            sys.exit(0)
    except IndexError:
        pass

    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    input = sys.argv[2]

    if command == 'compress':
        compress_file(input)

    elif command == 'decompress':
        decompress_file(input)
    else:
        print("Invalid command.")
        print(__doc__)
        sys.exit(1)


