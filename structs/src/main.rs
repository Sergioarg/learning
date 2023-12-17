struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
// Tuple Struct
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    // Defining struct

    // ? Pregunta: como se alamcenan estos valores en memoria?
    // Create an instance of de struct

    let user1 = User {
        active: true,
        username: String::from("user1"),
        email: String::from("user@some.com"),
        sign_in_count: 1,
    };

    // Accesing to value
    println!("Email: {}", user1.email);

    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
    println!("User 2: {}", user2.username);

    // if the instaces user1 is mutable I can change the values of
    // user1.email = String::from("anotheremail@example.com");

    // Creating Instances from Other Instances with Struct Update Syntax
    // let tup: ();

    // Tuple structs

}
