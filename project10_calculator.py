import os
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2  

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def power(n1,n2):
    return round(pow(n1,n2),2)

def root(n1,n2):
    return round(pow(n1,1/n2),2)

operation_continue = True
print("Welcome to the calculator app!!")

def Calculator():
    num1 = float(input("Enter the first number: "))

    sign = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division,
    "^" : power,
    "%" : root
    }

    for i in sign:
        print(i)

    while operation_continue:
        operation = input("Enter the operation: ")
        num2 = float(input("Enter another number: "))
        answer = round(sign[operation](num1,num2),2)
        print(f"{num1} {operation} {num2} = {answer}")
        conti = input(f"Type 'Y' if Want to continue with {answer} else Type 'N' for new calculation: ").lower()
        if conti =="y":
            num1 = answer
        else:
            os.system('cls')
            Calculator()
Calculator()

