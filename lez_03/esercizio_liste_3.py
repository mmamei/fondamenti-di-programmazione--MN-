end_color = "\033[0m"
blue = '\033[94m'
red = '\033[91m'
cyan = '\033[36m'
magenta = '\033[35m'
green = '\033[32m'
yellow = '\033[33m'



def ordina(lista):
    '''
    ordinare gli elementi con il seguente algoritmo: 
    Ad esempio ricevo la lista **[2 3 1]** 
    Trovo l'elemento minimo e scambio l'elemento minimo con il primo 
    (scambio 1 e 2) **[1 3 2]** 
    Ripeto l'operazione saltando il primo elemento 
    (che è già ordinato). 
    Trovo il minimo tra **[3 2]** cioè 2 e scambio **[1 2 3]**
    '''
    for i in range(len(lista)):
        print(blue,lista,end_color)
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(red,'scambio',lista[i], lista[min_index],end_color)
    return lista

x = [2,3,1,4,1]
print(x)
print(ordina(x))