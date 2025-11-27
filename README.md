💼 TITULO DEL PROYECTO → AGENDA VIRTUAL
👤 PROGRAMER → JHOSTIN ALVAREZ
📒 CURSO → ALGORITMO Y ESTRUCTURA DE DATOS

📌 DESCRIPCION:
Sistema de agenda virtual desarrollado en Python que permite gestionar contactos utilizando una estructura de datos de cola con listas doblemente enlazadas. La aplicación cuenta con una interfaz gráfica intuitiva para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de contactos.

📂 ESTRUCTURA DEL PROYECTO:

🔧 Clases Principales 

✔️ Sistema - Modelo de Datos → clase.py

-Representa un contacto en la agenda con los siguientes atributos:

Código: Identificador único

Nombre: Nombre del contacto

Apellido: Apellido del contacto

Correo: Dirección de email

Teléfono: Número de contacto

Categoría: Clasificación del contacto

✔️ Nodo - Estructura de Almacenamiento → cola.py

-Nodo para la lista doblemente enlazada que contiene:

registro: Objeto Sistema

siguiente: Referencia al siguiente nodo

anterior: Referencia al nodo anterior

✔️ Cola - Lógica de Negocio → cola.py

Implementa una cola con operaciones completas:

📊 Funciones principales

✅ encolar(registro): Agrega un nuevo contacto

✅ desencolar(): Elimina el primer contacto registrado

✅ limpiar(): Elimina todos los contactos registrados

✅ mostrar_agenda(): Muestra todos los contactos registrados

🔴 Validaciones

✅esta_vacia(): Verifica si la agenda esta vacia

✅codigo_existe(): Evita duplicados de codigos

📒 Funciones especiales

🔎 Operaciones de busqueda

☑️ busca_codigo(codigo): Busqueda por codigo del contacto registrado

☑️ busca_nombre(nombre): Busqueda por nombre del contacto registrado

☑️ busca_apellido(apellido): Busqueda por apellido del contacto registrado

☑️ busca_correo(correo): Busqueda por correo del contacto registrado

☑️ busca_telefono(telefono): Busqueda por telefono del contacto registrado

☑️ busca_categoria(categoria): Busqueda multiple por categoria de los contactos registrados

🗑️ Operaciones de eliminacion

☑️ deseconlar_ultimo(): Elimina el ultimo contacto registrado

☑️ eliminar_codigo(codigo): Elimina por codigo unico del contacto

☑️ eliminar_nombre(nombre): Elimina por nombre del contacto registrado

☑️ eliminar_apellido(apellido): Elimina por apellido del contacto registrado

☑️eliminar_correo(correo): Elimina por correo del contacto registrado

☑️ eliminar_telefono(telefono): Elimina por telefono del contacto registrado

☑️ eliminar_categoria(categoria): Elimina por categoria a multples contactos

👁️‍🗨️ Operacion de visualizacion

☑️ mostrar_frente(): Muestra el primer contacto registrado

☑️ mostrar_ultimo(): Muestra el ultimo contacto registrado

☑️ mostrar_agenda_ultimo(): Muestra los contactos desde el final
