import os
import sys 
raw_input = ''
# file = input("file.txt: ")
# with open(file, "w") as f:
#   f.write(input())
fd = open(file.txt,"w")
input = raw_input("user input")
fd.write(input)
#   text_file = open("file.txt", "r+")
sys.stdout = open("inte.txt", "w")
r"C:\Users\tcdin\Desktop\python\inte.txt"
r"C:\Users\tcdin\Desktop\python\file.txt"

list = []
# while True:
#     try:
#         element = float(input("enter numbers: "))
#     except ValueError:
#         print("Please enter numbers.")
#     else:
#         break
        
# while True:
#     list.append(element) 
#     element = float(input("enter numbers: "))
#     choice = input("want to stop? if yes type yes otherwise hit any key!")
#     if choice == "yes":
#         break
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
#avg = sum_of_elements/len_of_list
#print("Average is: ", avg)
# print("Minimum value is: " , str(min(list)))
# print("Maximum value is: " , str(max(list)))
# print("Sum of your list is: " , str(sum(list)))
sys.stdout.close()