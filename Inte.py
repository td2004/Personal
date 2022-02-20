import os
import sys
file = ""


list = []
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

