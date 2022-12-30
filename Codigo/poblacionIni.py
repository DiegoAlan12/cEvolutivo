import random
import time

def pobIni(num):
    listaInd = []
    for i in range(num):
        ind = [random.randint(0, 1) for _ in range(20)]
        print(f'{ind}')
        listaInd.append(ind)
    print(listaInd)
    return listaInd
        
def evaluation(ind):
    #Color del pozole
    char1 =[]
    char1.append(ind[0])
    print(char1)

    rojo = [1]
    blanco = [0]
    if  char1 == rojo:
        peso1 = 6.4
    elif char1 == blanco:
        peso1 = 6.1
    print(peso1)

    #Lechuga Si/No
    char2 = ind[1:3]
    #char2.append(ind[1:2])
    print(char2)

    lOrejona = [0,0]
    lRomana = [0,1]
    lChina = [1,0]
    lFrancesa = [1,1]
    if char2 == lOrejona:
        peso2 = 7.3
    elif char2 == lRomana:
        peso2 = 5.2
    elif char2 == lChina:
        peso2 = 1
    elif char2 == lFrancesa:
        peso2 = 2
    print(peso2)

    #Oregano Si/No
    char3 =[]
    char3.append(ind[3])
    print(char3)

    oreganoSi = [1]
    oreganoNo = [0]
    if char3 == oreganoSi:
        peso3 = 8.0
    elif char3 == oreganoNo:
        peso3 = 4.5
    print(peso3)
    
    #Acuagate
    char4 = ind[4:7]
    #char4.append(ind[4:6])

    print(char4)
    
    aHass = [0,0,0]
    aLHass = [0,0,1]
    aCriollo = [0,1,0]
    aFuerte = [1,0,0]
    aBacon = [0,1,1]
    aPinkerton = [1,0,1]
    aGwen = [1,1,0]
    aReed = [1,1,1]
    if char4 == aHass:
        peso4 = 6.3
    elif char4 == aLHass:
        peso4 = 2.0
    elif char4 == aCriollo:
        peso4 = 1.1
    elif char4 == aFuerte:
        peso4 = 3.1
    elif char4 == aBacon:
        peso4 = 6.3
    elif char4 == aPinkerton:
        peso4 = 2.0
    elif char4 == aGwen:
        peso4 = 1.1
    elif char4 == aReed:
        peso4 = 3.1
    print(peso4)

    #Limon
    char5 = ind[7:10]
    #char5.append(ind[7:9])
    print(char5)
    
    lSSemilla = [0,0,0]
    lVerde = [0,0,1]
    lAmarillo = [0,1,0]
    lReal = [1,0,0]
    lAcido = [0,1,1]
    lMexicano = [1,0,1]
    lComlima = [1,1,0]
    lPersa = [1,1,1]
    if char5 == lSSemilla:
        peso5 = 4.1
    elif char5 == lVerde:
        peso5 = 2.1
    elif char5 == lAmarillo:
        peso5 = 1.1
    elif char5 == lReal:
        peso5 = 5.2
    elif char5 == lAcido:
        peso5 = 4.1
    elif char5 == lMexicano:
        peso5 = 2.1
    elif char5 == lComlima:
        peso5 = 1.1
    elif char5 == lPersa:
        peso5 = 5.2
    print(peso5)

    #Rabano Si/No
    char6 =[]
    char6.append(ind[10])
    print(char6)

    rabanoSi = [1]
    rabanoNo = [0]
    if char6 == rabanoSi:
        peso6 = 7.5
    elif char6 == rabanoNo:
        peso6 = 5.0
    print(peso6)
    
    #Carne Puerco/Pollo
    char7 = ind[11:14]
    #char7.append(ind[11:13])
    print(char7)

    costillaCer = [0,0,0]
    chambaRes = [0,0,1]
    carDesCer = [0,1,0]
    carDesRes = [1,0,0]
    manCer = [0,1,1]
    espiCer = [1,0,1]
    lomoCer = [1,1,0]
    cocidoCer = [1,1,1]
    if char7 == costillaCer:
        peso7 = 4.1
    elif char7 == chambaRes:
        peso7 = 2.1
    elif char7 == carDesCer:
        peso7 = 1.1
    elif char7 == carDesRes:
        peso7 = 5.2
    if char7 == manCer:
        peso7 = 4.1
    elif char7 == espiCer:
        peso7 = 2.1
    elif char7 == lomoCer:
        peso7 = 1.1
    elif char7 == cocidoCer:
        peso7 = 5.2
    print(peso7)

    #Salsa
    char8 = ind[14:17]
    
    print(char8)

    sVerde = [0,0,0]
    sRoja = [0,0,1]
    sMacha = [0,1,0]
    sGuacamole = [1,0,0]
    sArbol = [0,1,1]
    sHabanero = [1,0,1]
    sPeanut = [1,1,0]
    sMorita = [1,1,1]
    if char8 == sVerde:
        peso8 = 2.0
    elif char8 == sRoja:
        peso8 = 1.3
    elif char8 == sMacha:
        peso8 = 2.1
    elif char8 == sGuacamole:
        peso8 = 1.1
    elif char8 == sArbol:
        peso8 = 2.0
    elif char8 == sHabanero:
        peso8 = 1.0
    elif char8 == sPeanut:
        peso8 = 1.0
    elif char8 == sMorita:
        peso8 = 2.0
    print(peso8)

    #Cebolla
    
    char9 = ind[17:20]
    
    print(char9)

    cFrancesa = [0,0,0]
    cBlanca = [0,0,1]
    cAmarilla = [0,1,0]
    cVidalia = [1,0,0]
    cCalcot = [0,1,1]
    cCebollin = [1,0,1]
    cCebolleta = [1,1,0]
    cMorada = [1,1,1]
    if char9 == cFrancesa:
        peso9 = 2.0
    elif char9 == cBlanca:
        peso9 = 1.3
    elif char9 == cAmarilla:
        peso9 = 2.1
    elif char9 == cVidalia:
        peso9 = 1.1
    elif char9 == cCalcot:
        peso9 = 2.0
    elif char9 == cCebollin:
        peso9 = 1.0
    elif char9 == cCebolleta:
        peso9 = 1.0
    elif char9 == cMorada:
        peso9 = 2.0
    print(peso9)

    FaF = peso1 + peso2 + peso3 + peso4 + peso5 + peso6 + peso7 + peso8 + peso9
    """"
    if FaF >= 50:
        print("Pozole muy MUY RICO")
    elif FaF <50 :
        print("El pozole está RICO")
    elif FaF >= 43:
        print("El pozole está RICO")
    elif FaF < 43:
        print("El pozole está BIEN")
    elif FaF >= 35:
        print("El pozole está BIEN")
    elif FaF <35:
        print("El pozole está MALO")
    elif FaF >= 27:
        print("El pozole está MALO")
    """

    print("Valor del hijo: ", "{:.2f}".format(FaF))
    return FaF

