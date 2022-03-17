day = int(input("enter a day(dd): "))
month = int(input("enter a month(mm): "))
year = int(input("enter a year(yyyy): "))
count = 0
# This is to check if the month has 31,30,29,28 days
def function (month, year):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==12:
        max_days=31
    elif month==4 or month==6 or month==9 or month==11:
        max_days=30
    elif year%4 or year%100 or year%400:
        max_days=29
    else:
        max_days=28
    return max_days
# This calls the function and converts it to a str value so that it can be concatinated
while True:
    max_days1 = function(month,year)
    if (day>0 and day<=max_days1) and (month>0 and month<13):
        dd = str(day)
        mm = str(month)
        yyyy = str(year)
    else:
        print("Invalid Date")
        break
       # This to ensure that there are always two digits. This is to convert 3 into 03 otherwise won't work.
        if month<10:
            mm = "0" +mm
        if day<10:
            dd = "0" +dd
        given_date = dd+mm+yyyy
    reversed_date = given_date [::-1]
    if given_date == reversed_date:
        if count ==0:
            print (day, "/", month, "/",year, "Date is palindrome")
        else:
            print (day, "/", month, "/",year, "Is the next palindrome date")
        break
    #This is for print the next palindromic date
    else:
       day = day + 1
       if day>max_days1:
           day =1
           month=month+1
           if month>12:
               month = 1
               year = year+1
               count = count+1
#comment for github trial1
#comment for github trial2!

    
 
        

        






