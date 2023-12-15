1. Clone y copy son lo mismo?
2. Cuando debo utilizar clone
3. No entiendo esto

```rust
let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point

    let r3 = &mut s; // no problem
    println!("{}", r3);
```

4. Alcance de los valores mutables e inmutables con las referencias


5. Que hace este codigo?
```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> String {
    s.replace("h", "f")
}
```
