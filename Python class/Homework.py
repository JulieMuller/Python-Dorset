"""
Make a program that asks for the name of the students who have taken the exam 
and the grade out of 10 they have obtained (in two different lines) until only 
the Enter key is pressed without any name. Names should be saved in one list and grades in another.
Once the data has been entered, the program must write the arithmetic mean of 
the grades and grades of all students so that the writing must be done in two 
columns with the name on the first and the note in the second.
"""
'''
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
'''

"""
Create a dictionary to store this information, indexed by the symbol. 
Then write a function which allows the user to specify an element (via its symbol) and a temperature, 
and which reports whether the element is solid, liquid or gas at that point.
"""
element = {"H": [1, 14, 20], "He": [2, 1, 4], "Li": [3, 453, 1603]}
def Symbol(symbol, temp):
    values = element[symbol]
    if values[1] > temp:
        print("Solid")
    if values[1] < temp and values[2] > temp:
        print("liquide")
    else : print("gaz")

Symbol("H", 90)

"""
Use a dictionary to store this information, and modify your function so
 that the user can specify which bank provides their mortgage. 
 You can assume that the monthly interest rate is simply one-twelfth of 
 these annual rates.
"""
bank = {"ANZ": [2.3, 4.1], "Bank of Australia": [0.1, 5], "Commonwealth Bank": [3.5, 3.8], "Westpac": [3.7, 3.7]}


