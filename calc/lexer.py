'''
Module for tokenizing mathematical equations.
'''

"""
Algorithm:

Start
Take the equation as input
Initialize an empty list to hold tokens
Iterate through each character in the equation:
    If the character is a digit:
        Start building a number token until a non-digit is encountered
        Append the complete number token to the list
    If the character is an operator:
        Check if the next character is the same operator (for '**' or '//')
            If so, append the double operator token and skip the next character
            Otherwise, append the single operator token
    If the character is a space, ignore it
    If the character is invalid, raise an error
Return the list of tokens
End
"""



def tokenizer(equation: str) -> list:
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

lexer = tokenizer # alt name for tokenizer

