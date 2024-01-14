use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() 
{ 
    println!("Guess a number between one and ten\nPlease input your guess");
    let rand_num = rand::thread_rng().gen_range(1..=100);
    let mut guesses:i32 = 0;
    loop
    {
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");
        let guess: u32 = guess.trim().parse()
            .expect("Please type a number!");
        match guess.cmp(&rand_num)
        {
            Ordering::Less => 
            {
                println!("Too small!");
            }

            Ordering::Greater => 
            {
                println!("Too big!");
            }

            Ordering::Equal =>
            {
                println!("You win!, you got in {guesses} guesses");
                break;
            }
        }
        guesses = guesses+1
    }
}
