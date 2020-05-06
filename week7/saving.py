def existID(ID):
    print("Perform an ID duplicate check")
    return 1
def save_money(name, how_much):
    print('Please choose the type of payment methods')
    type = input()
    if type=='card':
        print('Pay by card')
    else:
        print('Pay by cash')
    print(name+' mileage has been charged to', how_much+'won.')
def start():
    print('Please enter the ID')
    user=input()
    if existID(user)==1:
        print(user+' is the existing ID')
        print("Enter the amount you'd like to charge")
        money=input()
        save_money(user, money)
    else:
        print('End charging.')
