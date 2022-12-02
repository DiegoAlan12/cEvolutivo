import random
def pobIni(num):
    listaInd = []
    listaIndEva = []
    listaAll = []
    for i in range(num):
        ind = [random.randint(0, 1) for _ in range(12)]
        print(f'{ind}')
        listaInd.append(ind)
        listaIndEva.append(evaluation(ind))
        listaAll.append(ind)
        listaAll.append(evaluation(ind))
    print(listaInd)
    print(listaIndEva)
    print(listaAll)
    #print("{:.2f}".format(listaIndEva))
    return listaInd, listaIndEva, listaAll

def evaluation(ind):
    #Color del pozole
    char1 =[]
    char1.append(ind[0])
#   print(char1)

    rojo = [0]
    blanco = [1]
    if  char1 == rojo:
        peso1 = 6.4
    elif char1 == blanco:
        peso1 = 6.1

    #Lechuga Si/No
    char2 =[]
    char2.append(ind[1])
#    print(char2)

    lechugaSi = [0]
    lechugaNo = [1]
    if char2 == lechugaSi:
        peso2 = 7.3
    elif char2 == lechugaNo:
        peso2 = 5.2

    #Oregano Si/No
    char3 =[]
    char3.append(ind[2])
#    print(char3)

    oreganoSi = [0]
    oreganoNo = [1]
    if char3 == oreganoSi:
        peso3 = 8.0
    elif char3 == oreganoNo:
        peso3 = 4.5
    
    #Acuagate
    char4 = ind[3:5]

#    print(char4)
    
    aHass = [1,1]
    aLHass = [1,0]
    aCriollo = [0,1]
    aFuerte = [0,0]
    if char4 == aHass:
        peso4 = 6.3
    elif char4 == aLHass:
        peso4 = 2.0
    elif char4 == aCriollo:
        peso4 = 1.1
    elif char4 == aFuerte:
        peso4 = 3.1

    #Limon
    char5 = ind[5:7]
#    print(char5)
    
    lSSemilla = [1,1]
    lVerde = [1,0]
    lAmarillo = [0,1]
    lReal = [0,0]
    if char5 == lSSemilla:
        peso5 = 4.1
    elif char5 == lVerde:
        peso5 = 2.1
    elif char5 == lAmarillo:
        peso5 = 1.1
    elif char5 == lReal:
        peso5 = 5.2

    #Rabano Si/No
    char6 =[]
    char6.append(ind[7])
#    print(char6)

    rabanoSi = [0]
    rabanoNo = [1]
    if char6 == lechugaSi:
        peso6 = 7.5
    elif char6 == lechugaNo:
        peso6 = 5.0
    
    #Carne Puerco/Pollo
    char7 =[]
    char7.append(ind[8])
#    print(char7)

    puerco = [0]
    pollo = [1]
    if char7 == puerco:
        peso7 = 9.1
    elif char7 == pollo:
        peso7 = 3.4
    #Salsa
    char8 = ind[9:12]
    
#    print(char8)

    sVerde = [0,0,0]
    sRoja = [0,0,1]
    sMacha = [0,1,0]
    sGuacamole = [1,0,0]
    sArbol = [1,0,1]
    sHabanero = [1,1,0]
    sPeanut = [1,1,1]
    sMorita = [0,1,1]
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

    FaF = peso1 + peso2 + peso3 + peso4 + peso5 + peso6 + peso7 + peso8
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

if __name__ == "__main__":
    NG = int(input("Número de generaciónes: \n"))
    NI = int(input("Número de individuos: \n"))

    for i in range(NG):
        listaInd, listaIndEva, listaAll = pobIni(NI)
        listaX = ruleta(listaIndEva)
        print("Individuos", listaInd)
        print("Evaluados", listaIndEva)
        #print("{0:.2f}".format(listaX))
        print("Ruleta", listaX)
        print("Individuos y su evaluación: ", listaAll)

        for indice, (item1,item2) in enumerate(zip(listaX, listaIndEva)):
            
            if item1==item2:
                print(f"{item1} se encuentra en ambas listas en el índice {indice}")