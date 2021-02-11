'''Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki.'''

nevek  = []
név = None
while név !='':
    név = input('Adj meg egy nevet ')
    if név !='':
        nevek.append(név)
    if len(nevek) == 3:
        print('Nincs több lehetőség')
        break    
print(nevek) 