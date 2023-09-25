"""
Make a program that asks for the name of the students who have taken the exam 
and the grade out of 10 they have obtained (in two different lines) until only 
the Enter key is pressed without any name. Names should be saved in one list and grades in another.
Once the data has been entered, the program must write the arithmetic mean of 
the grades and grades of all students so that the writing must be done in two 
columns with the name on the first and the note in the second.
"""
name = []
grade = []
nameinput = input("Nom : ")
m = 0

while (nameinput != ""):
    gradeinput = int(input("Grade : "))
    grade.append(gradeinput) 
    nameinput = input("Nom : ")
    name.append(nameinput)
    
for i in range(len(grade)-1):
    print("Nom : {:14} | Note : {:5.1f}".format(name[i], grade[i]))
    m += grade[i]
print("mean = %s" %m)

