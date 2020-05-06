def existID(ID):
    print("Perform an ID duplicate check")
    return 0

def makeID(ID, pw, name, phone):
    check = existID(ID)
    if check==0:
        print("Available ID") 
        info = {'ID':ID, 'PW':pw, 'Name':name,'PH':phone}
        return info
    else:
       print("An ID that already exists. Please enter another ID")
