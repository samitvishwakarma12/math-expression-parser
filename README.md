# Expression Parser

A Python-based mathematical expression parser and evaluator built for learning and portfolio purposes.

This project tokenizes mathematical expressions, parses them into an Abstract Syntax Tree (AST), and recursively evaluates expressions using standard operator precedence rules.

## Features

Supports the following operators:

```text id="4zwyx9"
+   -   *   /   //   **   ^
```

Additional features:

* Operator precedence handling (PEMDAS)
* Right-associative exponentiation
* Multi-digit integer support
* AST (Abstract Syntax Tree) generation
* Recursive AST evaluation
* Modular project structure
* Supporting modules can run independently
* Includes algorithm explanations and documentation

## Project Structure

```text id="4ksm1l"
expression-parser/
│
├── main.py
│
└── math/
    ├── lexer.py
    ├── parser.py
    ├── evaluator.py
    └── ast_node.py
```

## Modules

### lexer.py

Tokenizes mathematical expressions into operators and numbers.

### parser.py

Parses tokens into an Abstract Syntax Tree using operator precedence rules.

### evaluator.py

Recursively evaluates AST nodes into final numerical results.

### ast_node.py

Defines AST node structures including:

* `NumberNode`
* `BinaryOpNode`

### main.py

Handles user input, expression execution, and runtime flow.

---

# Example

## Input

```text id="32m7ga"
2 + 3 * 4
```

## Generated AST

```text id="g29v1z"
(+)
├── 2
└── (*)
    ├── 3
    └── 4
```

## Output

```text id="kzmbi2"
14
```

---

# Running the Project

From the project root directory:

```bash
python -m main
```

---

# Running Supporting Modules Individually

Example:

```bash
python -m math.lexer
```

You may similarly run:

```bash
python -m math.parser
python -m math.evaluator
```

---

# Current Limitations

* No parentheses support
* No unary minus / negative numbers
* Integers only
* No variables or functions

---

# Purpose of the Project

This project was created for:

* Learning parsing techniques
* Understanding AST construction
* Practicing recursive evaluation
* Exploring interpreter architecture
* Building portfolio projects
* Understanding compiler and language design concepts

---

# Documentation

Each file contains:

* Algorithm explanations
* Inline documentation
* Modular function design

Additional docstrings and documentation improvements are planned.

---

# Planned Improvements

* Parentheses support
* Unary operators
* Variable support
* Function calls
* Better parser architecture
* Improved error handling
* More AST node types
* Better error messages
* More comprehensive docstrings
* Bug fixes and optimizations

---

# Notes

This project is actively being improved and expanded as part of the learning process.
