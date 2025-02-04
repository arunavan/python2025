import time
import datetime
import calendar
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))  


print(datetime.datetime(2025,5,3,6,8,9))  #custom date
print(datetime.datetime(2025,5,3)) 
print(datetime.datetime.now()) 

cal=calendar.month(2025,3)
cal1=calendar.FEBRUARY

html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
html_calendar_str = html_cal.formatmonth(2025, 3)
print(html_calendar_str)

print(cal)



# Iterate over the days of February 2025
for day in calendar.Calendar().itermonthdays(2025, 4):
    print(day, end=' ')

print(calendar.calendar(2025))

print(calendar.calendar(8))
print(calendar.TextCalendar(calendar.APRIL).firstweekday)