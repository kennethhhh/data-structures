from stack_array import Stack
import numbers

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def isNumber(string):
    try:
        float(string)
        return True
    except:
        return False

def postfix_eval(input_str):
    """Evaluates a postfix expression"""
    list=input_str.split()
    s=Stack(30)
    counter=0
    for item in list:
        if isNumber(item):
            s.push(float(item))
            counter+=1
        #elif item == "-" or item == "+" or item == "*" or item == "/" or item == "^":
        elif item in "-+*/^":
            try:
                num1=s.pop()
                num2=s.pop()
            except:
                #not enough numbers in the stack so pop() fails meaning not enough numbers
                raise PostfixFormatException("Insufficient operands")
            counter -= 1
            if item== "-":
                s.push((num2) - (num1))
            if item == "+":
                s.push((num2) + (num1))
            if item == "*":
                s.push((num2) * (num1))
            if item == "/":
                #cant divide by 0
                if (num1)==0:
                    raise ValueError
                else:
                    s.push((num2) / (num1))
            if item == "^":
                s.push((num2) ** (num1))
        else:
            #does not match any of the
            print(item, "is the invalid token")
            raise PostfixFormatException ("Invalid token")
    if counter>1:
        #this means that there are still numbers in the stack
        raise PostfixFormatException("Too many operands")
    return (s.pop())

    #"""Input argument:  a string containing a postfix expression where tokens
    #are space separated.  Tokens are either operators + - * / ^ or numbers
    #Returns the result of the expression evaluation.
    #Raises an PostfixFormatException if the input is not well-formed"""

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""
    RPN_list=[]
    s=Stack(30)
    str_list=input_str.split()
    for thing in str_list:
        if isNumber(thing):
            RPN_list.append(thing)
        elif thing == '(':
            s.push(thing)
        elif thing == ')':
            while s.peek()!= '(' and not s.is_empty():
                RPN_list.append(s.pop())
            s.pop()
        #exponential has highest precedence
        elif thing == '^':
            s.push(thing)
        elif thing == "*" or thing == "/":
            try:
                if s.peek() == "*" or s.peek() == "/" or s.peek() == "^" :
                    while not s.is_empty() and s.peek() == "*" or s.peek() == "/" or s.peek() == "^":
                        RPN_list.append(s.pop())
            except:
                pass
            s.push(thing)
        elif thing == "+" or thing == "-":
            while not s.is_empty() and s.peek() != '(':
                RPN_list.append(s.pop())
            s.push(thing)
    while s.size()!=0:
        RPN_list.append(s.pop())
    return (' '.join(RPN_list))





    # """Input argument:  a string containing an infix expression where tokens are
    # space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    # Returns a String containing a postfix expression """


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    input_list=input_str.split()
    reverse_list=input_list[::-1]
    s=Stack(30)
    for item in reverse_list:
        if isNumber(item):
            s.push(item)
        if item == '+' or item == '-' or item == '*' or item == '/' or item == '^':
            op1=s.pop()
            op2=s.pop()
            s.push(op1 + ' ' + op2 + ' ' + item)
    return(s.pop())

    # """Input argument: a string containing a prefix expression where tokens are
    # space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    # Returns a String containing a postfix expression(tokens are space separated)"""


#print(infix_to_postfix("2 * 3 * ( 4 + 5 )"))
#print(infix_to_postfix("3 + 4 - 2 + ( 7 ^ 2 )"))
#print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
#print(postfix_eval("5 2 4 * + 7 + 2 - 4 6 2 / 2 - * + 4 -"))
#print(postfix_eval("99 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +"))
#print(infix_to_postfix("6 + 6 * 6 + 2 + 7 - 5 - ( 1 * 8 * 6 + 4 * 7 ^ 2 / 9 ^ 1 ^ 2 / 3 ) ^ 3 + 4 ( 8 ^ 6 ) * 7 * 2 - 8 ^ 8 ^ 9 - 7 + 6 + 6 ^ 4 ^ 6 - 4 ( 3 + 6 ) + 3 * 5 / 8 - 2 ^ 9 / 4 ^ 2 * ( 4 * 9 + 3 - 3 / 5 ^ 3 - 1 ) + 2 - 4 ^ 9" ))