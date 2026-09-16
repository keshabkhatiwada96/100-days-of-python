from datetime import datetime
import calendar

now = datetime.now()

year = now.year
month = now.month
today = now.day

print("Month:", now.strftime("%B"))
print("Year:", year)
print("Today:", today)
print(now.strftime("Time = " "%H:%M:%S"))