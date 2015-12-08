""" Identifies the current BLS report Month and Year based on the 
current date and time"""

import datetime
from pytz import timezone
import pytz

jan_2016 = datetime.datetime(2016, 1, 8, 8, 30, 0)


def current_report():
	#identify the current year
	year = datetime.datetime.now().year
	
	pass

print jan_2016.year
print jan_2016.month
print jan_2016.day
print jan_2016.hour
print jan_2016.min
print jan_2016.second
print jan_2016.tzinfo


