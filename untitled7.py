from datetime import date
from datetime import timedelta
import calendar
date = str(input("enter the date: "))
offset =(date.weekday()- 1) % 7
last_friday = date - timedelta(days=offset)
print(last_friday)

from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
#today = str(input('Enter date(yyyy-mm-dd): '))
#my_date = datetime.strptime(my_string, "%Y-%m-%d")
#Friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
        #my_string += datetime.timedelta(1)


today = datetime.date.str(input('Enter date(yyyy-mm-dd): '))
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )

    