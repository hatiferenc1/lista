'''Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!'''
nevek  = []
név = None
while név !='':
    név = input('Adj meg egy nevet ')
    if név !='':
        nevek.append(név)
print(nevek)