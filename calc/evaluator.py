'''
This module evaluates mathematical expressions using the Shunting Yard styled approach.
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
Take two stacks: one for numbers and one for operators
Check the operator types
Pop two numbers and one operator
Apply the operator to the numbers
Append the result back to the numbers stack
End
"""

from .ast_node import NumberNode, BinaryOpNode

def evaluate(node):

    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, BinaryOpNode):

        left = evaluate(node.left)
        right = evaluate(node.right)

        if node.op == '+':
            return left + right

        elif node.op == '-':
            return left - right

        elif node.op == '*':
            return left * right

        elif node.op == '/':
            return left / right

        elif node.op == '//':
            return left // right

        elif node.op == '**':
            return left ** right