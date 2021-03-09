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
