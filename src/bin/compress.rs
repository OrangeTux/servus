use zip;
use std::io::Write;
use std::fs::File;

fn main() -> zip::result::ZipResult<()> {
    let mut w = File::create("hello_word.zip")?;
    let mut zip = zip::ZipWriter::new(w);

    let options = zip::write::FileOptions::default();

    zip.start_file("hello_world.txt", options)?;
    zip.write(b"Hello, World!")?;

    zip.finish()?;

    Ok(())
}
