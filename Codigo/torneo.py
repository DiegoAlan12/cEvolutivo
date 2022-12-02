def torneo(listaind):
    newList = []
    for i in listaind:
        if i <= fa:
            newList.append(i)

    secondList = sorted(newList, reverse=True)

    if len(secondList) >= 4:
        tresMejores = secondList[:4]
        return(tresMejores)
        print(tresMejores)
    else:
        return(secondList)
        print(secondList)

    

if __name__ == "__main__":
    torneo([[1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],[0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]])