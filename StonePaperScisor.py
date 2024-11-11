from random import randint
from time import sleep
print('''[0] - Stone 
[1] - Paper 
[2] - Scisor''')
y = int(input('Pick one: '))
itens = ('Stone', 'Paper', 'Scisor')
x = randint(0, 2)
print('-=' * 11)
print('Stone')
sleep(0.5)
print('Paper')
sleep(0.5)
print('Scisor')
print('-=' * 11)
sleep(0.25)
print('You pick {} \nI pick {}'.format(itens[y], itens[x]))
print('-=' * 11)
if x == 0: #stone
    if y == 0:
        print('Draw')
    elif y == 1:
        print('you won')
    elif y == 2:
        print('I won')
    else:
        print('You wont find nothing here, buddy')
elif x == 1: #paper
    if y == 0:
        print('I won')
    elif y == 1:
        print('Draw')
    elif y == 2:
        print('You Won')
    else:
        print('You wont find nothing here, buddy')
elif x == 2: #scisor
    if y == 0:
        print('You won')
    elif y == 1:
        print('I won')
    elif y == 2:
        print('Draw')
    else:
        print('You wont find nothing here, buddy')
