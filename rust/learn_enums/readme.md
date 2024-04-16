Tipos de datos algebraicos:
- Son tipos de datos que tienen variantes: tipos de datos que va a tener un enum

Enums: Tipos de datos algebraicos
- Conjunto delimitado de valores posibles
- Manejan los casos (o variantes) y no los valores
- El tipo de dato verifica los datos no los valores

```rust
    enum IncomesCategory {
        Ocio,
        Home,
        Mandatory,
    }
```

- Rust trata de ser deterministica: es poder tener la idea de saber que es lo que va a pasar
- Si sé que tipo de camino va a tomar mi programa por eso uso un tipo de dato algebarico
- el `match` da la opcion de hacer un codigo deterministico
