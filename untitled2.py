import os
import sys
sys.stdout = open("inte.txt", "w")
stringlist = []
r"C:\Users\tcdin\Desktop\python\inte.txt"
for i in range(5):
    stringlist.append(input)
#import math
#prod = ""
list = []
while True:
    try:
        element = float(input("enter numbers: "))
    except ValueError:
        print("Please enter numbers.")
    else:
        break
        
while True:
    list.append(element) 
    element = float(input("enter numbers: "))
    choice = input("want to stop? if yes type yes otherwise hit any key!")
    if choice == "yes":
        break
print("Elements of the list are: ", list)
list.sort()
print("Your list in asending order :",list)
list.sort(reverse=True)
print("Your list in desending order :",list)

for num in list:
    if num%2 == 0:
        print("Even numbers in the list are: " , num)
        
    if num%2 !=0:
        print("Odd numbers are", num)
sum_of_elements = sum(list)
len_of_list = len(list)
avg = sum_of_elements/len_of_list
print("Average is: ", avg)
print("Minimum value is: " , str(min(list)))
print("Maximum value is: " , str(max(list)))
print("Sum of your list is: " , str(sum(list)))
#print("Product of your list is: ", str(prod(list)))
sys.stdout.close()
