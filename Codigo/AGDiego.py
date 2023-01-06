#Importamos todas las librerias necesarias
import random
import pandas as pd
import matplotlib.pyplot as plt
from csv import writer

#Esta es la generación inicial con un tamaño de 20 individuos
def pobIni():
    tam = 20
    listaInd = []
    listaIndEva = []
    #Se genera cada individuo con cada una de sus posiciones, en total son 21 posiciones
    for i in range(tam):
        ind = [random.randint(0, 1) for _ in range(21)]
        #print(f'{ind}')
        #Cada individuo se almacena en una lista de individuos
        listaInd.append(ind)
        #Para después evaluar cada uno y que tome su función de aptitud
        listaIndEva.append(evaluation(ind))
    return listaInd, listaIndEva

def evaluation(ind):
    #Se pasa cada individuo y se evalua por las posiciones del individuo

    #Característica 1: Color del pozole
    char1 = []
    char1.append(ind[0])
    # print(char1)

    rojo = [1]
    blanco = [0]
    if char1 == rojo:
        costo1 = 120
        sabor1 = 5.5
    elif char1 == blanco:
        costo1 = 100
        sabor1 = 4.5
    #print(costo1, sabor1)

    #Característica 2: Lechuga
    char2 = ind[1:3]
    # print(char2)

    lOrejona = [0, 0]
    lRomana = [0, 1]
    lChina = [1, 0]
    lFrancesa = [1, 1]
    if char2 == lOrejona:
        costo2 = 20
        sabor2 = 1.5
    elif char2 == lRomana:
        costo2 = 15
        sabor2 = 4.5
    elif char2 == lChina:
        costo2 = 30
        sabor2 = 1.5
    elif char2 == lFrancesa:
        costo2 = 35
        sabor2 = 2.0
    #print(costo2, sabor2)

    #Característica 3: Oregano
    char3 = []
    char3.append(ind[3])
    # print(char3)

    oreganoSi = [1]
    oreganoNo = [0]
    if char3 == oreganoSi:
        costo3 = 25
        sabor3 = 6.5
    elif char3 == oreganoNo:
        costo3 = 25
        sabor3 = 4.5
    #print(costo3, sabor3)

    #Característica 4: Aguacate

    char4 = ind[4:7]
    # print(char4)

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
        sabor4 = 2.0
    elif char4 == aLHass:
        costo4 = 50
        sabor4 = 1.0
    elif char4 == aCriollo:
        costo4 = 45
        sabor4 = 1.5
    elif char4 == aFuerte:
        costo4 = 35
        sabor4 = 0.5
    elif char4 == aBacon:
        costo4 = 50
        sabor4 = 1.0
    elif char4 == aPinkerton:
        costo4 = 55
        sabor4 = 1.5
    elif char4 == aGwen:
        costo4 = 60
        sabor4 = 1.5
    elif char4 == aReed:
        costo4 = 55
        sabor4 = 1.0
   # print(costo4, sabor4)

    #Característica 5: Limón
    char5 = ind[7:10]
    # print(char5)

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
        sabor5 = 2.5
    elif char5 == lVerde:
        costo5 = 30
        sabor5 = 0.5
    elif char5 == lAmarillo:
        costo5 = 20
        sabor5 = 1.0
    elif char5 == lReal:
        costo5 = 30
        sabor5 = 0.5
    elif char5 == lAcido:
        costo5 = 35
        sabor5 = 1.0
    elif char5 == lMexicano:
        costo5 = 40
        sabor5 = 2.0
    elif char5 == lComlima:
        costo5 = 45
        sabor5 = 1.5
    elif char5 == lPersa:
        costo5 = 50
        sabor5 = 1.0
    #print(costo5, sabor5)

    #Característica 6: Rabano
    char6 = []
    char6.append(ind[10])
    # print(char6)

    rabanoSi = [1]
    rabanoNo = [0]
    if char6 == rabanoSi:
        costo6 = 50
        sabor6 = 5.5
    elif char6 == rabanoNo:
        costo6 = 50
        sabor6 = 4.5
    #print(costo6, sabor6)

    #Característica 7: Carne
    char7 = ind[11:14]
    # print(char7)

    costillaCer = [0, 0, 0]
    chambaRes = [0, 0, 1]
    carDesCer = [0, 1, 0]
    carDesRes = [1, 0, 0]
    manCer = [0, 1, 1]
    espiCer = [1, 0, 1]
    lomoCer = [1, 1, 0]
    pollo = [1, 1, 1]
    if char7 == costillaCer:
        costo7 = 120
        sabor7 = 2.0
    elif char7 == chambaRes:
        costo7 = 150
        sabor7 = 0.5
    elif char7 == carDesCer:
        costo7 = 115
        sabor7 = 1.0
    elif char7 == carDesRes:
        costo7 = 125
        sabor7 = 1.0
    if char7 == manCer:
        costo7 = 80
        sabor7 = 1.0
    elif char7 == espiCer:
        costo7 = 95
        sabor7 = 1.0
    elif char7 == lomoCer:
        costo7 = 100
        sabor7 = 1.0
    elif char7 == pollo:
        costo7 = 125
        sabor7 = 2.5
    #print(costo7, sabor7)

    #Característica 8: Salsa
    char8 = ind[14:17]
    # print(char8)

    sVerde = [0, 0, 0]
    sRoja = [0, 0, 1]
    sMacha = [0, 1, 0]
    sGuacamole = [1, 0, 0]
    sArbol = [0, 1, 1]
    sHabanero = [1, 0, 1]
    sPeanut = [1, 1, 0]
    sMorita = [1, 1, 1]
    if char8 == sVerde:
        costo8 = 100
        sabor8 = 0.5
    elif char8 == sRoja:
        costo8 = 110
        sabor8 = 0.5
    elif char8 == sMacha:
        costo8 = 120
        sabor8 = 2.5
    elif char8 == sGuacamole:
        costo8 = 130
        sabor8 = 0.5
    elif char8 == sArbol:
        costo8 = 95
        sabor8 = 2.0
    elif char8 == sHabanero:
        costo8 = 150
        sabor8 = 1.0
    elif char8 == sPeanut:
        costo8 = 115
        sabor8 = 1.5
    elif char8 == sMorita:
        costo8 = 110
        sabor8 = 1.5
    #print(costo8, sabor8)

    #Característica 9: Cebolla
    char9 = ind[17:20]
    # print(char9)

    cFrancesa = [0, 0, 0]
    cBlanca = [0, 0, 1]
    cAmarilla = [0, 1, 0]
    cVidalia = [1, 0, 0]
    cCalcot = [0, 1, 1]
    cCebollin = [1, 0, 1]
    cCebolleta = [1, 1, 0]
    cMorada = [1, 1, 1]
    if char9 == cFrancesa:
        costo9 = 60
        sabor9 = 0.5
    elif char9 == cBlanca:
        costo9 = 40
        sabor9 = 2.0
    elif char9 == cAmarilla:
        costo9 = 55
        sabor9 = 0.5
    elif char9 == cVidalia:
        costo9 = 65
        sabor9 = 1.0
    elif char9 == cCalcot:
        costo9 = 50
        sabor9 = 1.5
    elif char9 == cCebollin:
        costo9 = 50
        sabor9 = 1.0
    elif char9 == cCebolleta:
        costo9 = 55
        sabor9 = 1.5
    elif char9 == cMorada:
        costo9 = 45
        sabor9 = 2.0
   # print(costo9, sabor9)

    #Característica 10: Maiz
    char10 = []
    char10.append(ind[20])
    

    mBolsa = [1]
    mPreco = [0]
    if char10 == mBolsa:
        costo10 = 55
        sabor10 = 4.5
    elif char10 == mPreco:
        costo10 = 45
        sabor10 = 5.5
    #print(costo10, sabor10)

    #Dependiendo el costo total del pozole, se le asignará un valor entre 10 a 100
    #Para determinar que tan caro o barato es el pozole
    preCosto = costo1 + costo2 + costo3 + costo4 + costo5 + costo6 + costo7 + costo8 + costo9 + costo10
    #print("Costo pre: ", preCosto)
    costoVal = 0
    if preCosto in range(550,571):
        costoVal = 10
    elif preCosto in range(571, 591):
        costoVal = 15
    elif preCosto in range(591, 611):
        costoVal = 20
    elif preCosto in range(611, 631):
        costoVal = 25
    elif preCosto in range(631, 651):
        costoVal = 30
    elif preCosto in range(651, 671):
        costoVal = 35
    elif preCosto in range(671, 691):
        costoVal = 40
    elif preCosto in range(691, 721):
        costoVal = 60
    elif preCosto in range(721, 741):
        costoVal = 80
    elif preCosto in range(741, 761):
        costoVal = 100
    
    #Se realiza una regla de 3, ya que le asignamos un peso del 30% al costo en un 100% al MEJOR POZOLE
    costoTotal = (((costoVal)*30)/100)
    #De igual manera para un MEJOR POZOLE, se le da un peso de 70% dentro de 100% al sabor del pozole
    saborTotal = (((sabor1 + sabor2 + sabor3 + sabor4 + sabor5 + sabor6 + sabor7 + sabor8 + sabor9 + sabor10)*70)/100)
    #Y al realizar la suma, nos da un total de la función de aptitud, que mientras más alta sea, mejor será el pozole
    FA = costoTotal+saborTotal
    return FA

