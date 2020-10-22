import mysql.connector                  #incijuje pakiet bazy danych
mydb = mysql.connector.connect(         #lacze sie z baza danych
    host="localhost",
    user="root",
    password="",
    database="biuro"
    )
mycursor = mydb.cursor()                #ustawia kursor
destinations = ["eu", "am", "az", "af", "au"]                                           #Kontynenty swiata
types = ['i', 't', 'c']                                                                 #Typy wycieczek

def take_data():
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
    mycursor.execute("SELECT * FROM produkty;")     #wykonuje kwerende
    result=mycursor.fetchall()                  #zbieram wynik
    #for x in result:                        #wypisuje
       # print(x)
    return result

#queryresult=databaseOperation()

def writetofile(result):
    f=open("wynik.txt","a")
    f.write(str(result)+"\n")

def addtrip():
    continent=input("Podaj kontynent, na którym znajduje się cel: ")
    while continent not in destinations:                                             #Sprawdzam czy dobrze podal
        continent = input("Podałeś zły kontynent(eu, am, az, af, au): ")
    country=input("Podaj kraj, do którego jest ta wycieczka: ")
    city=input("Podaj miasto, do którego jest wycieczka: ")
    price=int(input("Podaj cenę wycieczki: "))
    while price<1:                                                                          #Sprawdzam czy dobrze podal
        price=input("Nie możesz mieć ujemnego budżetu: ")                                   #Daje kolejna szanse
    type=input("Podaj typ wycieczki: ")
    while type not in types:  # Sprawdzam czy dobrze podal
        type = input("T-turystyczna I-imprezowa C-chillowa. Wybierz swój typ: ")  # Daje kolejna szanse
    length=int(input("Ile dni trwa ta wycieczka: "))
    while length<1:                                                                          #Sprawdzam czy dobrze podal
        length=input("Nie może mieć mniej niż 1 dzień: ")
    sql = "INSERT INTO wycieczki (kontynent, kraj, miasto, cena, dni, typ ) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (continent, country, city, price, length,type)
    mycursor.execute(sql, val)
    mydb.commit()

#writetofile(queryresult)
addtrip()