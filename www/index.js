import * as wasm from "servus";

console.log("sum of 3 and 7 is " + wasm.sum(3, 7));
console.log("the reverse of 'OrangeTux' is '"+ wasm.reverse("OrangeTux") + "'");

let input = "OrangeTux"
let compressed = wasm.compress(input);
let uncompressed = wasm.decompress(compressed);
console.log(uncompressed);

var output = "";

for (var i = 0; i < uncompressed.length; i++) {
	output += String.fromCharCode(uncompressed[i]);
}

console.log(output);
