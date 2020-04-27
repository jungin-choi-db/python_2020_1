money = int(input('How much money was inserted? '))
course1 = int(input('How many tickets for the course 1? '))
course2 = int(input('How many tickets for the course 2? '))

change = money-course1*700-course2*900
print('Change:', change,'won')

change1000 = change//1000
change = change%1000
change100 = change//100

print('1000won:',change1000,'bills')
print('100won:',change100,'coins')
