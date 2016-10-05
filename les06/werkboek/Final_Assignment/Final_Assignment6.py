### DEEL 1 ###
def code(str):
    str.split()
    encripted=[]
    for letter in str:
        letterCode=ord(letter)
        encripted.append(chr((letterCode)+3))
    ''.join(encripted)
    print(''.join(encripted))
code('abAW ')

### DEEL 2 ###
def tabel():
    t=[['Tuple', 'JA', 'NEE', 'JA', 'JA'],
       ['Dictionary', 'NEE', 'JA', 'JA', 'NEE'],
       ['Set', 'NEE', 'JA', 'JA', 'NEE'],
       ['List', 'JA', 'JA', 'JA', 'JA']]

    print('{0:11}{1:10}{2:12}{3:10}{4:10}'.format('', 'Geordend', 'Muteerbaar', 'Iterable', 'Dubbele waarden toegestaan'))
    for list in t:
        print('{0:11}{1:10}{2:12}{3:10}{4:10}'.format(list[0], list[1], list[2], list[3], list[4]))
tabel()
