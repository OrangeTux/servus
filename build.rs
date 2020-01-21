use std::env;

fn main() {
    match env::var("SERVUS_WEB") {
        Ok(value) => if (value == "1") {
            println!("cargo:rustc-cfg=web")
        },
        Err(_) => {},
    }
}
