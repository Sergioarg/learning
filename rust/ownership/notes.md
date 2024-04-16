## Ownership concepts

#### Mutability and Immutability
1. This is a sercure to dondn't change value of the data in case of not be necessary

#### Owner:

> Apply for Structs or mallocs, ej String, Vec, HashMap
>
> Doesn't apply to scalar types because it only makes clones (copies) ej: i32, f64, &str.

### Ways to change owner

**Assign**
```rust
let mut _numbers = Vec::from([1,2,3,5]); // 1. owner: numbers
let mut owner_num = _numbers;
```
**Passing fn Argument**
```rust
fn add_nine1(data: Vec<i32>) { }
```
**Brackets Scope**
```rust
{
    let mut numbers = Vec::from([1,2,3,5]); // 1. owner: numbers
    println!("{}", numbers);
}
```

#### References as Borrowing

---
- There are only three options:
    - Make copies with `clone()`
    - borrowing reference `&`
    - Move "owner"
---

- References - Dangling Pointers
- Borrowing
- `change_with_own` and `change_value_in_ref` depends of the use case of the problem to solve
    - `change_with_own`: apply when is a simple case
    - `change_value_in_ref`: apply when is necesary to process a lot of information

```rust
fn main() {
    let mut s = String::from("Hello");
    // change_with_own(s);
    change_with_own(s.clone()); // O(n)

    for _ in 0..=10_000_000 {
        change_value_in_ref(&mut s); // (O) 1
        // change_with_own(s.clone()); // O(n)
    }
    println!("Final s:\n{}", s);
}

// Change the owner of 'Hello'
fn change_with_own(mut some_string: String) {
    some_string.push_str(", world");

    println!("Data: {}", some_string);
}

// Change the value of the reference of 's' in this example.
fn change_value_in_ref(some_string: &mut String) { // &mut String -> ref de 's'
    some_string.push_str(" Rust"); //
}
```

```rust
// Other option
fn main() {
    let s = String::from("Hello");
    let final_text = format!("{} {} ", s ,"Rust".repeat(10_000_000));
    println!("Final s:\n{}", final_text);
}
```

#### Borrow checker
Rules:
- &mut - &immutable  at same time forbidden
- &mut > 1  forbidden.
- reference valid
