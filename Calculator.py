import os
import art
clear = lambda: os.system('cls')


def calc():
    print(art.logo)
    n1 = int(input("What is the first number?: "))
    n2 = int(input("What is the second Number?: "))
    def addition(n1, n2):
        return n1 + n2
    def substraction(n1, n2):
        return n1 - n2
    def multyply(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2
    operations = {"+": addition, "-": substraction, "/": divide, "*": multyply}
    for x in operations:
        print(x)
    operator = input("Choose an operator: ")
    
    calculationFunction = operations[operator]
    answer = calculationFunction(n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")
    shouldCont = input(f"Type 'y' to continue calculating with {answer}, or type 'no' to start new calculation: ")
    while shouldCont == "y":
        n1 = answer
        n2 = int(input("What is the second Number?: "))
        for x in operations:
            print(x)
        operator = input("Choose an operator: ")
        calculationFunction = operations[operator]
        answer = calculationFunction(n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")
        shouldCont = input(f"Type 'y' to continue calculating with {answer}, or type 'no' to start new calculation: ")
    else:
        clear()
        calc()
calc()
