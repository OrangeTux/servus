// The web-sys crate provides access to Web APIs, like Document and console.  We don't have those
// APIs in non-web environments. Importing a WASM file that uses the `web-sys` crate would fail
// with:
//
// Traceback (most recent call last):
// File "python/wasm-with-wasmer.py", line 8, in <module>
//   servus = Instance(wasm_bytes)
// RuntimeError: Failed to instantiate the module:
//   link error: Import not found, namespace: ./servus.js, name: __wbindgen_throw
//
// Therefore theire 2 implemententations of the log! macro: 1 that writes to the browsers console
// and 1 that does nothing.
#[cfg(web)]
use web_sys;

// A macro to provide `println!(..)`-style syntax for `console.log` logging.
#[cfg(web)]
macro_rules! log {
    ( $( $t:tt )* ) => {
        web_sys::console::log_1(&format!( $( $t )* ).into());
    }
}

#[cfg(not(web))]
macro_rules! log {
    ( $( $t:tt )* ) => {}
}
