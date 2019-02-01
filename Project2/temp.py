import random

x=[]
op=["+","-","/","*","^","(",")"]
nums=["1","2","3","4","5","6","7","8","9"]

while len(x)!=100:
    x.append(random.choice(nums))
    x.append(random.choice(op))

print(" ".join(x))

def comp(thing,thi2):
    if thing == thi2:
        return True
    else:
        return False

print(comp("6 6 6 * + 2 + 7 + 5 - 1 8 * 6 * 4 7 2 ^ * 9 1 2 ^ ^ / 3 / + 3 ^ - 4 8 6 ^ 7 * 2 * + 8 8 9 ^ ^ - 7 - 6 + 6 4 6 ^ ^ + 4 3 6 + - 3 5 * 8 / + 2 9 ^ 4 2 ^ / 4 9 * 3 + 3 5 3 ^ / - 1 - * - 2 + 4 9 ^ -","6 6 6 * + 2 + 7 + 5 - 1 8 * 6 * 4 7 2 ^ * 9 1 2 ^ ^ / 3 / + 3 ^ - 4 8 6 ^ 7 * 2 * + 8 8 9 ^ ^ - 7 - 6 + 6 4 6 ^ ^ + 4 3 6 + - 3 5 * 8 / + 2 9 ^ 4 2 ^ / 4 9 * 3 + 3 5 3 ^ / - 1 - * - 2 + 4 9 ^ -"))