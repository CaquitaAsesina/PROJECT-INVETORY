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
    
    #VERIFICAR
    def esta_vacia(self):
        if self.tamaño == 0:
            return True
        else:
            return False

    def codigo_existe(self, codigo):
        actual = self.frente
        while actual != None:
            if actual.registro.getCodigo() == codigo:
                return True
            actual = actual.siguiente
        return False
    
    #AGREGAR (ENQUEUE)
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
    
    #BUSCAR (SEARCH)
    def busca_codigo(self, codigo):
        actual = self.frente
        while actual != None:
            if actual.registro.getCodigo() == codigo:
                return actual.registro
            actual = actual.siguiente
        return None
    
    def busca_nombre(self, nombre):
        actual = self.frente
        while actual != None:
            if actual.registro.getNombre() == nombre:
                return actual.registro
            actual = actual.siguiente
        return None
    
    def busca_apellido(self, apellido):
        actual = self.frente
        while actual != None:
            if actual.registro.getApellido() == apellido:
                return actual.registro
            actual = actual.siguiente
        return None
    
    def busca_correo(self, correo):
        actual = self.frente
        while actual != None:
            if actual.registro.getCorreo() == correo:
                return actual.registro
            actual = actual.siguiente
        return None
    
    def busca_telefono(self, telefono):
        actual = self.frente
        while actual != None:
            if actual.registro.getTelefono() == telefono:
                return actual.registro
            actual = actual.siguiente
        return None
    
    def busca_categoria(self, categoria):
        registros = []
        actual = self.frente
        while actual != None:
            if actual.registro.getCategoria() == categoria:
                registros.append(actual.registro)
            actual = actual.siguiente
        if registros == None:
            return None
        return registros
    
    #ELIMINAR (DEQUEUE)
    def desencolar(self):
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
    
    def eliminar_codigo(self, codigo):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getCodigo() == codigo:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente != None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente =None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.tamaño -= 1
                return usuario
        actual = actual.siguiente
        return None
    
    def eliminar_nombre(self, nombre):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getNombre() == nombre:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente != None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente =None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.tamaño -= 1
                return usuario
        actual = actual.siguiente
        return None
    
    def eliminar_apellido(self, apellido):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getApellido() == apellido:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente != None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente =None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.tamaño -= 1
                return usuario
        actual = actual.siguiente
        return None
    
    def eliminar_correo(self, correo):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getCorreo() == correo:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente != None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente =None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.tamaño -= 1
                return usuario
        actual = actual.siguiente
        return None
    
    def eliminar_telefono(self, telefono):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getTelefono() == telefono:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente != None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    self.ultimo.siguiente =None
                
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                self.tamaño -= 1
                return usuario
        actual = actual.siguiente
        return None
    
    def eliminar_categoria(self, categoria):
        if self.esta_vacia():
            return None
        usuarios = []
        actual = self.frente
        while actual is not None:
            siguiente = actual.siguiente  
            if actual.registro.getCategoria() == categoria:
                usuario = actual.registro
                if actual == self.frente:
                    self.frente = actual.siguiente
                    if self.frente is not None:
                        self.frente.anterior = None
                    else:
                        self.ultimo = None
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    if self.ultimo is not None:
                        self.ultimo.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
    
                self.tamaño -= 1
                usuarios.append(usuario)
            actual = siguiente
        if not usuarios:
            return None
        return usuarios
    
    #MODIFICAR (UPDATE)
    def modificar_nombre(self, codigo, nombre):
        if self.esta_vacia():
            return None
        actual = self.frente
        while actual != None:
            if actual.registro.getId() == id:
                actual.registro.setNombre(nombre)
                return actual.registro
            actual = actual.siguiente
        return None

    #MOSTRAR (SHOW)
    def mostrar_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.registro
    
    def mostrar_ultimo(self):
        if self.esta_vacia():
            return None
        return self.ultimo.registro
    
    def mostrar_agenda(self):
        if self.esta_vacia():
            return None
        actual = self.frente
        agenda = []
        while actual != None:
            agenda.append(actual.registro)
            actual = actual.siguiente
        return agenda
    
    def mostrar_ageneda_ultimo(self):
        if self.esta_vacia():
            return None
        actual = self.ultimo
        agenda = []
        while actual != None:
            agenda.append(actual.registro)
            actual = actual.anterior
        return agenda
    
        #LIMPIAR (CLEAN)
    def limpiar_cola(self):
        if self.esta_vacia():
            return None
        self.tamaño = 0
        self.frente = None
        self.ultimo = None
        return 1