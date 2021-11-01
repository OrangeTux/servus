import * as wasm from 'servus'

document.getElementById('compress').addEventListener('change', compressFile, false)
document.getElementById('decompress').addEventListener('change', decompressFile, false)

// Compress selected file using LZ4.
async function compressFile () {
  const file = this.files[0]

  // Read content of a file...
  let uncompressed = await file.text()

  // ... and turn it into a Uint8Array.
  uncompressed = new TextEncoder().encode(uncompressed)

  // Compress the file...
  const compressed = wasm.compress(uncompressed)
  download(compressed, `${file.name}.lz4`, 'application/octect-stream')
}

// Decompress file using LZ4.
async function decompressFile () {
  const file = this.files[0]
  // Read content of binary file...
  let compressed = await file.arrayBuffer()

  // ... and turn it unto a Uint8Array.
  compressed = new Uint8Array(compressed)

  // Decompress it...
  let uncompressedContent = wasm.decompress(compressed)

  /// ... And turn it into readable text.
  uncompressedContent = new TextDecoder('utf-8').decode(uncompressedContent)
  download(uncompressedContent, file.name, 'text/plain')
}

// Allow user to download given data as a file.
function download (data, fileName, mimeType) {
  const blob = new Blob([data], { type: mimeType })

  const url = URL.createObjectURL(blob)
  const a = document.getElementById('download')
  a.href = url
  a.download = fileName
  a.click()
}