def torneo(listaInd):
    newLista = []
    for i in listaInd:
        if i <= FaF:
            newLista.append(i)

    nNewLista = sorted(newLista, reverse=True)

    if len(nNewLista) >= 4:
        tresMejores = nNewLista[:4]
        return(tresMejores)
    else:
        return(nNewLista)

def cruza(individuos, numCortes):
    lista =[]
    lTemp = []

    pad1 = individuos[0]
    pad2 = individuos[1]
    for i in individuos:
        if i == 50:
            pad1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        elif i == 45:
            pad2 = [1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1]
        elif i == 35:
            pad3 = [1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0]
        elif i == 25:
            pad4 = [0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0]

    posCortes = random.randint(1,9)

    print("padre 1: ", pad1)
    print("Longitud padre1: ", len(pad1))
    print("padre 2: ", pad2)

    print("Numero de cortes: ", numCortes)
    print("Posicion de cortes", posCortes)

    for i in pad1[posCortes:]:
        lista.append(i)
        if len(lista)>numCortes-1:
            break

    for j in pad2[posCortes:]:
        lTemp.append(j)
        if len(lTemp)>numCortes-1:
            break

    print(lista)
    print(lTemp)

    parada = len(pad1) - numCortes

    for i in pad1[posCortes:]:
        pad1.pop(posCortes)
        if len(pad1) == parada:
            break

    for i in pad2[posCortes:]:
        pad2.pop(posCortes)
        if len(pad2) ==parada:
            break

    while len(lTemp)!=0:
        pad1.insert(posCortes, lTemp.pop(0))

    while len(lista)!=0:
        pad2.insert(posCortes,lista.pop(0))

    hijo1 = pad1
    hijo2 = pad2

    print("Hijo1 FA: ", evaluation(hijo1))
    print("Hijo2 FA: ", evaluation(hijo2))

    return(hijo1, hijo2)
"""
def ruleta(lista):
    listaSumas = []
    listax = []
    listaSumas.append(lista [0])
    for i in lista[1:]:
        pos = len(listaSumas)-1
        listaSumas.append(i+listaSumas[pos])
    
    pos2 = len(listaSumas)-1
    numero = listaSumas[pos2]
    a = random.randrange(0,int(numero))

    for i in listaSumas:
        if a < i:
            numero = i
        
        pos = listaSumas.index(numero)

        listax.append(lista[pos])

    return listax  
"""

if __name__ == "__main__":
    NG = int(input("Número de generaciónes: \n"))
    NI = int(input("Número de individuos: \n"))
    Ttor = int(input("Tamanio del torneo: \n"))
    nE = int(input("Individuos Elite: \n"))
    PC = int(input("Probabilidad de cruza: \n"))
    pm = int(input("Probabilidad de mutación: \n"))
    
    for i in range(NG):
        lista = pobIni(NI)
        fin = sorted(lista)
        print("Generación: ", i)

