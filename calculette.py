a = float(input("enter the first number: "))
b = float(input("enter the next number: "))
cal = input("select the type of calculation: addition, subtraction, multiplication, division: ")
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
try:
    if cal == "addition":
        print(f"the result is: ", addition)
    elif cal == "subtraction":
        print(f"the result is: ", subtraction)
    elif cal == "multiplication":
        print(f"the result is: ", multiplication)
    elif cal == "division":
        print(f"the result is: ", division)
    else:
        print("the calculation does not exist")
except ZeroDivisionError:
    print("error: division by zero is not allowed.")
except ValueError:
    print("error: invalid input. please enter a valid number")
except NameError:
    print("error: A variable is not defined. please check your code.")
except Exception as e:
    print(f"an unexpected error occurred: {e}")
               
