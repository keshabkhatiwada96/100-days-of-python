a = int  (input("enter yout number:  " ))
operator= (input("enter your operator (+,-,*,/); "))
b = int (input ("enter your second number: "))
if operator=="+":
 print ("sum = ", a+b)
elif operator=="-":
 print ("sub = ", a-b)
elif operator=="*":
 print ("mul = ", a*b)
elif operator=="/":
 print ("div = ", a/b)
else :
 print("invalid operator")