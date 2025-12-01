**Agenda Virtual — Documentación completa**

**Resumen:**

- **Proyecto:** Agenda Virtual
- **Autor:** Jhostin Álvarez
- **Lenguaje:** Python
- **Descripción breve:** Implementación de una agenda de contactos basada en una estructura tipo cola construida con una lista doblemente enlazada. Permite operaciones CRUD, búsquedas por distintos campos y utilidades para manejo de la colección (limpiar, mostrar frente/último, etc.).

Este documento explica en detalle la arquitectura, las clases principales, la API disponible, ejemplos de uso y recomendaciones para extender o ejecutar la aplicación.

**Estructura del repositorio (`inventory`)**

- `clase.py`: Modelo de datos que representa un contacto (clase `Sistema` o similar).
- `cola.py`: Implementación de la estructura de datos; define el `Nodo`, la `Cola` y todas las operaciones (encolar, desencolar, búsquedas, eliminaciones, etc.).
- `run.py`: Script de arranque / ejemplos de uso desde consola.
- `fronted.py`: (Probablemente) interfaz gráfica básica o código de integración con una GUI.
- `README.md`: Este archivo (documentación extendida).

Si tus archivos tienen nombres ligeramente distintos, ajusta las referencias arriba; los archivos citados son los localizados en este módulo `inventory`.

**Diseño y conceptos clave**

1. Modelo de datos (Contacto)

- Propósito: representar la información de un contacto en la agenda.
- Campos habituales (atributos esperados en `clase.py`):
  - `codigo` (int o str): identificador único del contacto.
  - `nombre` (str): nombre de pila.
  - `apellido` (str)
  - `correo` (str)
  - `telefono` (str)
  - `categoria` (str): etiqueta o categoría (ej. "Trabajo", "Familia", "Amigos").

2. Estructura de almacenamiento: Lista doblemente enlazada como Cola

- Se usa una implementación de cola donde cada nodo apunta a `siguiente` y `anterior`.
- Ventajas de la implementación doblemente enlazada:
  - Eliminaciones por referencia (cuando se encuentra el nodo) se realizan en O(1) para ajustar punteros.
  - Recorrido desde el frente o desde el final sin costo adicional.

3. Operaciones principales y su comportamiento

- `encolar(registro)`: Inserta al final de la cola. Antes de insertar valida que `codigo` no exista para evitar duplicados.
- `desencolar()`: Remueve y devuelve el elemento del frente (primer elemento) — comportamiento típico de una cola FIFO. Si está vacía, debe manejar la condición (retornar `None` o lanzar excepción según implementación).
- `limpiar()`: Elimina todos los nodos y deja la estructura vacía.
- `mostrar_agenda()`: Recorre desde el frente hasta el final y devuelve o imprime una lista formateada de contactos.
- `mostrar_agenda_ultimo()` / `mostrar_ultimo()`: Recorre desde el final hacia el frente o devuelve el último elemento insertado.
- `mostrar_frente()`: Devuelve el primer contacto sin eliminarlo.

4. Validaciones y utilidades

- `esta_vacia()`: True si no hay nodos.
- `codigo_existe(codigo)`: Recorre y verifica duplicados antes de encolar.

5. Búsquedas (operaciones de lectura)

- `busca_codigo(codigo)`: Búsqueda por `codigo`, devuelve el contacto o `None`.
- `busca_nombre(nombre)`, `busca_apellido(apellido)`, `busca_correo(correo)`, `busca_telefono(telefono)`: Búsquedas por campos; pueden devolver el primer resultado o una lista de coincidencias, según la implementación.
- `busca_categoria(categoria)`: Retorna múltiples coincidencias (lista) ya que varias entradas pueden compartir categoría.

6. Eliminaciones por criterio

- `desencolar_ultimo()` (o `desencolar_ultimo`): Elimina el último nodo insertado (comportamiento similar a una pila en el extremo posterior).
- `eliminar_codigo(codigo)`: Busca el nodo con ese `codigo` y lo remueve ajustando `anterior` y `siguiente`.
- `eliminar_nombre(nombre)` / `eliminar_apellido(apellido)` / `eliminar_correo(correo)` / `eliminar_telefono(telefono)` / `eliminar_categoria(categoria)`: Eliminan una o varias entradas que coincidan con la condición. Para categoría se espera la eliminación de múltiples nodos (iterar y remover todas las coincidencias).

**Contratos esperados de métodos (firmas y comportamiento esperado)**

- `encolar(registro: Sistema) -> bool`:

  - Inserta `registro` si `codigo` no está duplicado.
  - Retorna `True` si la inserción fue exitosa, `False` si hubo conflicto de `codigo`.

- `desencolar() -> Optional[Sistema]`:

  - Si cola no vacía: remueve y retorna el objeto del frente.
  - Si vacía: retorna `None` o lanza `IndexError` dependiendo de la implementación.

- `mostrar_agenda() -> List[Sistema]` o `-> str` (formateado):

  - Devuelve una representación de todos los contactos en orden desde el frente.

- `busca_codigo(codigo) -> Optional[Sistema]`:

  - Busca y devuelve el contacto o `None`.

- `eliminar_codigo(codigo) -> bool`:
  - Si existe el contacto, lo elimina y retorna `True`; si no, retorna `False`.

Nota: Adapta las expectativas a lo que tu código realmente implementa; los nombres y retornos pueden variar ligeramente.

**Ejemplos de uso (consola)**

