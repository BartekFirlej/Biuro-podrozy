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

def addtrip():
    continent=input("Podaj kontynent, na którym znajduje się cel: ")                 #Pobieram kontynent
    while continent not in destinations:                                             #Sprawdzam czy dobrze podal
        continent = input("Podałeś zły kontynent(eu, am, az, af, au): ")               #Jak zle to powtarza
    country=input("Podaj kraj, do którego jest ta wycieczka: ")                     #Pobieram kraj
    city=input("Podaj miasto, do którego jest wycieczka: ")                         #Pobieram miasto
    price=int(input("Podaj cenę wycieczki: "))                                          #Pobieram cene
    while price<1:                                                                          #Sprawdzam czy dobrze podal
        price=input("Nie możesz mieć ujemnego budżetu: ")                                   #Daje kolejna szanse
    type=input("Podaj typ wycieczki: ")                                                     #Pobieram typ
    while type not in types:  # Sprawdzam czy dobrze podal                                  #Sprawdzam typ
        type = input("T-turystyczna I-imprezowa C-chillowa. Wybierz swój typ: ")  # Daje kolejna szanse
    length=int(input("Ile dni trwa ta wycieczka: "))                                    #Chce dlugosc wycieczki
    while length<1:                                                                          #Sprawdzam czy dobrze podal
        length=input("Nie może mieć mniej niż 1 dzień: ")                                   #Jak zle to powtarza
    sql = "INSERT INTO wycieczki (kontynent, kraj, miasto, cena, dni, typ ) VALUES (%s, %s, %s, %s, %s, %s)"    #Kwerenda insert
    val = (continent, country, city, price, length,type)                                                    #Wartosci do wstawienia
    mycursor.execute(sql, val)                                                                      #Wykonanie kwerendy
    mydb.commit()                                                                       #Wyslanie do bazy

def writetofile(result,info):
    file=open("oferta.txt","w")                  #otwiera plik
    file.write("Oferta spersonalizowa dla: "+info[0]+"\nWymagania klienta:\nKontynent: "+info[1]+"\t"+"Cena do: "+str(info[2])+"\tTyp wycieczki: "+info[3]+"\n")
    file.write("Kontynent\tKraj\tMiasto\tCena\tIlosc dni\tTyp\n")
    for x in result:  # wypisuje
        file.write(x[0] + "\t" + x[1] + "\t" + x[2] + "\t" + str(x[3]) + "\t" + str(x[4]) + "\t" + x[5]+"\n")
    file.close()

def searchtrip(info):
    sql="SELECT kontynent, kraj, miasto, cena, dni, typ FROM wycieczki WHERE kontynent=%s AND cena<=%s AND typ=%s" #kwerenda wybierajaca po kryteriach
    val=(info[1],info[2],info[3])                                                                                   #wartosci do porownania
    mycursor.execute(sql,val)     #wykonuje kwerende
    result=mycursor.fetchall()                  #zbieram wynik
    if len(result)==0:                          #jesli otrzymalem 0 wierszy wyniku to znaczy ze nic nie spelnia warunkow
        print("Przykro nam, "+info[0]+"\nW tym momencie nie mamy w ofercie wycieczek spełniających Twoje kryteria")
    else:   #w innym wypadku wypisuje wynik w tabelce
        print(info[0]+" znalezlismy dla Ciebie "+str(len(result))+" ofert. Zapoznaj się z nimi:\n")
        print("Kontynent\tKraj\tMiasto\tCena\tIlosc dni\tTyp")
        for x in result:                        #wypisuje
            print(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+str(x[3])+"\t"+str(x[4])+"\t"+x[5])
        writetofile(result,info)


x=int(input("Witaj w aplikacji biura podróży Bartek\n1 - Aby zapoznac sie z oferta \n2 - Aby dodac oferte wycieczki\n"))
if x==1:
    client_data=list(take_data())
    queryresult=searchtrip(client_data)
else:
    addtrip()