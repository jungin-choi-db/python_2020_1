import matplotlib.pyplot as plt
me=[1950, 2350, 1850, 2200, 3800, 2800, 2000]
you=[1750, 2150, 2550, 2300, 2400, 1900, 1600]
x=[1,3,5,7,9,11,13]
x1=[2,4,6,8,10,12,14]
day=["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.barh(x,me,label='me', color='b')
plt.barh(x1,you,label='you', color='g')
plt.suptitle('My Kcal')
plt.yticks(x,day)
plt.xlabel('Kcal')
plt.ylabel('day')
plt.legend()
plt.show()
