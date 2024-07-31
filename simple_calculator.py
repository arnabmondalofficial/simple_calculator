#simple calculator
num1 = int(input("First number: "))
operators = input("Operators: ")
num2 = int(input("Second number: "))
if operators == "+":
    print("result: ", num1 + num2)
elif operators == "-":
    print("result: ", num1 - num2)
elif operators == "*":
    print("result: ", num1 * num2)
elif operators == "/":
    if num2!=0:
        print("result: ", num1 / num2)
    else:
        print("Indefinite")
else:
    print("Invalid operators. Please enter operators between +, -, *, /.")