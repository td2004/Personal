import calendar
from datetime import timedelta
import datetime
list = ["31.03.2004"]
d=int(input("Enter a date: "))
m=int(input("Enter month: "))
y=int(input("Enter year: "))
birthday = ["31.03.2004" ]
given_date = datetime.datetime(y, m, d)
day = given_date + timedelta(days = 1) 
week = given_date + timedelta(days = 7) 
year = given_date + timedelta(days = 365) 
print("Tommorrow's date is:", day)
print("One week from now is:", week)
print("Next year is : ", year)
day = calendar.weekday(y,m,d)
weekDay = calendar.day_name[day]
print(y,"/",m,"/",d, "is a", weekDay)
#Not working
if given_date in list:
    print("Birthday")

    
    



