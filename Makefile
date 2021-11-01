build:
	@SERVUS_WEB=0 wasm-pack build --out-dir python/pkg
	@SERVUS_WEB=1 wasm-pack build
