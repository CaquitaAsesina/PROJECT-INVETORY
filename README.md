Agenda Virtual 📇
Un sistema de gestión de contactos implementado en Python usando una estructura de datos tipo cola basada en lista doblemente enlazada.

🚀 Características Principales
✅ CRUD completo de contactos

🔍 Búsquedas avanzadas por múltiples criterios

🏗️ Estructura eficiente con lista doblemente enlazada

🎯 Validaciones automáticas (códigos únicos)

📊 Múltiples vistas (orden normal e inverso)

🖥️ Interfaz gráfica con Tkinter

🔄 Operaciones de cola (FIFO) tradicionales y especiales

📋 Operaciones Disponibles
Operaciones de Cola
encolar(contacto) - Agregar al final

desencolar() - Remover del frente

esta_vacia() - Verificar estado

limpiar() - Vaciar completamente

Búsquedas
busca_codigo(codigo) - Búsqueda por ID

busca_nombre(nombre) - Por nombre

busca_categoria(categoria) - Por categoría

busca_correo(correo) - Por email

busca_telefono(telefono) - Por teléfono

Eliminaciones
eliminar_codigo(codigo) - Por código

eliminar_categoria(categoria) - Todos de una categoría

desencolar_ultimo() - Remover el último

Visualización
mostrar_agenda() - Mostrar todos (frente → final)

mostrar_agenda_ultimo() - Mostrar en orden inverso

mostrar_frente() - Ver primer elemento

mostrar_ultimo() - Ver último elemento

🖥️ Interfaz Gráfica
Ejecuta python fronted.py para abrir la interfaz que incluye:

📝 Formulario para agregar contactos

🔍 Campo de búsqueda con filtros

📋 Lista visual de todos los contactos

🛠️ Botones para todas las operaciones CRUD

📊 Visualización en orden normal e inverso

🎯 Ejemplos de Casos de Uso
Agenda Personal: Gestionar contactos de amigos y familia

Clientes de Negocio: Clasificar clientes por categorías

Lista de Proveedores: Mantener información de contacto organizada

Red de Contactos: Búsqueda rápida por diferentes criterios

📝 Requisitos
Python 3.8 o superior

Tkinter (generalmente incluido con Python)

pip pillow

👨‍💻 Autor
Jhostin Álvarez - Implementación completa del sistema
