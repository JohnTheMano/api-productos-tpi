💻 Gestión de Productos y Categorías
Trabajo Práctico — Programación IV | Unidad 7: Server State y Navegación

Aplicación web desarrollada con React y TypeScript para la gestión de categorías de productos, conectada a una API REST desarrollada con FastAPI.

📌 Descripción del proyecto
El sistema permite consultar y administrar categorías de productos desde una interfaz web sencilla e intuitiva.

Algunos ejemplos de categorías son Informática y Accesorios, con sus respectivas descripciones.

La gestión de categorías se realiza desde el frontend. Las operaciones sobre productos y las asociaciones entre productos y categorías se implementan en el backend y se verifican mediante REST Client, de acuerdo con la consigna.

🚀 Tecnologías utilizadas

Tecnología	Uso
React	Construcción de la interfaz
TypeScript	Tipado estático
Vite	Entorno de desarrollo y compilación
Tailwind CSS	Estilos y diseño visual
TanStack Query	Gestión del estado del servidor y caché
React Router	Navegación entre páginas
Fetch API	Comunicación con el backend
✨ Funcionalidades
📋 Listado de categorías.
➕ Creación de categorías mediante un modal.
✏️ Edición de categorías existentes.
🗑️ Eliminación de categorías con confirmación.
🔄 Actualización de los datos mediante invalidación de caché con TanStack Query.
🧭 Navegación entre las secciones de categorías y productos.
⚠️ Manejo de estados de carga y errores.
📁 Estructura del proyecto

text
src/
├── components/
│   ├── Navbar.tsx
│   ├── CategoriaCard.tsx
│   ├── CategoriaList.tsx
│   └── CategoriaModal.tsx
├── pages/
│   ├── CategoriasPage.tsx
│   └── ProductsPage.tsx
├── services/
│   └── categoria.ts
├── types/
│   ├── categoria.ts
│   └── producto.ts
├── App.tsx
├── main.tsx
└── index.css
⚙️ Requisitos previos
Antes de ejecutar el proyecto, necesitás tener instalado:

Node.js
pnpm
También debe estar funcionando el backend de FastAPI.

🛠️ Instalación y ejecución
1. Instalar las dependencias

Desde una terminal ubicada en la carpeta frontend, ejecutar:


powershell
pnpm install
2. Iniciar el servidor de desarrollo


powershell
pnpm dev
Vite mostrará la dirección local para abrir la aplicación en el navegador. Por defecto, suele ser:

http://localhost:5173

3. Verificar la compilación


powershell
pnpm build
Este comando verifica el proceso de compilación de producción.

🔌 Conexión con el backend
La aplicación se comunica con la API de categorías mediante la siguiente dirección:

http://localhost:8000/categorias/

La documentación interactiva de FastAPI está disponible en:

http://127.0.0.1:8000/docs

El backend debe estar iniciado para que las operaciones de categorías funcionen correctamente.

🧭 Navegación

Ruta	Descripción
/categorias	Listado y administración de categorías
/productos	Página informativa de productos
🎓 Objetivo académico
Este proyecto permite aplicar los conceptos de:

Gestión del estado del servidor con TanStack Query.
Consultas y mutaciones mediante useQuery y useMutation.
Invalidación de caché después de modificar datos.
Navegación mediante React Router.
Componentes reutilizables y tipados con TypeScript.
Comunicación entre frontend y backend mediante una API REST.