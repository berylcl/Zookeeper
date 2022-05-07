def ayo_broke(balance):

    if balance <= 500:
        return 'Ayo is broke'
    else:
       return 'ayo has small money'


print(ayo_broke(500))
print(ayo_broke(700))
print(ayo_broke(3000))