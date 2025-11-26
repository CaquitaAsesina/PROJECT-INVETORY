class Sistema:
    def __init__(self, codigo, nombre, apellido, correo, telefono, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.categoria = categoria
    
    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getApellido(self):
        return self.apellido
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono

    def getCategoria(self):
        return self.categoria    
    
    def setCategoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return f"👤CODIGO:\n ⏩{self.codigo}\n👤NOMBRES:\n ⏩{self.nombre.upper()}\n👤APELLIDOS:\n ⏩{self.apellido.upper()}\n👤CORREO:\n ⏩{self.correo.upper()}\n👤TELEFONO:\n ⏩{self.telefono}\n👤CATEGORIA:\n ⏩{self.categoria.upper()}"
