menu = {}

def stworz_menu():
    for x in range(6):
        data = input('Wprowadz danie oraz cene: ')
        try:
            price = int(data.split()[-1])
            meal = data.rsplit(maxsplit=1)[0]
            menu[meal] = price
        except ValueError:
            print('Podana cena nie jest liczba')
            return

def wyswietl_szukane():
    min_price = int(input('Wprowadz minimalna cene: '))
    max_price = int(input('Wprowadz maksymalna cene: '))
    print(sorted([x for x in menu.values() if x > min_price and x < max_price]))

stworz_menu()
wyswietl_szukane()
