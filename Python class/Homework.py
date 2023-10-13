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

"""
S09_10 Exam grades
Make a program that asks for the number of students who have taken an exam and the marks (from 0 to 10) that they have obtained in the theory part and the problem part (in different lines), which account 40% and a 60% respectively in the final grade. These notes must be saved in 2 vectors.
The program:
1.	Write a table with 4 columns containing the student's order index (0, 1, 2, ...), theory note, problem mark and total mark.
2.	You must also write the maximum total grade, the minimum total grade and the average total grade.
3.	And finally you have to write the position (index) of the maximum total grade.
"""

import numpy as np

n = 2
notes = np.empty([n,4])

for i in range(n):
    notes[i][0] = i

    note = float(input("Student %s theory note :" % i))
    notes[i][1] = note

    mark = float(input("Student %s problem mark :" % i))
    notes[i][2] = mark

    total_mark = float(input("Student %s  total mark :" % i))
    notes[i][3] = total_mark
print(notes[:,3])
print("max total mark = {}, minimum total grade = {}, average total grade =  {}, index of max total grade = {}".format(max(notes[:,3]), 
                                                                                                                       min(notes[:,3]), 
                                                                                                                       np.mean(notes[:,3]),  
                                                                                                                       notes[:,3].argmax()))

"""S09_6 Sea temperature statistics
data are in the list called temp_mar sorted chronologically:
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
We also have a second list with the name of the months:
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
Write a program that
•	Define the above lists.
•	Convert the temp mar list to a NumPy array.
•	Determine, using the statistical functions of numpy, and write:
o	The average sea surface temperature in 2014. (Approximate response: 17.9 ºC.)
o	The month in which the sea surface has been coldest and its temperature. (Answer: 13.3 ºC, February.)
o	The month in which the sea surface has been warmest and its temperature. (Answer: 22.3 ºC, August.)
"""

import numpy as np

temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
temp_mar = np.array(temp_mar)
print("The average sea surface temperature in 2014 = {:.1f}" .format(np.mean(temp_mar)))
print("The month in which the sea surface has been coldest and its temperature = {}, {}" .format(months[temp_mar.argmin()], min(temp_mar)))
print("The month in which the sea surface has been coldest and its temperature = {}, {}" .format(months[temp_mar.argmax()], max(temp_mar)))


"""
The program must:
1.	Request the values of x0 and s.
2.	You must also ask for the initial and final values of the x interval and the number of points that the table must have.
3.	You must generate a numpy vector with equidistant x values.
4.	You must generate the numpy vector of the y from that of thex with a single instruction.
5.	You must use the x, y value table obtained using afor (a pair x andy in each line)
6.	The values of x should be written with 3 decimals and those ofy with 5.
(Check: For x0 = 0 and s = 0.3 in the interval [-1, 1] and n = 6 the program must write the following table of 6 values:
"""

import numpy as np
import math

x0 = float(input("Xo = "))
s = float(input("s = "))
iinterval = int(input("initial value = "))
finterval = int(input("final value = ")) 
n = int(input("n = "))


x = np.linspace(iinterval, finterval, n)

y = np.exp(-((x - x0) ** 2) / (2 * s ** 2))
y = (1/math.sqrt(2*math.pi)) * np.exp(-(1/2)*((x-x0)**2/s**2))


for i in range(len(x)):
    print("{:.3f} | {:.5f}".format(x[i], y[i]))


'''
S09_4 Convert Angstroms to Nanometers
Write a program that converts a vector of values in Angstroms (Å) to nanometers.
The program must construct an array of 21 equally spaced values ranging from 1.0 Å to 5.0 Å
 that can correspond for example to values of an interatomic distance, and must convert the 
 values to nanometers using the same array for save the result. Finally, the program must write the array. (Data: 1 Å = 0.1 nm).
'''
import numpy as np


a = 1.0
b = 5.0
n = 21

angstroms = np.linspace(a, b, n)
nanometers= angstroms * 0.1

print("Values in Angstroms (Å): %s" % angstroms)
print("\nValues in nanometers (nm): %s" % nanometers)