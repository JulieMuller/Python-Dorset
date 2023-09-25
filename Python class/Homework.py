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

