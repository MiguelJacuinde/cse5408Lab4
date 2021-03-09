# Cynthia Milan
# CSE 5408 Spring 2021
# Lab 4 : Github - Advanced
# Part e : Password Stregth Check 
# Group: APP-itizer Enthusiasts

import re

x = input("Please input Password: ")
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
    x = input("Please input Password: ")



