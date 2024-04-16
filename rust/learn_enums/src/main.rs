#[derive(Debug)]
enum IncomesCategory {
    Ocio,
    Home,
    Mandatory,
}

struct Ingresos {
    ingreso: u32,
    ingreso_categoria: String
}


fn main() {
    let category = IncomesCategory::Mandatory;

    if let IncomesCategory::Home = category {
        println!("Home!")
    }

    match category {
        IncomesCategory::Home => {
            println!("Home")
        }
        IncomesCategory::Ocio => {
            println!("Ocio")
        }
        IncomesCategory::Mandatory => {
            println!("Mandatory")
        }
    }
}
