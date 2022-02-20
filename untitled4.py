import os
import sys
sys.path.append ('/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages')

#sys.stdout = open(r"C:\Users\tcdin\Desktop\python\inte.txt", "w")
#sys.stdout = open("inte.txt", "w")
#r"C:\Users\tcdin\Desktop\python\inte.txt"
#r"/Users/arpitha/Desktop/Algo/inte.txt"

cwd = os.chdir(r'C:\Users\tcdin\Desktop\python')
netfilename = "inte.txt"

with open(netfilename, 'a') as the_file:
    list = []
    while True:
        try:
            element = float(input("enter numbers: "))
        except ValueError:
            print("Please enter numbers.")
        else:
            list.append(element)
            choice = input("want to stop? if yes type yes otherwise hit any key!")
            if choice == "yes":
                break
    print("Elements of the list are: ", list)
    the_file.write("\nElements of the list are: %s " %(str(list)))
    list.sort()
    print("Your list in asending order :",list)
    the_file.write("\nYour list in asending order : %s " %(str(list)))
    list.sort(reverse=True)    
    print("Your list in desending order :",list)
    the_file.write("\nYour list in descending order : %s " %(str(list)))
   
    for num in list:
        if num%2 == 0:
            print("Even numbers in the list are: " , num)
            the_file.write("\nEven numbers in the list are: %s " %(str(num)))
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
    #sys.stdout.close()