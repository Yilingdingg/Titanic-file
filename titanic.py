import pandas as pd

#create a data frame 
df = pd.DataFrame({
    "Name" : ["Crystal", "Amanda","Steffy","Susan", "Ines"],
    "Age" : [20,17,32,19,28],
    "Score" : [80,87,86,92,90],
})
#top 5
print(df.head())
#
print(df.shape)
print(df.info())
print(df.describe())

#seperate datas
age = df["Age"]
print(age)
ageAndname=df[["Name","Age"]]
print(ageAndname)
#filter
below_twenty = ageAndname[ageAndname["Age"]<20]
print(below_twenty)

above_87 = df[df["Score"]>87]
print(above_87)

#read from csv file
dft = pd.read_csv("titanic.csv")
print(dft.head())
print(dft.shape)
print(dft.info())
print(dft.describe())
nameAndsex = dft[["Name","Sex"]]
print(nameAndsex)
#|=or
class2And3 = dft[dft["Pclass"]==2|dft["Pclass"]==3]
maleAndp1 = dft[dft["Sex"]=="Male"&dft["Pclass"]==1]
