import xmltodict

with open('stations.xml') as xmlfile:
    stations=xmltodict.parse(xmlfile.read(),dict_constructor=dict)

def codeAndType():
    print('Dit zijn de codes en types van de 4 stations:')
    for details in stations['Stations']['Station']:
        print(details['Code'],' - ', details['Type'])
    print('')

def synonyms():
    print('Dit zijn alle stations met een of meer synoniemen:')
    for details in stations['Stations']['Station']:
        if details['Synoniemen'] != None:
            print(details['Code'],' - ', details['Synoniemen']['Synoniem'])
    print('')

def fullName():
    print('Dit is de lange naam van elk station:')
    for details in stations['Stations']['Station']:
        print(details['Code'], ' - ', details['Namen']['Lang'])
    print('')

codeAndType()
synonyms()
fullName()
