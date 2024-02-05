
use std::io;
use unicode_segmentation::UnicodeSegmentation;
fn main() {
    println!("Enter a string or char that you want to get the length of: ");
    let mut userinput: String = String::new();
    io::stdin()
        .read_line(&mut userinput)
        .expect("Failed to read input");
    println!("\nThe length of {} is {} (Including whitespaces) ",userinput, length(&userinput));
}
fn length(string:&String) -> usize {
    return string.graphemes(true).count()-1 
}
