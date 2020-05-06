def CoffeeMachine(money, coffee):
    item={"Americano":1100,"Espresso":1000,"Milk Tea":900}
    print('Here is your'+coffee)
    change = money - item[coffee]
    return change

change_money = CoffeeMachine(1500,'Americano')
print(change_money)
