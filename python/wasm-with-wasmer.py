import os
from wasmer import Instance

__dir__ = os.path.dirname(os.path.realpath(__file__))
file = "/../pkg/servus_bg.wasm"

wasm_bytes = open(__dir__ + file, 'rb').read()
servus = Instance(wasm_bytes)

sum = servus.exports.sum(3, 7)
print(f'wasmer: sum of 3 and 7 is {sum}')

data = b'OrangeTux'

length = len(data)

# Use the memory allocator from wasm-bindgen to allocate some memory.
offset = servus.exports.__wbindgen_malloc(length)

for i, c in enumerate(data):
    servus.memory.uint8_view()[offset + i] = c

# The second and third argument are respectively the offset in memory where
# data starts and the length of the data
servus.exports.reverse(8, offset, length)

# The call to `reverse()` doesn't return a return value. Instead the offset and
# and size of the data are written to index 2 and 3 of the 32 bit paged memory.
mem = servus.memory.uint32_view()
offset = mem[2]
length = mem[3]

mem = servus.memory.uint8_view()

reverse = ""
for i, c in enumerate(mem[offset:offset+length]):
    reverse += chr(c)

# Free the memory that we've used.
servus.exports.__wbindgen_free(offset, length)

print(f"wasmer: the reverse of '{data}' is '{reverse}'")
