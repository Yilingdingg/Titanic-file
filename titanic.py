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
print(class2And3)
print(maleAndp1)
#is in method
class2A3 = dft[dft["Pclass"].isin([2,3])]
print(class2A3)
maledata = dft[dft["Sex"].isin(["male"])]
print(maledata)
# get the particular column out of a condition
# ex: get names of adult passengers
adult_names = dft.loc[dft["Age"]>18,"Name"]
print(adult_names)
female_names = dft.loc[(dft["Sex"]=="female")&(dft["Age"]>18),"Name"]
print(female_names)
# specify the number of rows and the particular column
column_5 = dft.iloc[0:6,2]
print(column_5)
columns = dft.iloc[50:101,1:3]
print(columns)
# group by data categorically
average_age = dft.groupby('Sex')['Age'].mean()
print(average_age)
# ex: get the mean ticket price for each of sex and cabin class combination
average_price = dft.groupby(['Sex','Pclass'])['Fare'].mean()
print(average_price)
print(adult_names.value_counts())
print(adult_names.count())
# sorting the data
# entire data sort by age
age_sort = dft.sort_values(by = "Age", ascending = True)
print(age_sort.iloc[:,4])
