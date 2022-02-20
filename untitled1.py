import time
import datetime
import datetime
def last_day_of_month(any_day):
	# get close to the end of the month for any day, and add 4 days 'over'
	next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
	# subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
	return next_month - datetime.timedelta(days=next_month.day)


last_date_of_month= ""
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

from datetime import date, timedelta

def all_fridays(year):
       dt = date(year, 1, 1) 
       dt += timedelta(days = 6 - dt.weekday())  
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)
          
for s in all_fridays(2020):
   print(s)


from datetime import date, timedelta

last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)

start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)


print("First day of prev month:", start_day_of_prev_month)
print("Last day of prev month:", last_day_of_prev_month)