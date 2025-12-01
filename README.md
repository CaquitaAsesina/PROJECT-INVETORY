DOCUMENTACIÓN DEL SISTEMA DE AGENDA VIRTUAL

1. Descripción General
Este sistema implementa una agenda virtual utilizando una cola bidireccional basada en una lista doblemente enlazada. Permite gestionar contactos con operaciones típicas de una cola (FIFO - First In First Out) junto con funcionalidades adicionales de búsqueda, modificación y eliminación en cualquier posición.

Características principales:
Estructura de datos: Lista doblemente enlazada que simula una cola

Persistencia en memoria: Todos los datos se mantienen en memoria durante la ejecución

Validación: Evita códigos duplicados

Operaciones bidireccionales: Tanto desde el frente como desde el final

Búsquedas múltiples: Por diferentes campos del contacto

2. Estructura de Clases

2.1 Clase Sistema - Modelo de Datos
Representa un contacto en la agenda con los siguientes atributos:

Atributos:
codigo (str/int): Identificador único del contacto
nombre (str): Nombre del contacto
apellido (str): Apellido del contacto
correo (str): Correo electrónico
telefono (str): Número de teléfono
categoria (str): Categoría/clasificación del contacto

Métodos principales:

Getters y Setters: Para cada atributo, siguiendo el principio de encapsulación

**str**(): Representación formateada del contacto para visualización

2.2 Clase Nodo - Elemento de la Lista Enlazada

Atributos:
registro (Sistema): Objeto contacto almacenado en el nodo
siguiente (Nodo): Referencia al nodo siguiente (None si es el último)
anterior (Nodo): Referencia al nodo anterior (None si es el primero)

2.3 Clase Cola - Estructura Principal

Implementa una cola bidireccional usando lista doblemente enlazada.

Atributos:
frente (Nodo): Primer elemento de la cola
ultimo (Nodo): Último elemento de la cola
tamaño (int): Número total de elementos en la cola

3. Funcionamiento Detallado

3.1 Principios de la Cola Bidireccional

Estado inicial: frente = None, ultimo = None, tamaño = 0

Operación: encolar(registro1)
Resultado: frente → registro1 ← ultimo
tamaño = 1

Operación: encolar(registro2)
Resultado: frente → registro1 ↔ registro2 ← ultimo
tamaño = 2

Operación: encolar(registro3)
Resultado: frente → registro1 ↔ registro2 ↔ registro3 ← ultimo
tamaño = 3

3.2 Operaciones Disponibles
3.2.1 Operaciones Básicas de Cola

Método → Descripción → Complejidad
encolar(registro) →Agrega un contacto al final de la cola → O(1)
desencolar() → Elimina y retorna el contacto del frente → O(1)
esta_vacia() → Verifica si la cola está vacía → O(1)
mostrar_frente() →Muestra el contacto del frente sin eliminarlo → O(1)
mostrar_ultimo() →Muestra el último contacto sin eliminarlo → O(1)

3.2.2 Búsquedas

Método →Descripción →Complejidad
busca_codigo(codigo)→ Busca por código único→ O(n)
busca_nombre(nombre)→ Busca por nombre exacto →O(n)
busca_categoria(categoria) →Retorna lista de contactos por categoría →O(n)
Otras búsquedas: Por apellido, correo, teléfono→ Similar funcionamiento →O(n)

3.2.3 Eliminaciones

Método→ Descripción→Complejidad
desencolar_ultimo() →Elimina desde el final (no estándar en colas)→ O(1)
eliminar_codigo(codigo) →Elimina un nodo específico por código →O(n)
eliminar_categoria(categoria) →Elimina todos los contactos de una categoría→ O(n)

3.2.4 Modificaciones

Método→ Descripción →Complejidad
modificar_frente(nuevo_valor) →Modifica atributos del frente→ O(1)
modificar_ultimo(nuevo_valor) →Modifica atributos del final →O(1)

3.2.5 Visualización

Método →Descripción →Complejidad
mostrar_agenda() →Lista todos los contactos desde el frente→ O(n)
mostrar_agenda_ultimo() →Lista todos los contactos desde el final →O(n)

4. Flujos de Operación

4.1 Agregar un Contacto

Paso 1: Verificar si el código ya existe (codigo_existe())
⮕ Si existe: retorna None, no se agrega
⮕ Si no existe: continúa

Paso 2: Crear nuevo nodo con el registro
Paso 3: Si la cola está vacía:
frente = nuevo
ultimo = nuevo
Sino:
ultimo.siguiente = nuevo
nuevo.anterior = ultimo
ultimo = nuevo
Paso 4: Incrementar tamaño en 1

4.2 Eliminar por Código

Paso 1: Verificar si la cola está vacía
Paso 2: Recorrer la lista hasta encontrar el código
Paso 3: Reconfigurar punteros según la posición:
• Si es el frente: mover frente al siguiente
• Si es el último: mover último al anterior
• Si está en medio: puentear el nodo
Paso 4: Reducir tamaño en 1

4.3 Buscar Contactos por Categoría

Paso 1: Crear lista vacía para resultados
Paso 2: Recorrer toda la cola desde el frente
Paso 3: Para cada nodo, comparar la categoría
Paso 4: Si coincide, agregar a la lista de resultados
Paso 5: Retornar lista (puede estar vacía) 5. Validaciones y Control de Errores

5.1 Códigos Únicos

El sistema garantiza que no existan códigos duplicados mediante:
Verificación en encolar() antes de agregar
Retorno de None si se intenta agregar duplicado

5.2 Manejo de Cola Vacía
Todos los métodos verifican esta_vacia() antes de operar, retornando None cuando corresponda.

5.3 Integridad de Referencias
En operaciones de eliminación, se actualizan correctamente los punteros anterior y siguiente para mantener la integridad de la lista doble.

6. Ventajas de la Implementación

6.1 Ventajas

Acceso bidireccional: Permite operaciones desde ambos extremos
Búsqueda flexible: Encuentra contactos por cualquier campo
Eliminación específica: Puede eliminar nodos en cualquier posición
Memoria eficiente: Solo usa memoria para los elementos existentes
Operaciones O(1): Para operaciones básicas de cola

6.2 Limitaciones

Complejidad O(n): Para búsquedas y eliminaciones específicas
Sin persistencia: Los datos se pierden al terminar la ejecución
Sin ordenamiento: Los contactos no se ordenan automáticamente

PASOS PARA USAR LA AGENDA VIRTUAL

1. Crear un entorno virtual (si aún no existe)

Si el proyecto no incluye un entorno virtual, crea uno dentro de la carpeta del proyecto usando:
→ python -m venv venv

2. Activar el entorno virtual

Ubícate dentro de la carpeta del proyecto y activa el entorno virtual.
→ venv\Scripts\activate

3. Instalar las dependencias del proyecto

Una vez el entorno virtual esté activado, instala todos los paquetes necesarios ejecutando:
→ pip install -r requirements.txt

4. Ejecutar la aplicación

Cuando las dependencias estén instaladas, inicia la Agenda Virtual corriendo el archivo principal:
→ python run.py
