class Nodo:
    def __init__(self, registro):
        self.registro = registro
        self.siguiente = None
        self.anterior = None
        
class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None
        self.tamaño = 0
    
    def codigo_existe(self, codigo):
        actual = self.frente
        while actual != None:
            if actual.registro.getCodigo() == codigo:
                return True
            actual = actual.siguiente
        return False
    
    def esta_vacia(self):
        if self.tamaño == 0:
            return True
        else:
            return False
    
    def encolar(self, registro):
        if self.codigo_existe(registro.getCodigo()):
            return None
        nuevo = Nodo(registro)
        if self.esta_vacia():
            self.frente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        self.tamaño += 1
        return registro
    
    def desencolar_primero(self):
        if self.esta_vacia():
            return None
        registro = self.frente.registro
        self.frente = self.frente.siguiente
        if self.frente == None:
            self.ultimo = None
        else:
            self.frente.anterior = None
        self.tamaño -= 1
        return registro
    
    def desencolar_ultimo(self):
        if self.esta_vacia():
            return None
        registro = self.ultimo.registro
        self.ultimo = self.ultimo.anterior
        if self.ultimo == None:
            self.frente = None
        else:
            self.ultimo.siguiente = None
        self.tamaño -= 1
        return registro

    def mostrar_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.registro
    
    def mostrar_ultimo(self):
        if self.esta_vacia():
            return None
        return self.ultimo.registro
    
    def limpiar_cola(self):
        if self.esta_vacia():
            return None
        self.tamaño = 0
        self.frente = None
        self.ultimo = None
