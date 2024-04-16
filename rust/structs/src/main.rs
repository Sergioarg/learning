

// fn is_palindrome(s: String) -> bool {

//     for c in s.char() {
//         println!("{}", c);
//     }
// }

fn main() {

    let str = String::from("A man, a plan, a canal: Panama");

    for c in str.chars() {
        println!("{}", c);
    }
}
