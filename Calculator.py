def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Error! Division by zero."
def calculator():
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
        
        try:
            choice=int(input("Enter choice (1/2/3/4/5): "))
            if choice==5:
                print("Thank you for using the calculator.")
                break
            if choice in [1, 2, 3, 4]:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                if choice==1:
                    print(f"The result is: {add(num1,num2)}")
                elif choice==2:
                    print(f"The result is: {subtract(num1,num2)}")
                elif choice==3:
                    print(f"The result is: {multiply(num1,num2)}")
                elif choice==4:
                    print(f"The result is: {divide(num1,num2)}")
            else:
                print("Invalid input! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
calculator()