from art import logo
import sys

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

print(logo)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number? "))
    for k in operations:
        print(k)

    while True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop.: ").casefold()
        if again == 'n' or again == 'no':
            again2 = input("Start a fresh calculation? type 'y' or 'n' ").casefold()
            if again2 == 'y' or again2 == 'yes':
                calculator()
            else:
                print("BYE BYE!")
                sys.exit()


calculator()
