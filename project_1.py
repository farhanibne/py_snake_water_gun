#snake-water-gun


import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you =='g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you =='s':
            return False
        elif you == 'w':
            return True        

# print("comp one turn: snake(s) water(w) or gun(g)??")
randno = random.randint(1,3)
# print(randno)

if randno == 1 :
    comp =  's'
elif randno == 2 :
    comp =  'w'
elif randno == 3 :
    comp =  'g'    


you = input("your two turn: snake(s) water(w) or gun(g)??")



a = gameWin(comp, you)


print(f"you choose {you}")
print(f"computer choose {comp}")


if a== None:
    print("this is a tie")
elif a:
    print("you win!!!")
else:
    print("you lose!!")        

