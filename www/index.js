import * as wasm from "servus";

var compressFile = function() {
	var fileInput = document.getElementById("file-upload");

	if (fileInput.length === 0) {
		console.log(fileInput.length);
		return;
	}

	var file = fileInput.files.item(0);
	file.arrayBuffer().then(function(buffer) {
		var view = new Int8Array(buffer);
		console.log(view);
		var compressed = wasm.compress(view);

		var decompressed = wasm.decompress(compressed);
		let utf8decoder = new TextDecoder();
		console.log(utf8decoder.decode(decompressed));
	});

}

document.getElementById("file-upload").onchange = compressFile;
