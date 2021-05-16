import datetime
import pytz


today = datetime.date.today()
print(today)

birthday = datetime.date(1999, 6, 22)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today - tdelta)

#print(today.weekday())

print(datetime.time(5, 8, 20, 76))
"""datetime.date(Y, M, D)
datetime.time (hour, minute, second, microseconds)
datetime.datetime (Year, Month, Day, hour, minute, seconds, microseconds)"""


#Add ten hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Africa/Johannesburg'))
print(datetime_pacific)

#for tz in pytz.all_timezones:
    #print(tz)

#string formating with dates
#2021-5-7 => May 7, 2021

#strftime =>(f = formatting)
print(datetime_pacific.strftime('%B %d, %Y'))

#May 07, 2021 -> datetime(2021, 5, 7)
"use method called strptime (p = parsing)"
datetime_thing = datetime.datetime.strptime('May 07, 2021', '%B %d, %Y')
print (datetime_thing)

