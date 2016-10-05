def annuleringen():
    infile=open('annuleringen.txt')
    lines = infile.readlines()
    annuleringen=[]

    for line in lines:
        line=line.strip()
        cx=line.split(': ')
        annuleringen.append(cx[1])
    return annuleringen
    infile.close()

def treinritten ():
    infile=open('treinrittenutrecht.txt')
    lines = infile.readlines()
    ritten=[]

    for line in lines:
        station=line.strip()
        ritten.append(station)
    return ritten
    infile.close()

def deleteCX():
    outfile=open('doorgaandeRitten.txt', 'a')
    for rit in treinritten():
        station=rit[11:]
        if station not in annuleringen():
            outfile.write(str(rit)+'\n')
        else: continue
    outfile.close()
    print('klaar')

deleteCX()
