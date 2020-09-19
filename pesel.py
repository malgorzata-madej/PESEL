while True:

    print("""
    Program wyznacza datę urodzenia na podstawie podanego numeru PESEL.
    Wybierz, co chcesz zrobić:

    1. Wyznacz datę urodzenia
    2. Zakończ działanie programu
    
    """)

    dzialanie = input()

    if dzialanie == "1": 
        pesel = input("Podaj numer PESEL: ")
        znaki=[]

        for znak in pesel:
            znaki.append(znak)

        if znaki[2] == '8' or znaki[2] == '9':
            if znaki[2] == '8':
                znaki[2] = '0'
            elif znaki[2] == '9':
                znaki[2] = '1'
            data = znaki[4] + znaki[5] +'.'+znaki[2]+znaki[3]+'.18'+znaki[0]+znaki[1]
            print(data)
        elif znaki[2] == '0' or znaki[2] == '1':
            data = znaki[4] + znaki[5] +'.'+znaki[2]+znaki[3]+'.19'+znaki[0]+znaki[1]
            print(data)
        elif znaki[2] == '2' or znaki[2] == '3':
            if znaki[2] == '2':
                znaki[2] = '0'
            elif znaki[2] == '3':
                znaki[2] = '1'
            data = znaki[4] + znaki[5] +'.'+znaki[2]+znaki[3]+'.20'+znaki[0]+znaki[1]
            print(data)

    elif dzialanie == "2":
        break
    else:
        print("Podano niewłaściwy numer")
    



