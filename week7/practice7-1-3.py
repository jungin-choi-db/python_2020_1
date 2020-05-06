#import calculator
#if statement

import calculator

print("Enter the first number")
a=int(input())
print("Enter the second number")
b=int(input())
print("Select calculation and enter the number")
print("1. Addition, 2.Subtraction, 3.Multiplication, 4. Division")
c=input()

if c=='1':
    print("You select addition. ",a,"+",b)
    print("The answer is",calculator.sum(a,b))
elif c=='2':
    print("You select subtraction. ",a,"-",b)
    print("The answer is",calculator.sub(a,b))
elif c=='3':
    print("You select multiplcation. ",a,"*",b)
    print("The answer is",calculator.mul(a,b))
elif c=='4':
    print("You select division. ",a,"/",b)
    print("The answer is",calculator.div(a,b))
else:
    print("You enter the wrong number")
