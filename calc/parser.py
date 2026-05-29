'''
Module for parsing tokens into a result for further evaluation.
Supported operations:
- Addition            : +
- Subtraction         : -
- Multiplication      : *
- Division            : /
- Floor Division      : //
- Exponentiation      : **
Rules:
- Use only numbers and the operators above
- Do NOT use parentheses
- Example inputs:
    2 + 3 * 4
    10 // 3 + 2
    2 ** 3 * 5
'''

"""
Algorithm:

Start
Initialize two stacks: one for numbers and one for operators
For each token in the input:
    If the token is a number, push it onto the numbers stack
    If the token is an operator:
        While there is an operator at the top of the operators stack with greater precedence:
            
        
After processing all tokens, while there are still operators on the stack:


End
"""



from calc.ast_node import BinaryOpNode, NumberNode


def parser(tokens: list[str]) -> BinaryOpNode | NumberNode:

    precedence = {'+':1, '-':1, '*':2, '/':2, '//':2, '**':3, '^': 3}
    numbers = []
    ops = []

    for token in tokens:
      
        if token.isdigit():
            numbers.append(NumberNode(float(token)))

        else:
            while ops and (precedence[ops[-1]] > precedence[token] or (precedence[ops[-1]] == precedence[token] and token not in ('**', '^'))):
                build_node(numbers, ops)
            ops.append(token)
            
    while ops:
        build_node(numbers, ops)
    
    return numbers[0]
    


def build_node(numbers: list, ops: list) -> None:

    right = numbers.pop()
    left = numbers.pop()
    op = ops.pop()

    numbers.append(BinaryOpNode(left, op, right))    