text=input("enter a text:").lower()
vowel=("a","e","o","u","i")
count=0
for vowel in text:
    if vowel in text:
     count+=1
    print("number of vowels:",count)