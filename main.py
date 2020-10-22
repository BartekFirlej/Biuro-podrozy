def take_data():
    destinations = ["eu", "am", "az", "af", "au"]                                           #Kontynenty swiata
    types = ['i', 't', 'c']                                                                 #Typy wycieczek
    name=input("Dzień dobry. Witamy w programie biura podróży 'Bartek'. \nPodaj nam swoje imie: ") #Pobieram imie
    destination=input("Wybierz interesujący Cię kontynent podając dwie pierwsze litery: ")  #Pobieram kontynent
    while destination not in destinations:                                                  #Sprawdzam czy dobrze podal
        destination = input("Podałeś zły kontynent(eu, am, az, af, au): ")                  #Daje druga szanse w petli
    price=int(input("Podaj nam swój budżet: "))                                                  #Pobieram cene
    while price<1:                                                                          #Sprawdzam czy dobrze podal
        price=input("Nie możesz mieć ujemnego budżetu: ")                                   #Daje kolejna szanse
    type=input("W swojej ofercie mamy 3 typy wycieczek: t-turystyczna i-imprezowa c-chillowa. Wybierz swój typ: ")  #Pobieram typ
    while type not in types:                                                                #Sprawdzam czy dobrze podal
        type = input("T-turystyczna I-imprezowa C-chillowa. Wybierz swój typ: ")            #Daje kolejna szanse
    return name,destination,price,type                                                      #Zwracam wszystkie wartosci



#client_data=list(take_data())

def databaseOperation():
    import mysql.connector                  #incijuje pakiet bazy danych
    mydb = mysql.connector.connect(         #lacze sie z baza danych
        host="localhost",
        user="root",
        password="",
        database="bartek"
    )
    mycursor = mydb.cursor()                #ustawiam kursor
    mycursor.execute("SELECT * FROM produkty;")     #wykonuje kwerende
    result=mycursor.fetchall()                  #zbieram wynik
    for x in result:                        #wypisuje
       # print(x)
    return result

databaseOperation()

#def writetofile():

