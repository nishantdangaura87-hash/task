# QN.1

a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b & a > c:
    print("The largest number is : {a}")
elif b > a & b > c:
    print("The largest number is : {b}")
elif c > a & c > b:
    print("The largest number is : {c}")
else:
    print("All numbers are equal")

# QN.2

month_num = int(input("Enter month number (1-12): "))

if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
else:
    print("Invalid month number")


# QN.3
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num1, num2 = num2, num1
print(num1, num2)

# QN.4

age = int(input("Enter your age: "))
if age < 12:
    price = "free"
else:
    if age >= 12 and age <= 60:
        membership = input("Do you have a membership card? (yes/no): ")
        if membership == "yes":
            price = 150
        else:
            price = 200
    else:
        price = 100
print(f"The ticket price is {price}")

# QN.5

unit = float(input("Enter the electricity usage in units : "))
if unit < 100:
    bill = unit * 5
elif unit <= 300:
    bill = (100 * 5) + ((unit - 100) * 8)
else:
    bill = (100 * 5) + (200 * 8) + ((unit - 300) * 10)

print(f"The total electricity bill is Rs. {bill}")


# Qn.6

player1 = input("Player 1, enter your move (rock, paper, or scissors): ")
player2 = input("Player 2, enter your move (rock, paper, or scissors): ")
if player1 not in ["rock", "paper", "scissors"] or player2 not in ["rock","paper","scissors"]:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    if player1 == player2:
        print("It's a tie!")
    else:
        if player1 == "rock":
            if player2 == "scissors":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        else:
            if player1 == "paper":
                if player2 == "rock":
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")
            else:
                if player2 == "paper":
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")



# QN.7

a = int(input("Enter the number of students in class A: "))
b = int(input("Enter the number of students in class B: "))
c = int(input("Enter the number of students in class C: "))
desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2
total_desks = desks_a + desks_b + desks_c
print(f"The smallest possible number of desks that can be purchased is: {total_desks}")

# QN.8

current_floor = 5
requested_floor = 3
if requested_floor > current_floor:
    direction = "up"
elif requested_floor < current_floor:
    direction = "down"
else:
    direction = "stay at the current floor"
print(f"The lift should go {direction}.")

# QN.9

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print(f"{num} is positive and even.")
    else:
        print(f"{num} is positive and odd.")
else:
    print(f"{num} is not positive.")

# QN.10

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    if num1 > 0:
        print(f"The numbers are equal and the number is positive.")
    elif num1 < 0:
        print(f"The numbers are equal and the number is negative.")
    else:
        print(f"The numbers are equal and the number is zero.")


# QN.11

num = input("Enter a number: ")
num_str = str(num)
reversed_num_str = num_str[::-1]
if num_str == reversed_num_str:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# QN.12

import random

random_number = random.randint(0, 5)
if random_number == 0:
    print("Flamingos turn pink from eating shrimp.")
elif random_number == 1:
    print("The only food that doesn't spoil is honey.")
elif random_number == 2:
    print("Shrimp can only swim backwards.")
elif random_number == 3:
    print("A taste bud's life span is about 10 days.")
elif random_number == 4:
    print("It is impossible to sneeze while sleeping.")
else:
    print("It is illegal to sing off-key in North Carolina.")


# QN.13

total_amount = float(input("Enter the total purchase amount (in Rs.): "))
member_input = input("Are you a member? (True/False): ")
member = member_input == "true"
if total_amount > 1000 and member:
    discount_rate = 0.20
elif total_amount > 1000 and not member:
    discount_rate = 0.10
else:
    discount_rate = 0.00
discount = total_amount * discount_rate
final_amount = total_amount - discount
print(f"The final amount after discount is Rs. {final_amount:.2f}")


# QN.14

earth_weight = float(input("What is your Earth weight? "))
planet = int(input("Enter a planet number (1-7): "))
if planet == 1:
    gravity = 0.38
    planet_name = "Mercury"
elif planet == 2:
    gravity = 0.91
    planet_name = "Venus"
