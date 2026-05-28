'''
A simple calculator that supports basic arithmetic operations: addition, subtraction, multiplication, division, floor division, and exponentiation. The calculator uses a lexer to tokenize the input, a parser to build an abstract syntax tree (AST), and an evaluator to compute the result based on the AST.
The calculator follows the PEMDAS order of operations and does not support parentheses. Users can input mathematical expressions, and the calculator will return the computed result. The program also includes error handling to manage invalid inputs gracefully.
'''

"""
Algorithm:

Start
Display welcome message and supported operations
While True:
    Prompt user for input
    Try:
        Tokenize the input using the lexer
        Parse the tokens into an AST using the parser
        Evaluate the AST to get the result
        Print the result
    Except any exceptions:
        Print the error message
End
"""



from calc.lexer import tokenizer
from calc.parser import parser
from calc.evaluator import evaluate



def main():

    print("""
        Version 1.0
        
        Supported operations:
        
        Addition            : +
        Subtraction         : -
        Multiplication      : *
        Division            : /
        Floor Division      : //
        Exponentiation      : **
        
        Rules:
        - Parser uses PEMDAS order of operations.
        - Use only numbers and the operators above
        - Do NOT use parentheses
        - Example inputs:
            2 + 3 * 4
            10 // 3 + 2
            2 ** 3 * 5
        """)
    
    while True:
        try:
            equation = input("Enter a mathematical expression: ")
            tokens = tokenizer(equation)
            ast = parser(tokens)
            result = evaluate(ast)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")

   
    
if __name__ == "__main__":
    main()
