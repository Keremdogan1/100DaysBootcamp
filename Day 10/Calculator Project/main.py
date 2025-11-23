from art import logo

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mltpy(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    return "Can't divide by 0!"

operators = {
    "+": add,
    "-": sub,
    "*": mltpy,
    "/": div
}

will_num1 = False

while True:
    print(logo)
    if not will_num1:
        num1 = float(input("What's the first number? :"))

    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What's the second number? :"))

    if(operation == "+" or operation == "-" or operation == "*" or operation == "/"):
        print(f"{num1} {operation} {num2} = {operators[operation](num1, num2)}")
    else:
        print("Invalid operation!")

    check = input(f"Type 'y' to continue calculating with {operators[operation](num1, num2)} or type 'n' to start a new calculation: ").lower()
    if(check == "y"):
        will_num1 = True
        num1 = operators[operation](num1, num2)
    else:
        will_num2 = False
        print("\n" * 100)
