class nodoselfSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


    def insertar(self, info):
        nodo = nodoselfSimple()
        nodo.info = info
        if self.inicio is None:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while siguiente is not None:
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            nodo.siguiente = siguiente
            actual.siguiente = nodo
        self.tamanio += 1


    def imprimir(self):
        actual = self.inicio
        texto = "["
        while actual is not None:
            if actual.siguiente != None:
                texto = f"{texto}{actual.info}, "
            else:
                texto = f"{texto}{actual.info}]"
            actual = actual.siguiente
        print(texto)


    def get_tamanio(self):
        return self.tamanio


    def eliminar(self, info):
        data = None
        if(self.inicio.info == info):
            data = self.inicio
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while (siguiente is not None and info != siguiente.info):
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            if(siguiente is not None):
                data = siguiente.info
                actual.siguiente = siguiente.siguiente
                self.tamanio -= 1
        return data


    def index_of(self, info):
        actual = self.inicio
        index = 0
        for _ in range(self.tamanio):
            if actual.info == info:
                return index
            index += 1
            actual = actual.siguiente
        else:
            return None


    def index(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        return actual.info


    def reemplazo(self, indice, info):
            actual = self.inicio
            for _ in range(indice):
                actual = actual.siguiente
                if actual == None:
                    return None
            actual.info = info

    def extraer(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        data = actual.info
        self.eliminar(data)
        return data
