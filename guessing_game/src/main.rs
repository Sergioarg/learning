use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the numeber");
    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");
        let mut guess = String::new(); // mutable

        io::stdin()
            .read_line(&mut guess) // al hacer &mut estoy prestando guess a la funcion
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        println!("The secret number is: {secret_number}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
