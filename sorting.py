from lista import Lista


def bubble_sort(lista):
    for i in range(0, lista.get_tamanio() - 1):
        for j in range(0, lista.get_tamanio() - i - 1):
            if lista.index(j) > lista.index(j + 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j + 1))
                lista.reemplazo(j + 1, aux)


def bubble_plus_sort(lista):
    i = 0
    control = True
    while (i <= lista.get_tamanio() - 2) and control:
        control = False
        for j in range(0, lista.get_tamanio() - i - 1):
            if lista.index(j) > lista.index(j + 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j + 1))
                lista.reemplazo(j + 1, aux)
                control = True
        i = i + 1


def bubble_bidiretion_sort(lista):
    izquierda = 0
    derecha = lista.get_tamanio() - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if lista.index(i) > lista.index(i + 1):
                aux = lista.index(i)
                lista.reemplazo(i, lista.index(i + 1))
                lista.reemplazo(i, aux)
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if lista.index(j) > lista.index(j + 1):
                aux = lista.index(j)
                lista.reemplazo(j, lista.index(j + 1))
                lista.reemplazo(j + 1, aux)
                control = True
        izquierda += 1


def select_sort(lista):
    for i in range(0, lista.get_tamanio() - 1):
        min = i
        for j in range(i + 1, lista.get_tamanio()):
            if lista.index(j) < lista.index(min):
                min = j
        aux = lista.index(i)
        lista.reemplazo(i, lista.index(min))
        lista.reemplazo(min,aux)


def insert_sort(lista):
    for i in range(1, lista.get_tamanio() + 1):
        k = i - 1
        while (k > 0) and lista.index(k) < lista.index(k - 1):
            aux = lista.index(k)
            lista.reemplazo(k, lista.index(k - 1))
            lista.reemplazo(k - 1, aux)
            k -= 1


def quick_sort(lista, primero, ultimo):
    if primero < ultimo:
        pivote = ultimo
        izq = primero
        der = ultimo - 1
        while izq < der:
            while izq <= der and lista.index(izq) < lista.index(pivote):
                izq += 1
            while der >= izq and lista.index(der) > lista.index(pivote):
                der -= 1
            if izq < der:
                lista.reemplazo(izq, der)
        if lista.index(pivote) < lista.index(izq):
            lista.reemplazo(izq, pivote)
        quick_sort(lista, primero, izq - 1)
        quick_sort(lista, izq + 1, ultimo)


def merge_sort(lista):
    if lista.get_tamanio() <= 1:
        return lista
    else:
        medio = lista.get_tamanio() // 2
        izq = Lista()
        for i in range(0, medio):
            izq.insertar(lista.index(i))
        der = Lista()
        for i in range(medio, lista.get_tamanio()):
            der.insertar(lista.index(i))
        izq = merge_sort(izq)
        der = merge_sort(der)
        if izq.index(medio - 1) <= der.index(0):
            for i in range(der.get_tamanio()):
                izq.insertar(der.index(i))
            return izq
        resultado = mezcla(izq, der)
        return resultado


def mezcla(izq, der):
    lista_mezclada = Lista()
    while izq.get_tamanio() > 0 and (der.get_tamanio() > 0):
        if izq.index(0) < der.index(0):
            lista_mezclada.insertar(izq.extraer(0))
        else:
            lista_mezclada.insertar(der.extraer(0))
    if izq.get_tamanio() > 0:
        for i in range(izq.get_tamanio()):
            lista_mezclada.insertar(izq.index(i))
    if der.get_tamanio() > 0:
        for j in range(der.get_tamanio()):
            lista_mezclada.insertar(der.index(j))
    return lista_mezclada
