import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

to_continue = True
first_num = int(input("What's the first number?: "))
while to_continue:
    for key in operations:
        print(key)
    op = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    ans = float(operations[op](first_num,next_num))
    print(f"{first_num} {op} {next_num} = {ans}")
    y_n = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation:").lower()
    if y_n == "n":
        to_continue = False
    elif y_n == "y":
        to_continue = True
        first_num = ans
    else:
        to_continue = False
        print("Invalid input!!")









