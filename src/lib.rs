#[macro_use]
mod utils;

use wasm_bindgen::prelude::*;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[wasm_bindgen]
pub fn compress(input: &str) -> Vec<u8> {
    use lz4_compression::prelude::compress;
    log!("{:?}", input);
    let compressed_data = compress(input.as_bytes());
    log!("{:?}", compressed_data);
    compressed_data
}
