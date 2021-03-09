# Miguel Jacuinde
# CSE 5408 Spring 2021
# Lab 4 : Github - Advanced
# Group: APP-itizer Enthusiasts
# part a
# Write a program containing a function to reverse a user inputted string.

s = raw_input("Enter a string to reverse: ")
s = s.lower()
print(s[::-1])

##############################################################################

# part b
# Write a program containing a function to check if a user inputted number is
# prime.

def prime(num):
        if num > 1:
                for i in range (2, num//2):
                        if (num % i) == 0:
                                print(num, 'is not a prime number.')
                                break
                else:
                        print(num, 'is a prime number.')
        else:
                print(num, 'is not a prime number.')

num = int(raw_input('Enter a number to check if it is prime: '))
prime(num)

###############################################################################

# Cynthia Milan
# CSE 5408 Spring 2021
# Lab 4 : Github - Advanced
# Part d : Password Stregth Check
# Group: APP-itizer Enthusiasts

import re

x = raw_input("Please input Password: ")
print()
print("''",x,"''")
print()
num_sym = 0
num = 0
sym = 0
alphabet = 0

while x:
  list_of_password = list(x)
  for i in range(len(x)):
    if (list_of_password[i].isdigit()):
      num += 1
    elif (list_of_password[i].isupper()):
      alphabet += 1
    elif (list_of_password[i].islower()):
      alphabet += 1
    else:
      sym += 1

  num_sym = sym + num

  if (num_sym>1 and alphabet >1 and len(list_of_password) >6):
    print("Password is Strong")
    break
  else:
    print("Bad Password...Please Try again...")
    print()
    x = raw_input("Please input Password: ")
###################################################################################

#Brian Ayala
#APP-itizer Enthuasiasts
#CSE 5408 Spring 2021
#Lab 4 part d

i = int(input("Enter a number to output the fibonacci sum: "))

def fib(i):
    num1 = 0
    num2 = 1
    sum = 0
    if(i >= 1):
        sum = 1
        num3 = 1
        while(num3 <= i):
            num3 = num2 + num1
            sum += num3
            num1 = num2
            num2 = num3
    return sum

print(fib(i))
#######################################################################

# Citlaly Garcia
# CSE 5408 Spring 2021
# Lab 4: GitHub - Advanced
# Part c: Time Conversion
# Group: APP-itizer Enthusiasts

from datetime import datetime
import pytz

tz_CA = pytz.timezone('America/Los_Angeles')
datetime_CA = datetime.now(tz_CA)
t = datetime_CA.strftime("%H:%M:%S")
print("The current time in 24-Hour/Military time is ")

print(t)
