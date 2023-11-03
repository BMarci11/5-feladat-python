'''
for paros_szamok in range(2,12,2):
    print(paros_szamok,end=' ')
'''

'''
for i in range(10,0,-1):
    print(i,end=' ')
'''

'''
for a in range(9,0,-2):
    print(a,end=' ')
'''

'''
a = input("Írj be egy szöveget: ")
b = int(input("Írd le, hogy hányszor írjam le: "))
for b in range(b):
    print(a)
'''
'''
while True:
    szam = int(input("Kérlek adj meg egy páros számot: "))
    if szam % 2 == 0:
        print("A megadott szám páros.")
        break
    else:
        print("Adj egy számot megint.")
'''

import random

random_szamok = [num for num in [random.randint(1, 12) for _ in range(20)] if num % 3 == 0]

print("Az eredeti véletlenszámok:", random_szamok)

print("A 3-mal osztható számok darabszáma:", len(random_szamok))
