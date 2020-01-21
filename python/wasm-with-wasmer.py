import os
from wasmer import Instance

__dir__ = os.path.dirname(os.path.realpath(__file__))
file = "/../pkg/servus_bg.wasm"

wasm_bytes = open(__dir__ + file, 'rb').read()
servus = Instance(wasm_bytes)

sum = servus.exports.sum(3, 7)
print(f'wasmer: sum of 3 and 7 is {sum}')

# Offset in WASM memory where we start writing bytes.
# If it is 0, 1, 2 or 3 it fails with:
#
#    RuntimeError: Call error: WebAssembly trap occured during runtime: memory out-of-bounds access
# I've no clue yet why 4 is the magic number.
OFFSET = 4

for i, c in enumerate(b'OrangeTux'):
    servus.memory.uint8_view()[OFFSET + i] = c

length = i + 1

# The second and third argument are respectively the offset in memory where
# data starts and the length of the data
servus.exports.reverse(8, OFFSET, length)

# The call to `reverse()` doesn't return a return value. Instead the offset and
# and size of the data are written to index 2 and 3 of the 32 bit paged memory.
mem = servus.memory.uint32_view()
offset = mem[2]
length = mem[3]

mem = servus.memory.uint8_view()

reverse = ""
for i, c in enumerate(mem[offset:offset+length]):
    reverse += chr(c)

    # WASM doesn't have a garbage collector, so we do that manually by erasing the memory.
    mem[i] = 0


print(f"wasmer: the reverse of 'OrangeTux' is '{reverse}'")
