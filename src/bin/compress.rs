use lz4_compression::prelude::{ decompress, compress };

fn main(){
    let uncompressed_data: &[u8] = b"Hello world, what's up?";

    let compressed_data = compress(uncompressed_data);
    let decompressed_data = decompress(&compressed_data).unwrap();
}
