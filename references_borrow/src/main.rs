fn main() {
    let mut s = String::from("Hello");

    let r1 = &s; // no problem // inmutable
    let r2 = &s; // no problem // inmutable
    println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point

    let r3 = &mut s; // no problem // mutable
    println!("{}", r3);
}
