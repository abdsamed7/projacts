temps=[]
while True:
    temp=input("enter the temperature values(or 'q' to quit):")
    try:
     if temp.lower()=='q':
        break
     values=float(temp)
     temps.append(temp)
    except ValueError:
       print("please a valid number od 'q' to quit")
if temps:       
 print(f"the number of tomperature values:{len(temps)}")
 print(f"highest value:{max(temps)}")
 print(f"lowest value:{min(temps)}")
 print(f"avirage{sum(temps)/len(temps):.1f}")
else:
  print("no tomperature were entered")
