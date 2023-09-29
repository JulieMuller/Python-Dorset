'''
def max(a, b):
    if(a>b):
        print(a)
    else : print(b)

max(5,9)

def max(*numbers):
    listnum = []
    for number in numbers:
        listnum.append(number)
    max = listnum[0]
    min = listnum[0]
    for i in range(len(listnum)):        
        if(listnum[i] > max): max = listnum[i]
        if(listnum[i] < min): min = listnum[i]
    return max, min
    
print(max(5, 9, 7, 4, 3))

def max(listnum):
    max = listnum[0]
    min = listnum[0]
    for i in range(len(listnum)):        
        if(listnum[i] > max): max = listnum[i]
        if(listnum[i] < min): min = listnum[i]
    return max, min

listnum = [5, 0, 7, 4, 2, 3]
print(max(listnum))

try : 
    num = int(input('num  = '))
    if (num%2 == 0): print("even")
    else: print("odd")
except ValueError as error:
    print(error)
else : 
    print("all good")
finally:
    print("over")

f = False
while f != True:
    try : 
        num = int(input('num  = '))
        if (num%2 == 0): print("even")
        else: print("odd")
    except ValueError as error:
        print(error)
    else : 
        f = True

while True:
    try : 
        num = int(input('num  = '))
        if (num%2 == 0): print("even")
        else: print("odd")
    except ValueError as error:
        print(error)      

while True:
    try : 
        num = int(input('num  = '))
        if(num == 0 or num == 1):
            print("enter another number")         
        elif (num < 0): print("negative")
        else:
            c = True
            for  i in range(2,num):
                if num%i == 0:
                    c = False       
            if (c == True) : print("prime")
            else :  print("not prime")
        break
    except ValueError as error:
        print(error)        
'''




import numpy as np

vect = np.linspace(10, 30, 20, dtype=int)
vect[4] = 1
print(vect)

    
