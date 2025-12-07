# # # password= 'Raam1213'
# # # if len(password)>=8:
# # #     print('valid password')
# # # else:
# # #     print('invalid password')
# # #p=P,o=o
# # password= 'i love python programming language'
# # step1=password.maketrans('po',"PO")
# # print(password.translate(step1))

# # username='raam@123'
# # step2=step1.replace("",)
# fullname='Laxman devKota'.lower()
# print(fullname)
# step1=fullname.split()
# print('_'.join(step1))

# s_password="akazaa"
# step1=s_password.maketrans('akz',"235")
# print(f'Your secret code is : {s_password.translate(step1)}0##9')

# method 1
# email= 'laxman.kc123@gmail.com'
# step1=email.split('@')[0]
# print(step1)
# print(step1.replace('.',','))

# #method 2
# email= 'laxman.kc123@gmail.com'
# step1=email[:email.find('@')]
# #step1=email[:12]
# print(step1.replace('.',","))

# user_input= 'I loVe South movieS '.title()
# step1=user_input.split()
# print(' '.join(step1[::-1]))

# def login():
#     '''this function will display'''
#     print('print python')
# login()
# print (login.__doc__)

# num1 = 12
# num2 = 13
# print(num1 // num2)

# age = 21
# age += 3
# print(age)

# list1=[1,2,3,4]
# list2=list1
# list1+=list2
# print(list1)
# print(list2)

# list1=[1,2,3,4]
# list2=list1
# list1=list1+list2
# print(list1)
# print(list2)

# num1 = 17
# num2 = 15
# # print(num1 == num2)
# # if num1==num2:
# # if num1 < num2:
# #     print("num2 is greater than num1")
# # else:
# #     print("num1 is greater than num2")\
# # if num1 != num2 and num1 % 2 == 0:
# if num1 != num2 or num1 % 2 == 0:
#     print("True")
# else:
#     print("False")

# student_name=['laxman','heera','sita']
# name=input('enter the student name: ')
# #print(name in student_name)
# if name in student_name:
#     print(f'{name} is present')
# else:
#     print('{name} not available')
#     #----------------------------
# if name not in student_name:
#     print('true')
# else:
#     print('false')

# name='ram'
# name2='shyam'
# print(id(name))
# print(id(name2))
# print(name is name2)

# num1 = 17
# num2 = 19
# print(num1 & num2)
# print(num1^num2)
# print(num1 | num2)
# print(~num1)

# year=2025
# month=11
# day=24
# print(year,month,day,sep='/')


# for i in range(5):
#     print(i,end=' ')
# connecting a different line data into one line

# data conversion
# num1=12
# num2=19.12
# result=num1+num2
# print(type(result))

# num1 = 89
# print(~num1)

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

# def login():
#     #print('hello')
#     return('hello')
#     print('good afternoon')
# print(login())

# num1=int(input('Enter a first number" '))
# num2=int(input('Enter a second number" '))
# if  num1==num2 :
#     print('both number are equal')
# # elif
# elif num1>num2:
#     print('num1 is greater')
# elif num1<num2:
#     print('num2 is greater')
# else:
#     print('not equal')

# num=int(input('Enter a number'))
# if num>0:
#     print('Number is positive')
# elif num<0:
#     print('Number is zero')
# else:
#     print('Number is negative')

# num=int(input('Enter a number'))
# if num>1 and num<100:
#     print('Number is between 1 to 100')
# else:
#     print('Number is not between 1 to 100')

# marks = int(input("Enter the students marks"))
# if marks > 100 or marks < 0:
#     print("Invalid Marks")
# elif marks >= 90 and marks <= 100:
#     print("A+")
# elif marks >= 80 and marks <= 89:
#     print("A")
# elif marks >= 70 and marks <= 79:
#     print("B+")
# elif marks >= 60 and marks <= 69:
#     print("B")
# elif marks >= 50 and marks <= 59:
#     print("C")
# elif marks >= 40 and marks < 49:
#     print("D")
# else:
#     print("E")

# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# operator = input("Enter the operator")
# if operator not in ("+","-","/","*"):
#     print("Invalid operator")
# elif operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)

# a=int(input('Enter first number '))
# b=int(input('Enter second number '))
# c=int(input('Enter third number'))
# if a==b==c :
#     print('All number are equal')
# elif a==b or b==c or a==c :
#     print('Two numbers are equal')
# else :
#     print('All number are different')

# a=int(input('Enter a number: '))
# if a%3==0 and a%5==0 :
#     print('Fizz Buzz')
# elif a%3==0 and a%5!=0 :
#     print('Fizz')
# elif a%3!=0 and a%5==0 :
#     print('Buzz')
# else :
#     print(a)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# # Compare the numbers
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     # Numbers are equal, check the sign
#     if a > 0:
#         print("The numbers are equal and positive")
#     elif a < 0:
#         print("The numbers are equal and negative")
#     else:
#         print("The numbers are equal and zero")

# a=int(input('Enter first number : '))
# b=int(input('Enter second number: '))
# c=int(input('Enter third number: '))
# if a>b & a>c :
#     print('The largest number is : {a}')
# elif b>a & b>c :
#     print('The largest number is : {b}')
# elif c>a & c>b:
#     print('The largest number is : {c}')
# else :
#     print('All numbers are equal')

# import random
# import random as rd
# from random import *
# result=randint(1,12)
# month=('jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec')
# print(month[result])

# num1=int(input('Enter first number : '))
# num2=int(input('Enter second number : '))
# num1,num2=num2,num1
# print(num1,num2)

# age = int(input("Enter your age: "))
# if age < 12:
#     price = 'free'
# else:
#     if age >= 12 and age<= 60 :
#         membership = input("Do you have a membership card? (yes/no): ")
#         if membership == "yes":
#             price = 150
#         else:
#             price = 200
#     else:
#         price = 100
# print(f"The ticket price is {price}")

