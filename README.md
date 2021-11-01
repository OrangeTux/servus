# Servus

Using this project I'm exploring WebAssembly and it's ecosystem. This projects
make a Rust implementation of the lz4 compression algorithm available in
WebAssembly. A Python and Javascript implementation are provided that allow
users to (de)compress files. Both implementation use `Wasm`.

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

The `python/` folder contains 2 scripts which that uses a Wasm file to
(de)compress files using lz4.

``` bash
$ cd python
$ poetry install 
$ poetry shell
$ ./lz4.py --help
lz4 archive utility using Wasm.

USAGE:
    lz4 compress <file>
    lz4 decompress <file>

FLAGS:
        --help  Prints help information

ARGS:
    <file> Path to file that needs to be (de)compressed.
```

To decompress a file:

``` bash
venv> ./lz4.py compress pyproject.toml
Compressed pyproject.toml (436 bytes) to pyproject.toml.lz4 (333 bytes), reduction of 24%.
```

To decompress a file:

```
venv> ./lz4.py decompress pyproject.toml.lz4
Decompressed pyproject.toml.lz4 to pyproject.toml.
```

## JavaScript

The `www/` directory contains a file `index.js` which calls into the WASM
files. The result of those calls is written the the browser's console.

Build the WASM file for the browser environment:

Start the webserver:

``` bash
$ cd wwww/
$ npm install
$ npm start
```

Open http://localhost:8080 in your browser. The page shows two form fields to
upload files. One to compress files, another to decompress files. 

[poetry]: https://python-poetry.org/docs/#installation