Supongamos que `clase.py` define `Sistema` y `cola.py` define `Cola`. Un script típico de uso en `run.py` podría lucir así (ejemplo ilustrativo):

```python
from clase import Sistema
from cola import Cola

agenda = Cola()

# Crear contactos
c1 = Sistema(codigo=1, nombre='Ana', apellido='Pérez', correo='ana@example.com', telefono='999-000-111', categoria='Amigos')
c2 = Sistema(codigo=2, nombre='Luis', apellido='García', correo='luis@example.com', telefono='999-000-222', categoria='Trabajo')

# Encodar
agenda.encolar(c1)
agenda.encolar(c2)

# Mostrar agenda
print(agenda.mostrar_agenda())

# Buscar por código
print(agenda.busca_codigo(2))

# Eliminar por código
agenda.eliminar_codigo(1)

# Desencolar (sacar el primer registro)
agenda.desencolar()

# Limpiar todo
agenda.limpiar()
```

Coloca ese ejemplo en `run.py` para poder ejecutarlo directamente:

```powershell
python .\inventory\run.py
```

Si en Windows tienes `python` apuntando a la versión correcta, el comando anterior ejecutará el ejemplo; si usas un entorno virtual activa con `venv` primero.

**Interfaz gráfica (`fronted.py`)**

Si `fronted.py` implementa una GUI (por ejemplo con `tkinter`):

- Debe proporcionar formularios para crear/editar un contacto y botones que llamen a las funciones de `Cola`.
- Botones mínimos recomendados: `Agregar`, `Eliminar por código`, `Buscar`, `Limpiar`, `Mostrar todo`.
- Para persistencia temporal la GUI puede mostrar la lista en un `Listbox` o `Treeview`.

Si prefieres, puedo inspeccionar `fronted.py` y proponer mejoras en la GUI (validaciones de inputs, confirmaciones, manejo de errores) — dime si quieres eso.

**Casos límite y recomendaciones de robustez**

- Manejo de duplicados: validar `codigo` único antes de encolar (actualmente existe `codigo_existe`). Si la aplicación será usada en red o multi-hilo, necesitarás sincronización.
- Validación de campos: verificar formato de `correo`, longitud/formatos de `telefono` y que `codigo` tenga el tipo esperado.
- Persistencia: Actualmente la estructura es en memoria; para hacer persistente la agenda, añade serialización a JSON/CSV o uso de SQLite.
- Manejo de excepciones: todas las operaciones que remueven o buscan deberían manejar la cola vacía y entradas no encontradas sin romper la ejecución del programa.

**Sugerencias de mejora/funcionalidades futuras**

- Añadir persistencia con `sqlite3` o `shelve` para mantener los contactos entre sesiones.
- Exportar/importar contactos en `CSV` o `JSON`.
- Añadir pruebas unitarias con `unittest` o `pytest` para cubrir:
  - Inserción y eliminación (incluyendo extremos: primero/último).
  - Búsquedas que retornen múltiples resultados.
  - Validaciones de duplicados.
- Mejorar la GUI: búsquedas en tiempo real, filtros por categoría y paginación si hay muchos contactos.

**Cómo leer/entender el código fuente rápidamente**

1. Abre `clase.py` y localiza la clase que modela el contacto — revisa sus atributos y métodos (si tiene `__repr__` o `__str__` útiles para impresión).
2. Abre `cola.py` y revisa las definiciones de `Nodo` y `Cola`:
   - Observa cómo se actualizan `frente` y `final` al encolar/desencolar.
   - Revisa las funciones de búsqueda y eliminación para ver si devuelven objetos, índices o booleanos.
3. Abre `run.py` para ver ejemplos concretos de uso; si no existe, añade uno similar al ejemplo de este README.
4. Revisa `fronted.py` para ver si contiene lógica directa que debe delegarse a `Cola` (mejor separación de responsabilidades).

**Ejemplo de pruebas rápidas (pytest)**

Crear `tests/test_cola.py` con:

```python
import pytest
from clase import Sistema
from cola import Cola

def test_encolar_desencolar():
		cola = Cola()
		s = Sistema(codigo=10, nombre='T', apellido='A', correo='t@a.com', telefono='1', categoria='X')
		assert cola.encolar(s) is True
		assert cola.desencolar().codigo == 10

def test_codigo_unico():
		cola = Cola()
		s1 = Sistema(codigo=11, nombre='A', apellido='B', correo='a@b.com', telefono='2', categoria='C')
		s2 = Sistema(codigo=11, nombre='D', apellido='E', correo='d@e.com', telefono='3', categoria='C')
		assert cola.encolar(s1) is True
		assert cola.encolar(s2) is False
```

Instalar pytest (si se necesita):

```powershell
pip install pytest
pytest -q
```

**Notas finales y siguientes pasos recomendados**

- He documentado la arquitectura, uso y mejoras recomendadas para tu proyecto `inventory`.
- Pasos que puedo ejecutar ahora si me lo indicas:
  - Abrir los archivos `clase.py`, `cola.py`, `run.py` y `fronted.py` para generar documentación linea-a-linea o mejorar el código.
  - Añadir ejemplos ejecutables en `run.py` y pruebas unitarias en `tests/`.
  - Implementar persistencia (opcional) y un pequeño menú CLI.

Si quieres que continúe, dime qué prefieres: "inspeccionar código y ajustar README con detalles encontrados" o "añadir pruebas y ejemplos ejecutables". Estoy listo para seguir.
