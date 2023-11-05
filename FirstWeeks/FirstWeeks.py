"""
#sum of n first int
n = int(input("number :"))
s=0
for i in range(n+1):
    s = s+i
print(s)

#some formula
n = int(input("number :"))
s=0
for j in range(1, n+1):
    s += (j+1)/j**2
print(f"result {s: .2f}") #Just 2 decimals

#factorial of positive int
n = int(input("number :"))
s=1
for j in range(1, n+1):
    s = s*j
print("result %s" % s)

#repetitive 2 digits
for i in range(1, 10):
    for j in range(1, 10):
        print("result %s%s" % (i,j))

#not repetitive 2 digits
for i in range(1, 10):
    for j in range(1, 10):
        if (i != j):
            print("%s%s" % (i,j))

#some formula
n = int(input("number :"))
s=0
for j in range(0, n+1):
    s = j*(j+1)/2
    print(f"result {s}")

#repetitive 3 digits
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            print("%s%s%s" % (i,j,k))

#psoitive int less than 1000 such as sum of digits = 22
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if(i+k+j == 22):
                print("%s%s%s, sum of the digits : %s" % (i,j,k, (i+j+k)))

#sum of squares = number
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if(i**3+k**3+j**3 == int(str(i)+str(j)+str(k))):
                print("%s, sum of the digits squared : %s" % ((int(str(i)+str(j)+str(k)), (i**3+k**3+j**3))))

#sum of squares = number
n = int(input("number = "))
c=0
for i in range(1, n+1):
    if(n%i == 0) : 
        c+=1
        print("%s, %s" % (i, c))

#sequence of n odd numbers
n = int(input("number = "))
s = 0
for i in range(0, n):
    c = 2*i+1
    s += c
    print(c)
print("sum = %s" % s)

#is it prime?43
n = int(input("number = "))
c = True
for  i in range(2,n):
    if n%i == 0:
        c = False       
if (c == True) : print("prime")
else :  print("not prime")
"""

#fibonacci
n = int(input("number :"))
a = 0
b = 1
s = 0
for j in range(1, n+1):        
    print(s)
    s = a + b
    t = a
    a = s
    b = t    

