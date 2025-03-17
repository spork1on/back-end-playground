#timezones are managed in python with PYTZ
#good practice: all dates are stored in UTC

import datetime
import pytz

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)

d2 = datetime.datetime.now(pytz.timezone("Europe/Oslo"))
print(d2)

## What if isnt possible to use pytz? it can be done with python. However, pytz has no drawbacks, it only makes it easier and better.

time_sp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
time_oslo = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1)))


print(time_sp)
print(time_oslo)
