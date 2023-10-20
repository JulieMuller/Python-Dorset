import numpy as np


"""
Write a NumPy program to create a vector with values 
from 0 to 20 and change the sign of the numbers in the 
range from 9 to 15."""

vect = np.linspace(0,20,21)
vect[9:16] = -vect[9:16]
print(vect)

'''Write a NumPy program to create a vector with values ranging 
from 15 to 55 and print all values except the first and last.'''

vect = np.linspace(15, 55, 55-15+1)
print(vect)
print(vect[1:len(vect)-1])

"""Write a NumPy program to create a 3X4 array and iterate over it."""

mat = np.random.rand(3,4)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j], end = " ")
    print(' ')

"""Write a NumPy program to create a vector of length 
10 with values evenly distributed between 5 and 50."""

print(np.linspace(5, 50, num = 10))

'''Write a NumPy program to create a vector of length
 5 filled with arbitrary integers from 0 to 10.'''

print(np.random.randint(0, 11, 5))

"""Write a NumPy program to multiply the values of two given vectors."""

vect1 = np.random.randint(0,10, 5)
vect2 = np.random.randint(0,10, 5)
print(vect1, vect2, vect1*vect2)

'''Write a NumPy program to create a 3x4 matrix 
filled with values from 10 to 21.'''

print(np.arange(10,22).reshape((3, 4)))

'''Write a NumPy program to find the number of 
rows and columns in a given matrix.'''

mat = np.arange(10,22).reshape((3, 4))
print("rows = %s, columns = %s" %(len(mat), len(mat[0])))

"""Write a NumPy program to create a 4x4 matrix 
in which 0 and 1 are staggered, with zeros on the main diagonal."""

mat = np.zeros((4, 4))
mat[0::2, 1::2] = 1 #une ligne et une colonne sur 2
mat[1::2, 0::2] = 1 
print(mat)

'''Write a NumPy program to find common values between two arrays.
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [10, 30, 40]
Common values between two arrays:
[10 40]
'''

array1 = np.random.randint(0, 10, 5)
array2 = np.random.randint(0, 10, 3)
array3 = np.empty(0)
print(array1, array2, array3)

for i in range(len(array1)):
    for j in range(len(array2)):
        if(array1[i] == array2[j]):
            array3 = np.append(array3, array2[j])
print(array1, array2, array3)

"""Write a NumPy program to get the unique elements of an array.
Expected Output:
Original array:
[10 10 20 20 30 30]
Unique elements of the above array:
[10 20 30]
Original array:
[[1 1]
[2 3]]
Unique elements of the above array:
[1 2 3]
"""

x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))

"""Write a NumPy program to compute the cross
 product of two given vectors."""

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)

"""Write a NumPy program to convert cartesian coordinates to 
polar coordinates of a random 10x2 matrix representing cartesian
 coordinates."""
import numpy as np
z= np.random.random((10,2))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)

"""Write a NumPy program to find the closest value 
(to a given scalar) in an array."""
import numpy as np 
og = np.linspace(0,99, 100)

recherche = 6.999
save = abs(og[0]-recherche)
result = 0

for i in range(len(og)):
    dif = abs(og[i]-recherche)
    print(dif)
    if(save > dif):
        result = og[i]
        save = dif
print(result)