
from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
#today = str(input('Enter date(yyyy-mm-dd): '))
#my_date = datetime.strptime(my_string, "%Y-%m-%d")
#Friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
        my_string += datetime.timedelta(1)


today = datetime.date.str(input('Enter date(yyyy-mm-dd): '))
friday = today + datetime.timedelta( (4-today.weekday()) % 7 )

from datetime import datetime
from datetime import date
from datetime import timedelta
#import datetime 
#datetime.utcnow()
#today = str(input('Enter date(yyyy-mm-dd): '))
#my_date = datetime.strptime(my_string, "%Y-%m-%d")
#Friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
        #my_string += datetime.timedelta(1)


#today = datetime_str =(input('Enter date(yyyy-mm-dd): '))
#friday = today + datetime_str.timedelta( (4-today.weekday()) % 7 )

from datetime import datetime, timedelta
date_entry = input('Enter a date in YYYY-MM-DD format')
date1 = datetime.strptime(date_entry, '%Y-%m-%d')
friday = date_entry + datetime.timedelta( (4-data_entry.weekday()) % 7 )