
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    quotient=num//b
    remainder=num%b
    #base case
    if quotient==0:
        #if last remainder is between 10 to 16, convert to hexadecimal
        if remainder >= 10 and remainder < 16:
            remainder = chr(remainder + 55)
        return(str(remainder))
    #converts to hexadecimal
    if remainder>=10 and remainder<16:
        remainder=chr(remainder+55)
    #recursion
    return (str(convert(quotient,b))+str(remainder))

print(convert(11259375,16))
