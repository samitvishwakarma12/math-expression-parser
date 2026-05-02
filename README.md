
# Expression Parser

A simple Python-based expression evaluator supporting:

- +, -, *, /
- // (floor division)
- ** and ^ (exponentiation)

## Features
- Handles operator precedence (PEMDAS)
- Supports multi-digit integers
- Right-associative exponentiation

## Limitations
- No parentheses
- No negative numbers (unary minus)
- Integers only

## How it works
- Tokenizes input string
- Uses two stacks (numbers and operators)
- Applies operations based on precedence

## Example

Input:  2 + 3 * 4
Output: 14