def opeTorneo(listaIndEva, listaInd):
    #Se reciben 20 individuos
    generacion = []
    indices = []
    cont = 0
    while(cont<10):
        #Seleccionamos al azar 2 individuos
        indk1 = random.randrange(0,20)
        indk2 = random.randrange(0,20)
        #Encontramos los valores de aptitud de cada individuo
        valk1 = float(listaIndEva[indk1])
        valk2 = float(listaIndEva[indk2])
        #si el individuo es mayor o igual al individuo 2, el individuo 1 es elegido
        if valk1 >= valk2:
            if not(indk1 in indices):
                #Se agrega el individuo
                indices.append(indk1)
                generacion.append(listaInd[indk1])
                cont = cont+1
        #Si el individuo 2 es mayor que el 1, se selecciona
        elif(valk2>valk1):
            #Se comprueba que el individuo no haya sido agregado ya
            if not (indk1 in indices):
                #Se agrega el individuo
                indices.append(indk2)
                generacion.append(listaInd[indk2])
                cont = cont+1
    #Se devuelven 10 individuos, ya que solo se selecciona la mitad de poblacion
    return generacion

def opeCruza(listaIndEva, listaInd):
    #Se reciben 20 individuos debido a la reducción de estos en la selección
    indP2 = 1
    H1 = []
    H2 = []
    nuevaGen = []
    for indP1 in range(10):
        #Se selecciona el Padre 1 y el Padre 2
        P1 = listaInd[indP1][0:21]
        P2 = listaInd[indP2][0:21]
        for r in range(len(P1)):
            #La probabilidad de cruza es del 50% para cada uno
            #Por lo tanto se hacce al azar entre el 1 y 2
            azar = random.randrange(1,3)
            #Si sale 1 se elige un elemento del Padre 1 para el Hijo 1 y el Hijo 2 recibe el elemento del Padre 2
            if(azar==1):
                H1.append(P1[r])
                H2.append(P2[r])
            #Si sale 2 se elige un elemento del Padre 2 para el Hijo 1 y el Hijo 2 recibe el elemento del Padre 1
            elif(azar==2):
                H1.append(P2[r])
                H2.append(P1[r])
        #Se guardan los valores del Hijo 1
        nuevaGen.append(H1)
        #Se guardan los valores del Hijo 2
        nuevaGen.append(H2)
        H1 = []
        H2 = []
        indP2 = indP2+1
        if(indP2==10):
            indP2=0
    return nuevaGen

