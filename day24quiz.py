print("=====================") 
print("Quiz Game")
print("=====================")


print("""
Welcome to the Quiz Game!

Rules:
1. There are 5 questions.
2. Each correct answer wins money.
3. One wrong answer ends the game.
4. Good Luck!

""")
print("""Question 1 for Rs. 1,000

What is the capital of Nepal?

A. Kathmandu
B. Pokhara
C. Biratnagar
D. Dharan

""")


choice=(input("Choose correct option(A,B,C,D) : ")).upper()

if choice == "A":
 print("Congratulation you Won RS 1000")
else:
 print("Try Again")
 exit()



print("**************************")

print("""Question for Rs. 2,000


Question 2 Rs. 2,000

What is the national flower of Nepal?

A. Rose
B. Sunflower
C. Rhododendron 
D. Lotus

""")


choice=(input("Choose correct option(A,B,C,D) : ")).upper()

if choice== "C":
 print("Congratulation you Won RS 2000")
else:
 print("Try Again")
 exit()


print("***********************")


print("""
Question 3  Rs. 5,000

What is the national animal of Nepal?

A. Tiger
B. Dog
C. Yak
D. Cow

""")


choice=(input("Choose correct option(A,B,C,D) : ")).upper()

if choice== "D":
 print("Congratulation you Won RS 5,000")
else:
 print("Try Again")
 exit()



print("*******************")
print("""
Question 4  Rs. 10,000

Which is the highest mountain in the world, located in Nepal?

A. Kanchenjunga
B. Dhaulagiri
C. Mount Everest (Sagarmatha) 
D. Annapurna

""")


choice=(input("Choose correct option(A,B,C,D) : ")).upper()

if choice== "C":
 print("Congratulation you Won RS 10,000")
else:
 print("Try Again")
 exit()


print("""
Question 5  Rs. 20,000

Which is the official currency of Nepal?

A. Indian Rupee
B. Dollar
C. Nepali Rupee 
D. Yuan

""")


choice=(input("Choose correct option(A,B,C,D) : ")).upper()

if choice== "C":
 print("Congratulation you Won RS 20,000")
else:
 print("Try Again")
 exit()

print("*************Congratulation You have Won the Quiz gamee*************")