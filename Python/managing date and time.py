### To manage date and time python demands that a full datetime is stabilished and then its possible to manipulate it with .date() or .time
import datetime

resultado = datetime.datetime.now() - datetime.timedelta(hours=1)
print(resultado) # show full date and time
print(resultado.time()) # show only time
print(resultado.date()) # show only date

### CONVERTING AND FORMATING DATETIME

#FORMATING - STRFTIME (format)
d = datetime.datetime.now()

print(d.strftime("%d/%m/%y %H:%M"))

#CONVERTING STRING TO DATETIME - STRPTIME (parse)
current_datetime = datetime.datetime.now()
datetime_str = "2023-10-20 10:20"
mask_ptbr = "%d/%m/%Y %a" # %a shows the week day
mask_en = "%Y-%m-%d %H:%M"

print(current_datetime.strftime(mask_ptbr))

print(type(datetime_str)) #class string
converted_date = datetime.datetime.strptime(datetime_str, mask_en)
print(type(converted_date)) #class datetime.datetime


