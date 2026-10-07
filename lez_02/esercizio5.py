def inserisci_punto():
    '''
    inserisci un punto nel piano cartesiano
    '''
    x = int(input("Inserisci la coordinata x: "))
    y = int(input("Inserisci la coordinata y: "))
    return (x, y)

def inserisci_rettangolo():
    '''
    inserisci un rettangolo nel piano cartesiano
    come 2 punti
    '''
    x1,y1 = inserisci_punto()
    x2,y2 = inserisci_punto()
    return  [x1,y1,x2,y2]   


def posizione_relativa(xA,yA,xB,yB, 
                       xC,yC,xD,yD):
    '''
    dati 2 rettangoli nel piano cartesiano:
    R1 = (xA,yA) (xB,yB)
    R2 = (xC,yC) (xD,yD)
    determina la loro posizione relativa
    - disgiunti
    - sovrapposti
    - coincidenti
    '''
    if xA == xC and yA == yC and xB == xD and yB == yD:
        return "coincidenti"
    elif xB < xC or xD < xA or yB < yC or yD < yA:
        return "disgiunti"
    else:
        return "sovrapposti"

xA,yA,xB,yB = inserisci_rettangolo()
xC,yC,xD,yD = inserisci_rettangolo()
posizione = posizione_relativa(xA,yA,xB,yB, xC,yC,xD,yD)
print("I rettangoli sono:", posizione)