elif planet == 3:
    gravity = 0.38
    planet_name = "Mars"
elif planet == 4:
    gravity = 2.53
    planet_name = "Jupiter"
elif planet == 5:
    gravity = 1.07
    planet_name = "Saturn"
elif planet == 6:
    gravity = 0.89
    planet_name = "Uranus"
elif planet == 7:
    gravity = 1.14
    planet_name = "Neptune"
else:
    print("Invalid planet number")
    exit()
dest_weight = earth_weight * gravity
print(f"Your weight on {planet_name} is {dest_weight}")


# QN.15

mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))
mark4 = int(input("Enter marks for subject 4: "))
total_marks = mark1 + mark2 + mark3 + mark4
percentage = (total_marks / 400) * 100
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

# QN.16

cost_price = float(input("Enter the cost price of the bike (in Rs): "))
if cost_price > 100000:
    tax_rate = 15
elif cost_price > 50000:
    tax_rate = 10
else:
    tax_rate = 5
tax = cost_price * (tax_rate / 100)
print(f"The road tax to be paid is Rs. {tax:.2f}")


#QN.17

years = int(input("Enter years of service: "))

if years > 10:
    bonus = 0.10
    print("Bonus: 10%")
elif years >= 6 and years <= 10:
    bonus = 8
    print("Bonus: 8%")
else:
    bonus = 0.05
    print("Bonus: 5%")

salary = float(input("Enter your salary: "))
bonus_amount = salary * bonus

print("Bonus amount = Rs.", bonus_amount)


#QN.18

score = float(input("Enter your subject score: "))

if score > 90:
    print("Congratulations! You did an excellent job!")
elif score >= 50 and score <= 90:
    print("You can improve. Keep practicing!")
else:
    print("You should consider retaking the course.")


#QN.19

age = int(input("Enter your age: "))

if age >= 18:
    degree = input("Do you have a degree? (yes/no): ")

    if degree == "yes":
        experience = float(input("Enter your years of work experience: "))

        if experience > 3:
            print("Highly Eligible.")
        elif experience >= 1:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not eligible (No degree).")
else:
    print("Not eligible (Underage).")


#QN.20

age = int(input("Enter age: "))
gender = input("Enter gender (M or F): ").upper()
days = int(input("Enter number of days: "))
if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    else :
        wage_per_day = 750
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    else :
        wage_per_day = 850
total_wages = wage_per_day * days
print(f"Wage per day: {wage_per_day}")
print(f"Total wages: {total_wages}")

#QN.21

is_valid = True
balance = 50000
correct_pin = 123
pin = int(input("Enter your PIN: "))
if pin == correct_pin:
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Invalid amount or insufficient balance.")
    elif choice == 2:
        print(f"Your current balance is: {balance}")
    elif choice == 3:
        print("Thank you for visiting.")
    else:
        print("Invalid option. Please select 1, 2, or 3.")
else:
    print("Wrong PIN. Access denied.")


#QN.22

print("Welcome to the Magic Forest")
choice1 = input("Do you want to go north or south? ").lower()
if choice1 == "south":
    print("Game Over")
elif choice1 == "north":
    choice2 = input("Do you want to cross the river or follow the path? ").lower()

    if choice2 == "cross the river":
        print("Game Over")
    elif choice2 == "follow the path":
        choice3 = input("Choose between fairy, ogre, or elf: ").lower()

        if choice3 == "ogre" or choice3 == "fairy":
            print("Game Over")
        elif choice3 == "elf":
            print("You Win")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")


#QN.23


print("Welcome to the Haunted House")

direction = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if direction == "downstairs":
    print("Game Over")

elif direction == "upstairs":
    choice1 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()

    if choice1 == "enter the room":
        print("Game Over")

    elif choice1 == "stay outside":
        creature = input("Choose one: ghost, vampire, or werewolf: ").lower()

        if creature == "ghost" or creature == "vampire":
            print("Game Over")
        elif creature == "werewolf":
            print("You Win")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

else:
    print("Invalid direction")
