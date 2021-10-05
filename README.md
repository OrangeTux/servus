# Servus

Using this project I'm exploring WebAssembly and it's ecosystem. I'm trying to
build a simple file sharing web application using Python, Rust, WebAssmebly
and Javascript.


## Quickstart

First you need compile the Rust code in `src/` to WebAssembly. `wasm-pack` is
needed for that.

``` bash
$ cargo install wasm-pack
```

``` bash
$ make build
```

This command produces several files. Among them:

* `pkg/servus_bg.wasm` - the Rust library compiled to WebAssembly
* `pkg/servus.js` - glue code between Javascript and WebAssembly

## Python

The `python/` folder contains 2 scripts which call into the WASM files. One
script is using `wasmer`, the other `wasmtime`.

``` bash
$ python3.7 -m venv .env
$ source .env/bin/activate
$ pip install -r python/requirements.txt
```

Now you can run the scripts:

``` bash
$ make python
[INFO]: Checking for the Wasm target...
[INFO]: Compiling to Wasm...
    Finished release [optimized] target(s) in 0.02s
[INFO]: Installing wasm-bindgen...
[INFO]: Optional fields missing from Cargo.toml: 'description', 'repository', and 'license'. These are not necessary, but recommended
[INFO]: :-) Done in 0.10s
[INFO]: :-) Your wasm pkg is ready to publish at ./pkg.
Using wasmer
wasmer: sum of 3 and 7 is 10
wasmer: the reverse of 'OrangeTux' is 'xuTegnarO'

Using wasmtime
wasmtime: sum of 3 and 7 is 10
```

## JavaScript

The `www/` directory contains a file `index.js` which calls into the WASM
files. The result of those calls is written the the browser's console.

Build the WASM file for the browser environment:

``` bash
$ make javascript
```

Now start the webserver:

``` bash
$ cd wwww/
$ npm install
$ npm start
```

If you now open the Developer Console of your browser and visit
http://localhost:8080 you should see this:

```
sum of 3 and 7 is 10
This log comes from WASM.
the reverse of 'OrangeTux' is 'xuTegnarO'
```
