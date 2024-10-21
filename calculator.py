# Function for Addition
def add(x, y):
    return x + y

#Substarction
def substract(x,y):
    return x - y

# Multiplication
def multiply(x,y):
    return x * y

# Division
def divide(x ,y):
    # To divide by zero
    if y == 0:
        return "Error! Division by Zero."
    else: 
        return x/y
    
    #Main Program
while True:
    # User Input
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
        
    #Display operations
    print("Select operation: ")
    print("1. Add")
    print("2. Substract")
    print("3. Multipy")
    print("4. Divide")

    #Collecting user input for operation
    operation = input("Enter your choice (1/2/3/4): ")

    #Dealing with conditionals
    if operation == "1":
        print(f"The result of {x} + {y} is : {add(x,y)}")
    elif operation == "2":
        print(f"The result of {x} - {y} is: {substract(x,y)}")
    elif operation == "3":
        print(f"The result of {x} * {y} is: {multiply(x,y)}")
    elif operation =="4":
        print(f"The result of {x} / {y} is: {divide(x,y)}")
    else:
        print("Invalid input! Please choose a valid operation")

# Ask user if they want to perfom another calculation
    continue_calculation = input("Do you want to perform another calculation? yes/no: ")
    if continue_calculation.lower() != 'yes':
        break #Exit the loop
