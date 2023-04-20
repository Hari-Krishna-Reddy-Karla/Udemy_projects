 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower() + name2.lower()

x = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
y = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")

score = str(x) + str(y)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")