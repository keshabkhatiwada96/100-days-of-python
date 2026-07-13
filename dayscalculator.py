from datetime import datetime
date1 = input("Enter first date (DD/MM/YYYY):")
date2 = input("Enter second date (DD/MM/YYYY):")
first_date = datetime.strptime(date1, "%d/%m/%Y")
second_date = datetime.strptime(date2, "%d/%m/%Y")
difference = abs((second_date-first_date). days)
print("Difference between the two dates is", difference, "days.")