import csv
import random
bestand = 'kluizen.csv'
kluizenLijst={}
keuze = 0

def bootUp():
    with open(bestand, 'r') as kluizenLijstCSV:
        reader=csv.reader(kluizenLijstCSV, delimiter=';')
        for row in reader:
            pincode=row[0]
            kluisnummer=row[1]
            kluizenLijst[pincode]=kluisnummer

def appendToCsv(pincode, kluisnummer):
    with open(bestand, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow((pincode, kluisnummer))
def writeOverCSV():
    with open(bestand, 'w') as kluizenLijstCSV:
        writer=csv.writer(kluizenLijstCSV, delimiter=';')
        for key, value in kluizenLijst.items():
            writer.writerow([key, value])

def randomPin():
    pin=random.randrange(1000,10000)
    return pin

def aantalKluizenVrij():
    print("\nEr zijn",(12-len(kluizenLijst)),"kluizen vrij.\n")

def nieuweKluis():
    if len(kluizenLijst) < 12:
        pincode=str(randomPin())
        kluisnummer=str(len(kluizenLijst)+1)
        kluizenLijst[pincode]=kluisnummer
        appendToCsv(pincode, kluisnummer)
        print("Kluis ", kluisnummer, "is voor u geopend. De pincode hiervan is: ", pincode,'\n')
    else:
        print('\nEr zijn helaas geen vrije kluizen meer\n')

def kluisOpenen():
    invoerPin=str(input('Wat is uw pincode? '))
    if invoerPin in kluizenLijst:
        print("Kluis nummer ",kluizenLijst[invoerPin]," is voor u geopend.\n")
    else:
        print('Pin onbekend\n')

# def kluisTeruggeven():
#     invoerPin=(input('Wat is uw pincode? '))
#     if invoerPin in kluizenLijst:
#         print("Kluis nummer ",kluizenLijst.pop(invoerPin)," is voor u vrijgegeven.\n")
#         writeOverCSV()
#     else:
#         print('Pin onbekend\n')

bootUp()

while keuze != 5:
    print("\n1: Ik wil een nieuwe kluis\n"
          "2: Ik wil mijn kluis openen\n"
          "3: Ik geef mijn kluis terug\n"
          "4: Ik wil weten hoeveel kluizen nog vrij zijn\n"
          "5: Ik wil stoppen\n",
          kluizenLijst)#zodat je kan zien welke pincode bij welke kluis hoort
    keuze=int(input('\nWat wilt u doen?'))
    if 0 > int(keuze) > 5:
        print('Geen geldige invoer. Kies een cijfer van 1 t/m 5\n')
    elif keuze == 1:
        nieuweKluis()
    elif keuze == 2:
        kluisOpenen()
    elif keuze == 3:
        #kluisTeruggeven()
        print("Functie niet beschikbaar\n")
    elif keuze == 4:
        aantalKluizenVrij()

print("Afgesloten")
