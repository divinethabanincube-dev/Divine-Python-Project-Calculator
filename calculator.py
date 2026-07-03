num1 =float(input("Enter first number:"))
operator = input ("Enter operater(+,-,*,/):")
num2 = float(input("Enter second number"))

if operator =="+":
    print ("Result:",num1 +num2)
elif operator =="-":
    print("Result:",num1 +num2)

elif    operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("result:",num1 / num2)
    else:          
        print("cannot divide by zero")
else: 
    print("invalid operator") 