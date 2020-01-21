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
    log!("{:?}", input);

    input.chars().rev().collect::<String>()
}
