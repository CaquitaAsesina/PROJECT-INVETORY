# 📒 Sistema de Agenda Virtual

El **Sistema de Agenda Virtual** es una aplicación diseñada para gestionar contactos utilizando una **cola bidireccional** implementada con una **lista doblemente enlazada**.  
Permite registrar, buscar, modificar y eliminar contactos, manteniendo una estructura eficiente sin uso de bases de datos externas.

---

## 🚀 Características Principales

- **Estructura dinámica:** lista doblemente enlazada simulando una cola.
- **Acceso bidireccional:** operaciones desde el frente y el final.
- **Validación estricta:** evita códigos duplicados.
- **Búsquedas flexibles:** por código, nombre, apellido, correo, teléfono o categoría.
- **Eliminación y modificación en cualquier posición.**
- **Persistencia en memoria:** no requiere archivos ni bases de datos.

---

## 🧩 Estructura del Sistema

### 🔹 Clase `Sistema` (Modelo de Contacto)

Representa un contacto con los siguientes atributos:

- `codigo`
- `nombre`
- `apellido`
- `correo`
- `telefono`
- `categoria`

Incluye:

- Encapsulación mediante getters y setters.
- Método `__str__()` para mostrar el contacto formateado.

---

### 🔹 Clase `Nodo`

Elemento básico de la lista doblemente enlazada.

- `registro` → contacto almacenado
- `siguiente` → referencia al nodo siguiente
- `anterior` → referencia al nodo anterior

---

### 🔹 Clase `Cola`

Estructura principal del sistema, con:

- `frente`
- `ultimo`
- `tamaño`

#### **Operaciones principales**

| Tipo de operación | Métodos                                                       |
| ----------------- | ------------------------------------------------------------- |
| Inserción         | `encolar()`                                                   |
| Eliminación       | `desencolar()`, `desencolar_ultimo()`                         |
| Búsquedas         | `busca_codigo()`, `busca_nombre()`, `busca_categoria()`, etc. |
| Modificaciones    | `modificar_frente()`, `modificar_ultimo()`                    |
| Visualización     | `mostrar_agenda()`, `mostrar_agenda_ultimo()`                 |

---

## ⚙️ Funcionamiento Interno

### ✔ Encolar

Inserta un contacto al final.  
Complejidad: **O(1)**.

### ✔ Desencolar

Elimina el contacto del frente.  
Complejidad: **O(1)**.

### ✔ Búsquedas

Recorre la lista completamente, según el criterio.  
Complejidad: **O(n)**.

### ✔ Eliminaciones específicas

Permite eliminar por:

- Código
- Categoría
- Desde el final

Complejidad: **O(n)** cuando requiere recorrido.

---

## 🧪 Flujo Típico de Operaciones

### ➤ Agregar un contacto

1. Validar que el código no exista.
2. Crear nodo nuevo.
3. Enlazar al final de la cola.
4. Incrementar tamaño.

### ➤ Eliminar un contacto por código

1. Recorrer la cola hasta encontrarlo.
2. Ajustar punteros según su posición (frente, medio o final).
3. Reducir tamaño.

### ➤ Buscar por categoría

1. Recorrer desde el frente.
2. Comparar categoría.
3. Retornar lista de coincidencias.

---

## 🛡 Validaciones y Manejo de Errores

- No permite códigos duplicados.
- Todas las operaciones verifican si la estructura está vacía.
- Los punteros se actualizan correctamente al eliminar nodos.

---

## 📌 Ventajas y Limitaciones

### ✔ Ventajas

- Operaciones básicas en tiempo constante.
- Estructura dinámica y eficiente.
- Eliminaciones específicas sin necesidad de reordenar.
- Búsquedas amplias por múltiples campos.

### ✖ Limitaciones

- Datos no persistentes (se pierden al cerrar la app).
- Búsquedas y eliminaciones internas son O(n).
- No incluye ordenamiento automático.

---

# 🖥 Cómo Ejecutar la Agenda Virtual

Sigue estos pasos:

---

## 1️⃣ Crear entorno virtual (si no existe)

python -m venv venv

## 2️⃣ Activar entorno virtual

Windows:
venv\Scripts\activate

Linux / MacOS:
source venv/bin/activate

## 3️⃣ Instalar dependencias

pip install -r requirements.txt

## 4️⃣ Ejecutar la aplicación

python run.py
