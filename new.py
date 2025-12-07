# password='Ram@123'
# result=password.isupper()
# print(result)

# password='ram@123'
# flag=False
# for i in password:
#     if i.isdecimal():
#         flag=True
#         break
# print(flag)
# import string
# #import string a st
# #from string import *
# #from string import punctuation
# print(string.punctuation)

# user_input=input('Enter a sentence: ')
# print(user_input)
# step1=user_input[0]
# print(step1)
# step2=user_input[-1]
# print(step2)
# step3=len(user_input)-2
# print(step3)
# step4=(''.join([step1,step4,step2]))
# result=user_input[0]+'*'*step3+step2
# print(result)

# user_input='+977 980-0002-052'.replace('-','').replace(' ','')
# print('*'*35)
# step1=user_input[:4]
# print(step1)
# step2=user_input[-4:]
# print(step2)
# step3=len(user_input)-8
# print(step3)
# step4='*'*step3
# print(''.join([step1,step4,step3]))
# result=user_input[0]+'*'*step3+step2
# print(result)
# print('*'*35)


letters='aeiou'
s1=letters.replace('a','✈️').replace('e','😎').replace('i','🍦').replace('o','🍎').replace('u','☂')
print(s1)
