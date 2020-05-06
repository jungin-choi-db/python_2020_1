def CoffeeMachine(money, coffee):
    if coffee=='Americano': 
        price = 1100 
        print('Here is your Americano') 
    elif coffee=='Espresso': 
        price = 1000 
        print('Here is your Espresso')
    elif coffee=='Milk tea':
        price = 900  
        print('Here is your Milk tea') 
    change = money - price 
    return change 


change_money = CoffeeMachine(1500,'Americano') 
print("The change is", change_money,"won") 
