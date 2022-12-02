

def ruleta(lista):
    listaSumas = []
    listaSumas.append(lista [0])
    for i in lista[1:]:
        pos = len(listaSumas)-1
        listaSumas.append(i+listaSumas[pos])

if __name__ == "__main__":
    lista = [50.3,42.5,39.8,40.7,35.2]

    print(lista)
