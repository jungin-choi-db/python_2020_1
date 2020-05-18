luv = input("Let's say 'l love you' in another language")
love={"I love you":"English","Aishiteru":"Japanese","Wo ai ni":"Chinese","Ti amo":"Italian", "Te qiero":"Spanish","Ich liebe dich":"German"}
            
def add_another(language, contry):
    love[language]=contry
          
if luv in love:
    print(love[luv])
else:
    print("I don't know")
    ask=input("Do you want to add another language?(Yes or No)")  
    if ask=="Yes":
        language=input("Write l love you in the country you want to save")
        contry=input("Which country are you talking about?")
        add_another(language, contry)
        print(love)


