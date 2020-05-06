def CoffeeMachine(money, coffee): #define CoffeeMachine function. money and coffee is parameters of CoffeeMachine function.
    if coffee=='Americano': #if statement. if condition is coffee parameter's value is Americano or not.
        price = 1100 #if condition is true, then price value is 1100.
        print('Here is your Americano') #print function.
    elif coffee=='Espresso': #if condition is false, next condition is coffee parameter's value is Espresso or not.
        price = 1000 #elif condition is true, then price value is 1000.
        print('Here is your Espresso') #print function.
    elif coffee=='Milk tea':#Thrid condition is coffee parameter's value is Milk tea or not.
        price = 900  #elif condition is true, then price value is 900.
        print('Here is your Milk tea') #print function.
    change = money - price #change variable's value is money-price. money is a parameter.
    return change #The return value of CoffeeMachine function is change value.


change_money = CoffeeMachine(1500,'Americano') #fucntion call. change_money value is the return value of coffeemachine function.
print("The change is", change_money,"won") #print function. print change_money value.
