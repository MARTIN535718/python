import random

helyes = 0


jel = input('Írj be egy műveletijelet: ')

while jel != '0' and helyes != 6:
    sz1 = random.randint(1,10)
    sz2 = random.randint(1,10)
    
    if helyes == 5:
        jel = input('Írj be egy új műveleti jelet vagy egy "0" hogy leállítsd a programot: ')
        helyes = 0
    
    if jel == '+':
        osszeg = sz1 + sz2
        print(sz1, '+', sz2, '=', end='')
        eredmeny = int(input(' '))
        
        if eredmeny == osszeg:
            helyes += 1
            print(helyes, '/5', sep='')
    
    if jel == '-':
        osszeg = sz1 - sz2
        print(sz1, '-', sz2, '=', end='')
        eredmeny = int(input(' '))
        
        if eredmeny == osszeg:
            helyes += 1
            print(helyes, '/5', sep='')
    
    if jel == '*':
        osszeg = sz1 * sz2
        print(sz1, '*', sz2, '=', end='')
        eredmeny = int(input(' '))
        
        if eredmeny == osszeg:
            helyes += 1
            print(helyes, '/5', sep='')
    '''
    if jel == '/':
        osszeg = sz1 / sz2
        print(sz1, '/', sz2, '=', end='')
        eredmeny = int(input(' '))
        
        if eredmeny == osszeg:
            helyes += 1
            print(helyes, '/5', sep='')
    '''
