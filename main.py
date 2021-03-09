#part a
#Write a program containing a function to reverse a user inputted string.

s = raw_input("Enter a string to reverse: ")
s = s.lower()
print(s[::-1])

##############################################################################

#part b
#Write a program containing a function to check if a user inputted number is
#prime.

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


