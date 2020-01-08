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
$ wasm-pack build
```

This command produces several files. Among them:

* `pkg/servus.wasm` - the Rust library compiled to WebAssembly
* `pkg/servus.js` - glue code between Javascript and WebAssembly.

Now it's time to install web app which source is located in `www/`.

```bash
$ cd www
$ npm install
```

Start serving the web app. It will be server at http://localhost:8080.

```bash
$ npm start
```
