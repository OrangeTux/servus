use lz4_compression::prelude::{ decompress, compress };

fn main(){
    let uncompressed_data: &[u8] = b"servus";

    let compressed_data = compress(uncompressed_data);
    println!("{:?}", compressed_data);
    let decompressed_data = decompress(&compressed_data).unwrap();
}
