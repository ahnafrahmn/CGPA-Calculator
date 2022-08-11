

name = input("Enter your name. \n  ::  ")

courseno = None
while courseno == None:
    try:
        courseno = int(input("how many courses ? \n  ::  "))
    except:
        print("Error, Enter a number! ")

result = 0
creditHrs = 0
allCH = 0
i = 0
while i < courseno:
    grade = input(
        "Enter your grade in letter for the %s no. course ::  " % (str(i+1)))
    creditHrs = int(input("Enter your credit hours for this course  ::  "))
    grade = grade.upper()
    if grade == "A" or grade == "B+" or grade == "B" or grade == "B-" or grade == "C+" or grade == "C" or grade == "C-" or grade == "D+" or grade == "D" or grade == "F":
        i += 1
        allCH += creditHrs
        if grade == "A":
            result += 4*creditHrs

        elif grade == "B+":
            result += 3.7*creditHrs

        elif grade == "B":
            result += 3.4*creditHrs

        elif grade == "B-":
            result += 3.1*creditHrs

        elif grade == "C+":
            result += 2.8*creditHrs

        elif grade == "C":
            result += 2.5*creditHrs

        elif grade == "C-":
            result += 2.2*creditHrs

        elif grade == "D+":
            result += 1.5*creditHrs

        elif grade == "D":
            result += 1.0*creditHrs

        elif grade == "F":
            result += 0.0*creditHrs

    else:
        print("invalid grade!!")


creditHrs = float(creditHrs)
result = float(result)
allCH = float(allCH)


cgpa = "%.2f" % (result/(allCH))
print(name, "your CGPA is :", cgpa)
