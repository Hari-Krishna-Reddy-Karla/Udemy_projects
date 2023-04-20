print("welcome to the rollercoster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("what is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want a photo taken Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your total bill is {bill}")

    print(f"Your bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
