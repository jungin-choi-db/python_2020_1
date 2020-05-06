#import calculator
#dictionary

import calculator

print("Enter the first number")
a=int(input())
print("Enter the second number")
b=int(input())
print("Select calculation and enter the number")
print("1. Addition, 2.Subtraction, 3.Multiplication, 4. Division")
c=input()

cal={"1":calculator.sum(a,b),"2":calculator.sub(a,b),"3":calculator.mul(a,b),"4":calculator.div(a,b)}
calc={"1":"addition","2":"substraction","3":"multiplication","4":"division"}
symbol={"1":"+","2":"-","3":"*","4":"/"}
print("You select", calc[c],".",a,symbol[c],b)
print("The answer is",cal[c])