def opeMutacion(cruza):
    muta = []
    mutado = []
    for ind in cruza:
        mutado = []
        for j in range(len(ind)):
            #Se genera una tasa de mutación de manera aleatoria
            tasaMuta = random.random()
            gen = ind[j]
            #Comparamos la tasa de mutación con el % de mutación
            if(tasaMuta<.03):
                #Muta 
                if(gen==1):
                    mutado.append(0)
                else:
                    mutado.append(1)
            else:
                #no muto
                mutado.append(gen)
        muta.append(mutado)
    return muta

#Se hace el cálculo entre cada generación del individuo promedio                
def genePromedio(listaIndEva):
    prom = sum(listaIndEva)/len(listaIndEva)
    return prom

#Se hace la evaluación entre el mejor y el peor individuo de cada generación
def evaluar(listaIndEva, listaInd):
    individuoSelect = []
    individuo = []
    minValue = min(listaIndEva)
    maxValue = max(listaIndEva)
    indice = listaIndEva.index(maxValue)
    individuo = listaInd[indice]
    individuoSelect.append(individuo)
    individuoSelect.append(maxValue)
    individuoSelect.append(minValue)
    print(individuoSelect)
    return individuoSelect
    
if __name__ == "__main__":
    individuosBest = []
    generacionesProm = []
    graficar = []

    #se generan los individuos de la poblacion en la generacion inicial
    #Y al mismo tiempo nos da las aptitudes de cada uno de ellos
    listaInd, listaIndEva = pobIni()
    print("Individuos: \n", listaInd)
    print("-------------------")
    print("Evaluaciones: \n", listaIndEva)
    #Ciclamos según el número de generaciónes requeridas
    for g in range(1000):
        #Identificamos al mejor iindividuo y al peor individuo de cada generación
        best = evaluar(listaIndEva, listaInd)
        individuosBest.append(best)

        #Identificamos el promedio de aptitud por cada generación
        promedio = genePromedio(listaIndEva)
        generacionesProm.append(promedio)

        #Primer operador a realizar: Selección por Torneo con K=2
        seleccion = opeTorneo(listaIndEva, listaInd)
        #Segundo operador: Cruza Uniforme con probabilidad del 50%
        cruza = opeCruza(listaIndEva, seleccion)
        #Tercer operador: Mutación por inversión base N
        #NOTA:La probabilidad de mutación, se midofica en la línea 405
        mutacion = opeMutacion(cruza)
        
        listaInd = mutacion
        listaIndEva = []
        for i in mutacion:
            listaIndEva.append(evaluation(i))
    
    #Creamos un .CSV, con los resultados
    headers = ['Individuo', 'Mejor AP', 'Peor AP', 'AP Promedio']
    with open('C:/Users/diego/OneDrive/Documents/ComputoEvolutivo/P1.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(headers)
        f_object.close()
    for i in range(len(generacionesProm)):
        tupla = []
        for j in range(3):
            tupla.append(individuosBest[i][j])
        tupla.append(generacionesProm[i])
        with open('C:/Users/diego/OneDrive/Documents/ComputoEvolutivo/P1.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(tupla)
            f_object.close()
    #Mostramos el gráfico de los resultados
    resultsData = pd.read_csv('C:/Users/diego/OneDrive/Documents/ComputoEvolutivo/P1.csv', index_col = 0)
    resultsData.head()
    resultsData.plot()
    plt.show()