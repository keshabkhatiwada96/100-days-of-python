#  Random 4-Digit OTP Generator and Verification
# This program generates a random 4-digit One-Time Password (OTP). 
# After the OTP is generated, the user is prompted to enter it. 
# If the entered OTP matches the generated OTP, the program displays a **"Login Successful"** message.
#  Otherwise, it displays **"Wrong OTP"** and the program terminates.

import random

input("press ENTER to generate a random OTP.. ")
OTP = random.randint(1000,9999)
print("\nYour OTP:\n",OTP)

user_otp=int(input("enter your OTP: "))
if user_otp== OTP:
 print("Login Sucessful")
 print("""\
 "🎉 **Congratulations!** 🎉

You have successfully logged in.

Your OTP has been verified successfully. Welcome! We hope you have a great experience using the system.
""")
else:
 print("wrong OTP")