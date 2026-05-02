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

    equation = input("Enter the equation to solve here: ")
    tokens = tokenizer(equation)
    result = parser(tokens)
    print("Result:", result)



def tokenizer(equation):

  
    tokens = []
    symbols = ['+','-','/','*','^']
    i = 0
    
    while i < len(equation):
      
        char = equation[i]
        
        if char.isdigit():
            stacker = char
            i += 1
          
            while i < len(equation) and equation[i].isdigit():
              
                stacker += equation[i]
                i += 1
              
            tokens.append(stacker)
          
        
        elif char in symbols:
          
            if i + 1 < len(equation) and equation[i+1] == char:
              
                if char in '/*':
                    tokens.append(char + char)  # '**' or '//'
                    i += 2

              
                else:
                    raise ValueError(f"The char {char + char} is invalid!")

          
            else:
                tokens.append(char)         # SINGLE operator
                i += 1

      
        elif char.isspace():
            i += 1
          
        
        else:
            raise ValueError(f"The char {char} is invalid!")
    
    return tokens



def parser(tokens):

  
    precedence = {'+':1, '-':1, '*':2, '/':2, '//':2, '**':3, '^': 3}
    numbers = []
    ops = []


  
    def apply_op():

      
        if len(numbers) < 2:
            raise ValueError("Invalid expression")
            
        right = int(numbers.pop())
        left = int(numbers.pop())
        op = ops.pop()
        
        
        if op == '+':
            numbers.append(left + right)
        elif op == '-':
            numbers.append(left - right)
        elif op == '*':
            numbers.append(left * right)
        elif op == '/':
            numbers.append(left / right)
        elif op == '//':
            numbers.append(left // right)
        elif op == '**' or op == '^':
            numbers.append(left ** right)

  
    for token in tokens:
      
        if token.isdigit():
            numbers.append(token)

      
        else:
          
            while ops and (precedence[ops[-1]] > precedence[token] or (precedence[ops[-1]] == precedence[token] and token not in ('**', '^'))):
                apply_op()
            ops.append(token)
    
    while ops:
        apply_op()
    
    result = numbers[0]
    return result
        
main()
