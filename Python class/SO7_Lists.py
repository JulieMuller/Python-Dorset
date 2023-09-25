'''
a = []
b = input('number : ')
m = 0
while b != "":
    a.append(b)
    b = float(b)
    m += b
    b = input('number : ')
print("mean =  {}".format(m/(len(a))))

names = []
userinput = input('names : ')
names = userinput.split(' ')
for values in names:
    print("hi %s" % values)


element = ["H", "C", "N", "O", "S", "Cl"]
atomic_mass = [1.008, 12.011, 14.007, 15.999, 32.065, 35.453]
result = 0
name_element = input("Name of the element : ")
while name_element != '':
    numb_element = int(input("Number of atoms : "))
    result += numb_element * atomic_mass[element.index(name_element)]
    name_element = input("Name of the element : ")
print(result)

n = int(input("Maximum degree n = "))
coef = []
result = 0
coef.append(float(input("Coef degree 0 = ")))
for i in range(n):
    coef.append(float(input("Coef degree %s = " % (i+1))))
x = float(input("x  = "))
for i in range(n+1):
    result += coef[i]*x**(i)
print("The result for x = %s is %s" % (x, result))


Dict = {}

#nested keys -> dictionary in dict
Dict = {"dict 1":{1:"Geeks"},"dict 2":{2:"for"}}

#get items
print(Dict["dict 1"][1])
#get methode doesn't throw error if key doesn't exist it will write default instead
Dict.get("key")

#change value
Dict["dict 1"][1] = "change"
print(Dict["dict 1"][1])

#add item
Dict["dict 1"][3] = "test"
print(Dict["dict 1"][3])

#delete item
del Dict["dict 1"][3]
#Dict.clear()

print("dict 1" in Dict) #check if key is in the list

#iterate through dict
for keys, values in Dict.items():
    print(keys)
    print(values)

cities = ("paris", "madrid")
country = ("france", "spain")
dict = dict(zip(cities, country))
print(dict)

dict2 = {"ten" : 10}
dict.update(dict2)
print(dict)


dict = {"name" : "kelly", "age" : 25, "salary" : 200, "city" : "NY"}
keys = ["name", "salary"]
for key in keys:
    del dict[key]
print(dict)

print("NY" in dict.values())
'''

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
'''



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
    #code to exectue
    pass
except Exception:
    #error action
    pass
else : #not mendatory
    pass
finally: #not mendatory
    pass