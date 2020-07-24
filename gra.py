import pyfiglet
import time
import os
try:
    os.system("cls")
    print(pyfiglet.figlet_format("Piniądz tycon"))
    print("Wersja 1.0 BETA")
    print("Masz pomysł na funkcje? Napisz na majliproject@gmail.com !")
    print("Jeżeli chcesz mi pomóc w tworzeniu gry, zgłoś się na maila..")
    input("Naciśnij Enter")
    os.system("cls")
    coin = 0
    boost = 0
    while coin<=1000:
        
        print("-"*14 + "Aktualne statystyki" + "-"*14)
        print("Pieniądze:" +str(coin)+ "/1000")
        print("Boost:"+str(boost)+"/10")
        print("Napisz \"p\" aby zarabiać!")
        print("Napisz \"upgrade\" aby szybciej zarabiać!")
        con = input(">>>")
        if con == "p":
            if boost == 0:
                coin = coin + 10
            else:
                coin = coin*boost
                coin = coin+10
        elif con=="upgrade":
            if coin>=20:
                if boost == 10:
                    print(pyfiglet.figlet_format("JUŻ MAKS"))
                else:
                    boost = boost+1
                    coin = coin - 20
            else:
                print(pyfiglet.figlet_format("BRAK PIENIĘDZY"))
        elif con == "czysto":
            os.system("cls")
        else:
            print(pyfiglet.figlet_format("NIE ZNAM"))
            print(pyfiglet.figlet_format("POLECENIA"))
    os.system("cls")      
    print(pyfiglet.figlet_format("GRATULACJE!"))
    print("Ukończyłeś grę. Brawo!")
    time.sleep(1000000)
except KeyboardInterrupt:
    print(" ")
    print('Gra została wyłączona. Twoje wyniki zostały utracone bezpowrotnie...')
        
