def prime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
         return False
    return True
number=int(input("enter a number:"))
if prime(number):
   print(f"{number}:is prime")
else:
   print(f"{number}is not prime")       