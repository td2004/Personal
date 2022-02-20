import pandas as pd
#Creating dictionary and then converting into a data frame. Example 1
dic1= {"name": ["ball","tall","small","kite"],"age": ["3", "4" , "5", "6"]}
print(dic1)
df = pd.DataFrame(dic1)
df1 = pd.DataFrame(dic1, index = ['a', 'b', 'c', 'd'])
print(df)
print("-------------")
print(df1)
print("------------")
#Creating dictionary and then converting into a data frame. Example 2
data = {"name": ["ball","tall","small","kite"],"age": ["3", "4" , "5", "6"]}
df2 = pd.DataFrame(data)
print(df2)
print("--------------")

#Creating list and printing the data frame. Example 1
data = [['name', 'tall'], ['age', 15]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df )
print("--------------")
#Creating list of list and then converting into a data frame. Example 2
data1 = [['Apple', 'Stock_list', 10], ['Google', 'StockList', 9], ['ADHL', 'ShortList', 7],
        ['Algo', 'List', 8], ['Tesla', 'List', 6], ['BPH', 'List', 5], ]
df3 = pd.DataFrame(data1, columns = ['Stock', 'Type', 'Number'])
print(df3)
print("--------------")

#converting dataframe to dictionary
my_dictionary = df3.to_dict()
print (my_dictionary)
print("-----------")

#converting data frame to list
df4 = pd.DataFrame(data)
list1 = df4.values.tolist()
print(list1)
import pandas as pd
df = open("output_file.txt", "a")
df = pd.read_csv("output_file.txt", sep = " ")
print(df)
df.to_csv("outputt_file.txt", sep = " ")

import os
cwd = os.chdir(r'C:\Users\tcdin\Desktop\New Folder')
df = pd.DataFrame({"a": [1, 6, 14, 20, 35], "b": [14, 5, 60, 50, 46], "c": [7,8,9, 1000, 2004]})
d = pd.DataFrame({"a": [2, 4, 6], "b": [7, 3, 8], "c": [2,4,6]})



df["a*b"] = df["a"] * df["b"]
df["b*c"] = df["b"] * df["c"]
df["a-b"] = df["a"] * df["b"]
df["c-b"] = df["c"] * df["b"]
df["c-b"] = df["c"] * df["b"]
df["b*b"] = df["b"] * df["b"]
df["a*a"] = df["a"] * df["a"]
df["c*c"] = df["c"] * df["c"]
df["ar2-ar1"] = df["a"].diff()
df["br2-br1"] = df["b"].diff()
df["cr2-cr1"] = df["c"].diff()
df["as2-as1"] = df["a"].shift(2) - df["a"].shift(1)
#df["0*1"] = df["0"] * df["1"]
print(df)
df = pd.DataFrame(d)
answer= df.std()
print("The standard deviations of the 3 columns are:")
print (answer)


