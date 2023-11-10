import time
from arbol import nodoArbol
from lista import Lista
from random import randint
from sorting import *


def generar_datos(cantidad_de_datos):
    list_datos = Lista()
    for _ in range(cantidad_de_datos):
        list_datos.insertar(randint(0,1000000))
    return list_datos


if __name__ == "__main__":
    #for _i in range(10):
        NUM = 1000
        list_datos = generar_datos(NUM)
        print("Procesando: 1) Bubble Sort")
        ti_bubble_sorting = time.time()
        bubble_sort(list_datos)
        tf_bubble_sorting = time.time()
        time_bubble_sort = tf_bubble_sorting - ti_bubble_sorting
        print(f"Demoro: {time_bubble_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 2) Bubble Plus Sort")
        ti_bubble_plus_sorting = time.time()
        bubble_plus_sort(list_datos)
        tf_bubble_plus_sorting = time.time()
        time_bubble_plus_sort = tf_bubble_plus_sorting - ti_bubble_plus_sorting
        print(f"Demoro: {time_bubble_plus_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 3) Bubble Bidirection Sort")
        ti_bubble_bi_sorting = time.time()
        bubble_bidiretion_sort(list_datos)
        tf_bubble_bi_sorting = time.time()
        time_bubble_bi_sort = tf_bubble_bi_sorting - ti_bubble_bi_sorting
        print(f"Demoro: {time_bubble_bi_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 4) Select Sort")
        ti_select_sorting = time.time()
        select_sort(list_datos)
        tf_select_sorting = time.time()
        time_select_sort = tf_select_sorting - ti_select_sorting
        print(f"Demoro: {time_select_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 5) Insert Sort")
        ti_insert_sorting = time.time()
        insert_sort(list_datos)
        tf_insert_sorting = time.time()
        time_insert_sort = tf_insert_sorting - ti_insert_sorting
        print(f"Demoro: {time_insert_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 6) Quick Sort")
        ti_quick_sorting = time.time()
        quick_sort(list_datos, 0, list_datos.get_tamanio() - 1)
        tf_quick_sorting = time.time()
        time_quick_sort = tf_quick_sorting - ti_quick_sorting
        print(f"Demoro: {time_quick_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 7) Merge Sort")
        ti_merge_sorting = time.time()
        merge_sort(list_datos)
        tf_merge_sorting = time.time()
        time_merge_sort = tf_merge_sorting - ti_merge_sorting
        print(f"Demoro: {time_merge_sort}\n")
        
        list_datos = generar_datos(NUM)
        print("Procesando: 8) Binary Tree Sort")
        ti_tree_sorting = time.time()
        arbol = nodoArbol(list_datos.index(0))
        for elemento in range(1, list_datos.get_tamanio()):
            arbol.insertarNodo(list_datos.index(elemento))
        tf_tree_sorting = time.time()
        time_tree_sort = tf_tree_sorting - ti_tree_sorting
        print(f"Demoro: {time_tree_sort}\n")
        print("********************************")
        
        print("tiempos:")
        print(time_bubble_sort)
        print(time_bubble_plus_sort)
        print(time_bubble_bi_sort)
        print(time_select_sort)
        print(time_insert_sort)
        print(time_quick_sort)
        print(time_merge_sort)
        print(time_tree_sort)
        print("")
