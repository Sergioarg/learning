fn main() {
    let mut s = String::from("Hello");

    let r1 = &s; // borrow // inmutable
    let r2 = &s; // borrow // inmutable
    println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point

    let r3 = &mut s; // borrow // mutable
    println!("{}", r3);
}
