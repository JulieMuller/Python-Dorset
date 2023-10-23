#---------------- imports ---------------- 

import matplotlib.pyplot as plt
import numpy as np
import math
#%matplotlib inline #to display graphs in notebooks

#---------------- formating ---------------- 
s = 3
print(f"result {s: .2f}") #Just 2 decimals

#---------------- User inputs ---------------- 
n = int(input("number :")) #do not forget to convert to the right type

#----------------  numpy ---------------- 
import numpy as np
notes = np.empty([3,4]) #n lines, 4 columns
notes = np.random.rand(3, 4) #random, size 3 lines 4 columns
print(notes[:,3]) #prints 3rd column

#---------------- lists ---------------- 
string = ''
names = string.split(' ') #splits in a list on spaces

#---------------- dict ---------------- 
#nested keys -> dictionary in dict
Dict = {"dict 1":{1:"Geeks"},"dict 2":{2:"for"}}
#get items
print(Dict["dict 1"][1]) #fist key, second key outputs value of second key

#get methode doesn't throw error if key doesn't exist it will write default instead
print(Dict.get("dict 1")) #gives value of key

#change value
Dict["dict 1"][1] = "change"
print(Dict["dict 1"][1])

#add item
Dict["dict 1"][3] = "test"
print(Dict["dict 1"][3])

print("dict 1" in Dict) #check if key is in the list

#iterate through dict
for keys, values in Dict.items():
    print(keys)
    print(values)

#"adds" 2 dicts
cities = ("paris", "madrid")
country = ("france", "spain")
dict = dict(zip(cities, country))
print(dict)
#adds a dict to an existing one
dict2 = {"ten" : 10}
dict.update(dict2)
print(dict)

dict = {"name" : "kelly", "age" : 25, "salary" : 200, "city" : "NY"}
keys = ["name", "salary"]
for key in keys:
    del dict[key]
print(dict)

print("NY" in dict.values())

#---------------- plot ---------------- 
start, end, nbpt = 1,3,3
x = np.array(np.linspace(start, end, nbpt))

y = ((1/math.sqrt(2*math.pi))*np.exp(-(1/2)*((x-x0)**2/s**2))) 

plt.plot(x, y, label="x0 = %s, s = %s" %(x0, s))
plt.title("Gaussian function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

#---------------- try except ---------------- 
try : 
    #code to exectue
    pass
except Exception as variable_name: #exception = ValueError
    #error action
    print(variable_name)
    pass
else : #not mendatory
    pass
finally: #not mendatory
    pass

#---------------- several input ---------------- 
def max(*numbers):
    print(numbers[4])    
max(5, 9, 7, 4, 3)

#---------------- git ----------------
"""
Git
git add -A        git commit -m "Commit 2"       git pull          git push
"""