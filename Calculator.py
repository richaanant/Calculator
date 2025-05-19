num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))
operator= input("Select the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("The result is ", result)
elif operator == "-":
    result = num1 - num2
    print("The result is ", result)
elif operator == "*":
    result = num1 * num2
    print("The result is ", result)
elif operator == "/":
    if num2 == 0:
        print("you can't divide by zero")
    else: 
          result = num1 / num2
          print("The result is ", result)
    

else: print("Invalid operator")
