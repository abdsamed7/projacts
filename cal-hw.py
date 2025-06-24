def power_nbr(a,b):
     s=1
     for i in range(int(b)):
          s=a*s
     return s      
def addition(a,b):
    addition=a+b
    return addition
def subtraction(a,b):
    subtraction= a-b
    return subtraction
def multiplication(a,b):
    multiplication = a * b
    return multiplication
def division(a,b):
    division = a / b
    return division
while True:
 print("\n select the type of calculation:\n")
 print("1.addition")
 print("2.subtraction")  
 print("3.multiplication") 
 print("4.division")
 print("5.power")
 print("6.exit")
 cal=input("choose the operation number :")
 if cal=="6":
  print("finish")
  break
 try:
    a = float(input("enter the first number: "))
    b = float(input("enter the first number: "))
    if cal == "1":
        print(f"the result is: ", addition(a,b))
    elif cal == "2":
        print(f"the result is: ",subtraction(a,b))
    elif cal == "3":
        print(f"the result is: ",multiplication(a,b))
    elif cal == "4":
        print(f"the result is: ",division(a,b))   
    elif cal=="5":
       print(f"the result is:",power_nbr(a,b)) 
 except ZeroDivisionError:
    print("error: division by zero is not allowed.")
 except ValueError:
    print("error: invalid input. please enter a valid number")
 except NameError:
    print("error: A variable is not defined. please check your code.")
 except Exception as e:
    print(f"an unexpected error occurred: {e}")            
 