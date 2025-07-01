def filter_even(numbers):
    even_numbers=[]
    for num in numbers:
       if num%2==0:
           even_numbers. append(num)
           return even_numbers
all_numbers=[]
while True:
 num=input("enter even number or 'q' to exit :")
 if num.lower()=='q':
    break
 try:
    number=int(num)
    all_numbers . append(number)
 except ValueError:
    print("please enter a valid number")    
print(f"even number is {filter_even(all_numbers)}")
        