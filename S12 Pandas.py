import pandas as pd


'''
df = pd.read_csv("C:\\Users\\Mulle\\Desktop\\AIDorset\\S12\\Educational_Attainment_20231027.csv")

df.head(5)
df.tail(5)
df.shape()
df.describe()
df.dtypes()
df.drop("Geography", axis = 1).describe(include="all") #axis = 1 move columns 1 step ahead otherwise empty column, include all = include strings

df = pd.read_csv("C:\\Users\\Mulle\\Desktop\\AIDorset\\S12\\survey_results_public.csv")

#good for notebooks but not so much for console
pd.set_option('display.max_rows', 85)
pd.set_option('display.max_columns', 85)
print(df)
'''

baby_names = pd.read_csv("C:\\Users\\Mulle\\Desktop\\AIDorset\\S12\\US_Baby_Names_right.csv")
print(baby_names.head(10))
baby_names.drop('Unnamed: 0', axis=1)
baby_names.drop('Id', axis=1)
print(baby_names.head(10))

m= 0
f =0
for genders in baby_names["Gender"]:
    if(genders == "M") : 
        m += 1
    else:
        f = 0
if(m>f):
    print("male")
else:
    print("female")

print(baby_names.groupby('Name').describe())
