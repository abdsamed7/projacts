def fact(n):
    if n==0 or n==1:
        return 1
    result=1
    for i in range(2,n + 1):
        result*=i
    return result
def prime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
         return False
    return True
def sum_prime(n):
    factorial=fact(n)
    total=0
    for i in range (2,(factorial+1)):
       if prime(i): 
        total+=i
    return total
n=int(input("enter a number"))
print(f"sum primees in factorial {n}!={sum_prime(n)}")    
