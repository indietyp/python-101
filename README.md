# Git 102 - Advanced Git

This is the repository for the Python 101 introduction course, which is offered as part of the course offering of the
IMPRS for Cell, Developmental and Systems Biology at the MPI-CBG.

To access the exercise portion of the course, please visit one of the following links:
* [GitHub](https://github.com/indietyp/python-101/tree/main/tasks)
* [MPI-CBG OwnCloud]
* [TU-Dresden OwnCloud]

You can do with this book whatever you want. If you find any errors or have suggestions for improvements, please open an
issue or a merge request. Thank you! :)

## Creating the book

This book uses [mdBook](https://github.com/rust-lang/mdBook) to generate a static website from markdown files. To run
any of these commands you need to have [Rust](https://www.rust-lang.org/) installed.

You can install all required dependencies with the following command:

```bash
cargo install mdbook mdbook-linkcheck mdbook-mermaid mdbook-emojicodes mdbook-admonish
```

You can then build the book with the following command:

```bash
mdbook build
```

You can also serve the book locally with the following command:

```bash
mdbook serve
```

## License

This book is licensed under the [CC0 1.0 Universal](LICENSE-CC0.md) license.

> This means you can do with it whatever you want. You don't even have to give attribution. Although, I would appreciate
> it if you did. :)
>
> This does not mean this work is given into the public domain. (Although, I would like that.) This is because it isn't
> possible to attribute something to the public domain in some jurisdictions. (e.g. Germany)

All software in this repository is dual-licensed under the [MIT](LICENSE-MIT.md) and [Apache 2.0](LICENSE-APACHE.md)
licenses.
