from datetime import *
import pytz

current=datetime.now()
print(current)
timez=datetime.now(pytz.utc)
print('The current timezone is :{}'.format(timez))
timeUS=datetime.now(pytz.timezone('US/Central'))
print('The current US timezone is :{}'.format(timeUS))
print()


east_zone=datetime.now(pytz.timezone('America/New_York'))
print('US Eastern timezone datetime :',east_zone.strftime("%Y/%m/%d %H:%M:%S"))

from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))


# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))
