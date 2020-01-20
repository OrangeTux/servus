build:
	@wasm-pack build

python: build
	@echo 'Using wasmer'
	@python python/wasm-with-wasmer.py
	@echo
	@echo 'Using wasmtime'
	@python python/wasm-with-wasmtime.py
