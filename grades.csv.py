with open("C:/Users/luxis computar/OneDrive/Bureau/formation pathon/home work/grades.csv.py", "r") as infile:
    lines = infile.readlines()
with open("averages.csv", "w") as outfile:
    outfile.write("StudentName,Average,Status\n") 
    for line in lines:
        parts = line.strip().split(",")  
        name = parts[0]
        scores = []
        for item in parts[1:]:
            item = item.strip()
            if item.isdigit():  
                scores.append(int(item))
        if scores:
            average = sum(scores) / len(scores)
            status = "Pass" if average >= 50 else "Fail"
        else:
            average = 0
            status = "Fail"
        outfile.write(f"{name},{average:.2f},{status}\n")

