#[macro_use]
mod utils;

use std::str;
use wasm_bindgen::prelude::*;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[wasm_bindgen]
/// Compress input using LZ4 compression.
pub fn compress(input: &[u8]) -> Vec<u8> {
    use lz4_compression::prelude::compress;
    compress(input)
}

#[wasm_bindgen]
// Decompress given input using LZ4 decompression.
pub fn decompress(input: &[u8]) -> Vec<u8> {
    use lz4_compression::prelude::decompress;
    decompress(input).unwrap()
}
