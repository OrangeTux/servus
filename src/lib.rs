#[macro_use]
mod utils;

extern crate wasm_bindgen;
use wasm_bindgen::prelude::*;

#[no_mangle]
#[wasm_bindgen]
pub extern fn sum(x: i32, y: i32) -> i32 {
    x + y
}

#[no_mangle]
#[wasm_bindgen]
pub extern fn reverse(input: String) -> String {
    log!("This log comes from WASM.");

    input.chars().rev().collect::<String>()
}

#[no_mangle]
#[wasm_bindgen]
pub extern fn compress(input: Vec<u8>) -> Vec<u8> {
    use lz4_compression::compress::compress as _compress;
    log!("{:?}", input);
    let output = _compress(&input);
    log!("{:?}", output);

    output
}

#[no_mangle]
#[wasm_bindgen]
pub extern fn decompress(input: Vec<u8>) -> Vec<u8> {
    use lz4_compression::decompress::decompress as _decompress;
    log!("WASM: {:?}", input);
    let output = _decompress(&input).unwrap();
    log!("WASM: {:?}", output);

    output
}
