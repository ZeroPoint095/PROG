stations=['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def vraagOmEenStation(stationVar):
    'vraagt om een station'
    station=''
    while station not in stations:
        station=input("Voer een "+stationVar+" in: ")
        if station not in stations:
            print("Station komt niet voor in lijst.")
    return station

def inlezen_beginpunt():

  #  station=''
#    while station not in stations.xml:
    beginstation=vraagOmEenStation('beginstation')



  #  begin=input('Wat is het beginstation? ')

   # while begin not in stations.xml:
   #     print('Deze trein komt niet in '+str(begin))
   #     begin=input('Wat is het beginstation? ')

    return beginstation

def inlezen_eindpunt(beginstation):

    eindstation=''
    while eindstation not in stations:
        eindstation=vraagOmEenStation('eindstation')
        isEindstationVoorBeginstation = stations.index(eindstation)<stations.index(beginstation)
        if isEindstationVoorBeginstation:
            print("Kan niet")
            eindstation=''

  #  eind=input('Wat is het eindstation? ')
   # while eind not in stations.xml:
#        print('Deze trein komt niet in '+str(eind))
 #       eind=input('Wat is het eindstation? ')
  #  while stations.xml.index(eind)<stations.xml.index(begin):
   #     print('Eindstation ligt voor beginstation.')
    #    eind=input('Wat is het eindstation? ')
    return eindstation


def omroepen_reis(begin, eind):
    rangBegin=(stations.index(begin)+1)
    rangEind=(stations.index(eind)+1)
    afstand=((rangEind-rangBegin))

    print('Het beginstation '+begin+' is het '+str(rangBegin)+'e station in het traject')
    print('Het eindstation '+eind+' is het '+str(rangEind)+'e station in het traject')
    print('De afstand bedraagt '+str(afstand)+' station(s)')
    print('De prijs van het kaartje is '+str((afstand)*5)+' euro')

    print('Jij stapt in de trein in: '+begin)
    for traject in range((stations.index(begin)+1),(stations.index(eind))):
        print('- '+stations[traject])
    print('Jij stapt uit in: '+eind)

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)
