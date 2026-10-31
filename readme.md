# 🎬 Sistema de Control de Películas

Un proyecto desarrollado en **Django** para la gestión y control de un catálogo de películas, integrado con base de datos relacional (compatible con MySQL/MariaDB) y un entorno de trabajo colaborativo mediante Git y GitHub.

---

## 📂 Estructura del Proyecto

```text
proyecto_peliculas/
│
├── app_peliculas/             # Aplicación principal de Django
│   ├── migrations/            # Historial de migraciones de la base de datos
│   ├── templates/             # Plantillas HTML (vistas del sistema)
│   │   └── app_peliculas/
│   │       └── lista_peliculas.html
│   ├── admin.py               # Configuración del panel de administración
│   ├── apps.py                # Configuración de la app
│   ├── models.py              # Definición de los modelos de datos
│   ├── urls.py                # Rutas específicas de la aplicación
│   └── views.py               # Lógica de vistas y procesamiento de formularios
│
├── proyecto_peliculas/        # Configuración global del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configuración general y de base de datos
│   ├── urls.py                # Rutas principales del proyecto
│   └── wsgi.py
│
├── venv/                      # Entorno virtual de Python (ignorado por Git)
└── manage.py                  # Script de gestión y comandos de Django
```

---

## 🚀 Requisitos Previos

Antes de ejecutar el proyecto en tu computadora, asegúrate de tener instalado:
* **Python** (versión 3.x recomendada)
* **Git**
* Un servidor de base de datos local como **MariaDB** o **MySQL**

---

## ⚙️ Configuración del Entorno Local (Paso a Paso)

Sigue estos pasos para clonar y poner en marcha el proyecto en tu equipo:

### 1. Clonar el repositorio
Abre tu terminal y clona el proyecto desde GitHub:
```bash
git clone https://github.com/ElSololobo2/proyecto_peliculas.git
cd proyecto_peliculas
```

### 2. Crear y activar el entorno virtual
* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
  *(Nota: Si PowerShell bloquea la activación, ejecuta una vez como Administrador: `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`)*

### 3. Instalar las dependencias
Con el entorno virtual activo (`(venv)`), instala Django y el conector de base de datos:
```powershell
pip install django mysqlclient
```

### 4. Configurar la Base de Datos
1. Abre tu gestor de base de datos (MariaDB/MySQL) y crea una base de datos vacía llamada `peliculas`:
   ```sql
   CREATE DATABASE peliculas;
   ```
2. Asegúrate de configurar las credenciales correctas en el archivo `proyecto_peliculas/settings.py` dentro de la sección `DATABases`.

### 5. Aplicar migraciones
Genera las tablas necesarias en tu base de datos ejecutando:
```powershell
python manage.py migrate
```

### 6. Ejecutar el servidor de desarrollo
Inicia el servidor local de Django:
```powershell
python manage.py runserver
```
Abre tu navegador y entra a: `http://127.0.0.1:8000/`

---

## 🔄 Guía rápida para Git (Trabajo en equipo)

Cada vez que realices cambios en el código y quieras subirlos para compartirlos con tu equipo, utiliza la siguiente secuencia en tu terminal:

```powershell
# 1. Verificar archivos modificados
git status

# 2. Agregar cambios
git add .

# 3. Guardar cambios localmente con un mensaje descriptivo
git commit -m "Descripción de los cambios realizados"

# 4. Enviar cambios a GitHub
git push origin main
```

Para descargar los cambios más recientes que haya subido tu compañero:
```powershell
git pull origin main
```