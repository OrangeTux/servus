python: export SERVUS_WEB=0
javascript: export SERVUS_WEB=1

build:
	@wasm-pack build

python: build
	@wasm-pack build --out-dir python/pkg

	@echo 'Using wasmer'
	@cd python; poetry run python wasm-with-wasmer.py
	@echo
	@echo 'Using wasmtime'
	@cd python; poetry run python wasm-with-wasmtime.py

javascript: build
