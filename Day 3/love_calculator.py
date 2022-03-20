# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_int = 0
second_int = 0

first_int += name1.lower().count("t")
first_int += name2.lower().count("t")
first_int += name1.lower().count("r")
first_int += name2.lower().count("r")
first_int += name1.lower().count("u")
first_int += name2.lower().count("u")
first_int += name1.lower().count("e")
first_int += name2.lower().count("e")

second_int += name1.lower().count("l")
second_int += name2.lower().count("l")
second_int += name1.lower().count("o")
second_int += name2.lower().count("o")
second_int += name1.lower().count("v")
second_int += name2.lower().count("v")
second_int += name1.lower().count("e")
second_int += name2.lower().count("e")

final_score = int(f"{first_int}{second_int}")

if(final_score < 10 or final_score > 90):
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif(final_score > 40 and final_score < 50):
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")