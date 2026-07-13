import datetime
import nepali_datetime

while True:
    print("\n==============================")
    print("      DATE CONVERTER")
    print("==============================")
    print("1. AD to BS")
    print("2. BS to AD")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            year = int(input("Enter AD Year: "))
            month = int(input("Enter AD Month: "))
            day = int(input("Enter AD Day: "))

            ad_date = datetime.date(year, month, day)
            bs_date = nepali_datetime.date.from_datetime_date(ad_date)

            print("\n Nepali Date:", bs_date)

        except ValueError:
            print("\n Invalid English date!")

    elif choice == "2":
        try:
            year = int(input("Enter BS Year: "))
            month = int(input("Enter BS Month: "))
            day = int(input("Enter BS Day: "))

            bs_date = nepali_datetime.date(year, month, day)
            ad_date = bs_date.to_datetime_date()

            print("\n English Date:", ad_date)

        except ValueError:
            print("\n Invalid Nepali date!")

    elif choice == "3":
        print("\nThank you for using the Date Converter!")
        break

    else:
        print("\n Invalid choice! Please enter 1, 2, or 3.")