# unit = float(input("Enter the electricity usage in units : "))

# if unit < 100:
#     bill = unit * 5
# elif unit <= 300:
#     bill = (100 * 5) + ((unit - 100) * 8)
# else:
#     bill = (100 * 5) + (200 * 8) + ((unit - 300) * 10)

# print(f"The total electricity bill is Rs. {bill}")

# a = int(input("Enter the number of students in class A: "))
# b = int(input("Enter the number of students in class B: "))
# c = int(input("Enter the number of students in class C: "))
# desks_a = (a + 1) // 2
# desks_b = (b + 1) // 2
# desks_c = (c + 1) // 2
# total_desks = desks_a + desks_b + desks_c
# print(f"The smallest possible number of desks that can be purchased is: {total_desks}")

# current_floor = 5
# requested_floor = 3
# if requested_floor > current_floor:
#     direction = "up"
# elif requested_floor < current_floor:
#     direction = "down"
# else:
#     direction = "stay at the current floor"
# print(f"The lift should go {direction}.")

# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 0:
#         print(f"{num} is positive and even.")
#     else:
#         print(f"{num} is positive and odd.")
# else:
#     print(f"{num} is not positive.")

# mark1 = int(input("Enter marks for subject 1: "))
# mark2 = int(input("Enter marks for subject 2: "))
# mark3 = int(input("Enter marks for subject 3: "))
# mark4 = int(input("Enter marks for subject 4: "))
# # Calculate total marks
# total_marks = mark1 + mark2 + mark3 + mark4
# # Calculate percentage (assuming each subject is out of 100, total out of 400)
# percentage = (total_marks / 400) * 100
# # Determine grade based on percentage
# if percentage > 70:
#     grade = "Distinction"
# elif percentage > 60:
#     grade = "First"
# elif percentage > 40:
#     grade = "Pass"
# else:
#     grade = "Fail"
# # Display the results
# print(f"Total Marks: {total_marks}")
# print(f"Percentage: {percentage:.2f}%")
# print(f"Grade: {grade}")

# #list
# items=[1,2,3,4]
# #items.append([3,4])
# #items.insert(0,'ram')
# items[0]='ram'#type: ignore

# items=[1,2,[3,4]]
# items.remove(2)
# print((items))

# items=[1,2,[3,4]]
# items.pop() # type: ignore
# print((items))

# items = [1, 2, [3, 4]]
# num1 = items
# items += num1
# items = items + num1
# items = [1, 2, [3, 4]]
# print((items))
# print(num1)

# items=1,2,3,4
# items='ram',+1,2,3,4
# list=list(items)
# list.insert(1,list.pop(2))
# print(tuple(list))

# items=(1,2,3,3,3,3,4,5,5,6,7,8,8)
# result=items.count(3)
# print(result)

# set data structures

# items={1,2,3,4}
# items.discard(8)
# print(items)

# items = {"shyam", 1, "ram", 2, 3, 4}
# items = {"shyam", 1,4, "ram"}
# # items2 = {2, 3, 4}
# items2 = {4}
# # items.clear()
# # result = items.intersection(items2)
# # result = items.difference(items2)
# #result=items2.isdisjoint(items)
# result=items.isdisjoint(items2)
# print(result)

# Program to calculate employee bonus based on years of service

# years = int(input("Enter years of service: "))

# if years > 10:
#     bonus = 0.10
#     print("Bonus: 10%")
# elif years >= 6 and years <= 10:
#     bonus = 0.08
#     print("Bonus: 8%")
# else:
#     bonus = 0.05
#     print("Bonus: 5%")

# salary = float(input("Enter your salary: "))
# bonus_amount = salary * bonus

# print("Bonus amount = Rs.", bonus_amount)

# age = int(input("Enter your age: "))

# if age >= 18:
#     degree = input("Do you have a degree? (yes/no): ")

#     if degree == "yes":
#         experience = float(input("Enter your years of work experience: "))

#         if experience > 3:
#             print("Highly Eligible.")
#         elif experience >= 1:
#             print("Eligible.")
#         else:
#             print("Under Review.")
#     else:
#         print("Not eligible (No degree).")
# else:
#     print("Not eligible (Underage).")

# age = int(input("Enter age: "))
# gender = input("Enter gender (M or F): ").upper()
# days = int(input("Enter number of days: "))
# if 18 <= age < 30:
#     if gender == 'M':
#         wage_per_day = 700
#     elif gender == 'F':
#         wage_per_day = 750
#     else:
#         wage_per_day = 'invalid gender'
# elif 30 <= age <= 40:
#     if gender == 'M':
#         wage_per_day = 800
#     elif gender == 'F':
#         wage_per_day = 850
#     else:
#         wage_per_day = 'invalid gender'
# else:
#     wage_per_day = 0
# total_wages = wage_per_day * days
# print(f"Wage per day: {wage_per_day}")
# print(f"Total wages: {total_wages}")

# age = int(input("Enter age: "))
# gender = input("Enter gender (M or F): ").upper()
# days = int(input("Enter number of days: "))
# if 18 <= age < 30:
#     if gender == 'M':
#         wage_per_day = 700
#     elif gender == 'F':
#         wage_per_day = 750
#     else:
#         'invalid gender'
# elif 30 <= age <= 40:
#     if gender == 'M':
#         wage_per_day = 800
#     elif gender == 'F':
#         wage_per_day = 850
#     else:
#         'invalid gender'
# else:
#     wage_per_day = 0
# total_wages = wage_per_day * days
# print(f"Wage per day: {wage_per_day}")
# print(f"Total wages: {total_wages}")

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


