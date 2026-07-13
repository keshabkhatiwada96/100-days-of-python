# making money exchange here 
print("this is converter of NPR to USD,EUR,AUD&GBP")
print("1 = USD, 2 = EUR, 3 = AUD, 4 = GBP ")
choice = int(input("Enter choice (1-4): "))

match choice:
  case 1 :
    amount=float(input("enter your USD amt: "))
    npr = amount*156
    print("NPR =",npr)



  case 2 :
    amount=float(input("enter your EUR amt: "))
    npr = amount*176
    print("NPR =",npr)

  case 3 :
    amount=float(input("enter your AUD amt: "))
    npr = amount*105
    print("NPR =",npr)

  case 4 :
    amount=float(input("enter your GBP amt: "))
    npr = amount*202
    print("NPR =",npr)

  case  _:
     print("invalid choice ")


 