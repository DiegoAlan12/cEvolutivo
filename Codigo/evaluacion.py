def evaluation(ind):
    # Color del pozole
    char1 = []
    char1.append(ind[0])
    print(char1)

    rojo = [1]
    blanco = [0]
    if char1 == rojo:
        costo1 = 120
        sabor1 = 95
    elif char1 == blanco:
        costo1 = 120
        sabor1 = 95
    print(costo1, sabor1)

    # Lechuga
    char2 = ind[1:3]
    print(char2)

    lOrejona = [0, 0]
    lRomana = [0, 1]
    lChina = [1, 0]
    lFrancesa = [1, 1]
    if char2 == lOrejona:
        costo2 = 20
        sabor2 = 15
    elif char2 == lRomana:
        costo2 = 15
        sabor2 = 45
    elif char2 == lChina:
        costo2 = 30
        sabor2 = 15
    elif char2 == lFrancesa:
        costo2 = 35
        sabor2 = 20
    print(costo2, sabor2)

    # Oregano
    char3 = []
    char3.append(ind[3])
    print(char3)

    oreganoSi = [1]
    oreganoNo = [0]
    if char3 == oreganoSi:
        costo3 = 25
        sabor3 = 65
    elif char3 == oreganoNo:
        costo3 = 25
        sabor3 = 45
    print(costo3, sabor3)

    # Aguacate

    char4 = ind[4:7]
    print(char4)

    aHass = [0, 0, 0]
    aLHass = [0, 0, 1]
    aCriollo = [0, 1, 0]
    aFuerte = [1, 0, 0]
    aBacon = [0, 1, 1]
    aPinkerton = [1, 0, 1]
    aGwen = [1, 1, 0]
    aReed = [1, 1, 1]
    if char4 == aHass:
        costo4 = 45
        sabor4 = 20
    elif char4 == aLHass:
        costo4 = 50
        sabor4 = 10
    elif char4 == aCriollo:
        costo4 = 45
        sabor4 = 15
    elif char4 == aFuerte:
        costo4 = 35
        sabor4 = 5
    elif char4 == aBacon:
        costo4 = 50
        sabor4 = 10
    elif char4 == aPinkerton:
        costo4 = 55
        sabor4 = 15
    elif char4 == aGwen:
        costo4 = 60
        sabor4 = 15
    elif char4 == aReed:
        costo4 = 55
        sabor4 = 10
    print(costo4, sabor4)

    # Limon
    char5 = ind[7:10]
    print(char5)

    lSSemilla = [0, 0, 0]
    lVerde = [0, 0, 1]
    lAmarillo = [0, 1, 0]
    lReal = [1, 0, 0]
    lAcido = [0, 1, 1]
    lMexicano = [1, 0, 1]
    lComlima = [1, 1, 0]
    lPersa = [1, 1, 1]
    if char5 == lSSemilla:
        costo5 = 25
        sabor5 = 25
    elif char5 == lVerde:
        costo5 = 30
        sabor5 = 5
    elif char5 == lAmarillo:
        costo5 = 20
        sabor5 = 10
    elif char5 == lReal:
        costo5 = 30
        sabor5 = 5
    elif char5 == lAcido:
        costo5 = 35
        sabor5 = 10
    elif char5 == lMexicano:
        costo5 = 40
        sabor5 = 20
    elif char5 == lComlima:
        costo5 = 45
        sabor5 = 15
    elif char5 == lPersa:
        costo5 = 50
        sabor5 = 10
    print(costo5, sabor5)

    #Rabano
    char6 = []
    char6.append(ind[10])
    print(char6)

    rabanoSi = [1]
    rabanoNo = [0]
    if char6 == rabanoSi:
        costo6 = 50
        sabor6 = 55
    elif char6 == rabanoNo:
        costo6 = 50
        sabor6 = 45
    print(costo6, sabor6)

    #Carne
    char7 = ind[11:14]
    print(char7)

    costillaCer = [0,0,0]
    chambaRes = [0,0,1]
    carDesCer = [0,1,0]
    carDesRes = [1,0,0]
    manCer = [0,1,1]
    espiCer = [1,0,1]
    lomoCer = [1,1,0]
    pollo = [1,1,1]
    if char7 == costillaCer:
        costo7 = 120
        sabor7 = 20
    elif char7 == chambaRes:
        costo7 = 150
        sabor7 = 5
    elif char7 == carDesCer:
        costo7 = 115
        sabor7 = 10
    elif char7 == carDesRes:
        costo7 = 125
        sabor7 = 10
    if char7 == manCer:
        costo7 = 80
        sabor7 = 10
    elif char7 == espiCer:
        costo7 = 95
        sabor7 = 10
    elif char7 == lomoCer:
        costo7 = 100
        sabor7 = 10
    elif char7 == pollo:
        costo7 = 125
        sabor7 = 25
    print(costo7, sabor7)

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
        costo8 = 100
        sabor8 = 5
    elif char8 == sRoja:
        costo8 = 110
        sabor8 = 5
    elif char8 == sMacha:
        costo8 = 120
        sabor8 = 25
    elif char8 == sGuacamole:
        costo8 = 130
        sabor8 = 5
    elif char8 == sArbol:
        costo8 = 95
        sabor8 = 20
    elif char8 == sHabanero:
        costo8 = 150
        sabor8 = 10
    elif char8 == sPeanut:
        costo8 = 115
        sabor8 = 15
    elif char8 == sMorita:
        costo8 = 110
        sabor8 = 15
    print(costo8, sabor8)

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
        costo9 = 60
        sabor9 = 5
    elif char9 == cBlanca:
        costo9 = 40
        sabor9 = 20
    elif char9 == cAmarilla:
        costo9 = 55
        sabor9 = 5
    elif char9 == cVidalia:
        costo9 = 65
        sabor9 = 10
    elif char9 == cCalcot:
        costo9 = 50
        sabor9 = 15
    elif char9 == cCebollin:
        costo9 = 50
        sabor9 = 10
    elif char9 == cCebolleta:
        costo9 = 55
        sabor9 = 15
    elif char9 == cMorada:
        costo9 = 45
        sabor9 = 20
    print(costo9, sabor9)

    #Maiz
    char10 = []
    char10.append(ind[21])
    print(char10)
    
    mBolsa = [1]
    mPreco = [0]
    if char10 == mBolsa:
        costo10 = 45
        sabor10 = 50
    elif char10 == mPreco:
        costo10 = 45
        sabor10 = 55
    print(costo10, sabor10)

    costoTotal =(((costo1 + costo2 + costo3 + costo4 + costo5 + costo6 + costo7 + costo8 + costo9 + costo10)*70)/100)
    print("cTotal: ", costoTotal)
    saborTotal = (((sabor1 + sabor2 + sabor3 + sabor4 + sabor5 + sabor6 + sabor7 + sabor8 + sabor9 + sabor10)*30)/100)
    print("sbtotal: ",saborTotal)
    FA = costoTotal+saborTotal
    print("Valor de la FA: ",FA)
    return FA