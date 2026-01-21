"""
Script para crear la estructura inicial del proyecto MercaSMART
Ejecutar desde la raíz del proyecto: python setup_project.py
"""

import os

# Estructura de carpetas y archivos
structure = {
    "backend": {
        "app": {
            "api": {
                "endpoints": {
                    "__init__.py": "",
                },
                "__init__.py": "",
            },
            "models": {
                "__init__.py": "",
            },
            "services": {
                "__init__.py": "",
            },
            "core": {
                "__init__.py": "",
                "config.py": "# Configuración de la aplicación\n",
            },
            "__init__.py": "",
            "main.py": """from fastapi import FastAPI

app = FastAPI(title="MercaSMART API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a MercaSMART API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
""",
        },
        "tests": {
            "__init__.py": "",
        },
        "requirements.txt": """fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
pydantic==2.5.3
pydantic-settings==2.1.0
python-dotenv==1.0.0
""",
        ".env.example": """DATABASE_URL=postgresql://user:password@localhost:5432/mercasmart
SECRET_KEY=your-secret-key-here
DEBUG=True
""",
        "README.md": """# MercaSMART Backend

API REST desarrollada con FastAPI para la aplicación MercaSMART.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: http://localhost:8000
Documentación automática en: http://localhost:8000/docs
""",
    },
    "mobile": {
        "README.md": """# MercaSMART Mobile

Aplicación móvil desarrollada con React Native.

## Instalación

```bash
npm install
```

## Ejecutar

```bash
# Android
npm run android

# iOS
npm run ios
```
""",
    },
    "docs": {
        "architecture.md": """# Arquitectura MercaSMART

## Visión General

MercaSMART es una aplicación que ayuda a optimizar las compras del mercado
comparando precios entre diferentes supermercados.

## Componentes

1. **Backend API**: FastAPI (Python)
2. **Base de Datos**: PostgreSQL
3. **Mobile App**: React Native
4. **Scraping**: Módulos Python (futura implementación)

## Flujo de Datos

Usuario → App Mobile → API REST → PostgreSQL
""",
        "api-spec.md": """# Especificación de API

## Endpoints Planeados

### Supermercados
- GET /api/supermercados - Listar todos
- POST /api/supermercados - Crear nuevo
- GET /api/supermercados/{id} - Obtener uno
- PUT /api/supermercados/{id} - Actualizar
- DELETE /api/supermercados/{id} - Eliminar

### Productos
- GET /api/productos
- POST /api/productos
- GET /api/productos/{id}
- PUT /api/productos/{id}
- DELETE /api/productos/{id}

### Precios
- GET /api/precios
- POST /api/precios
- GET /api/precios/producto/{producto_id}

### Listas de Mercado
- GET /api/listas
- POST /api/listas
- GET /api/listas/{id}
- POST /api/listas/{id}/optimizar
""",
        "development-guide.md": """# Guía de Desarrollo

## Convenciones de Código

### Python (Backend)
- Usar snake_case para variables y funciones
- Usar PascalCase para clases
- Máximo 88 caracteres por línea (Black formatter)

### JavaScript (Mobile)
- Usar camelCase para variables y funciones
- Usar PascalCase para componentes React
- Usar Prettier para formateo

## Git Workflow

1. Crear branch desde develop: `git checkout -b feature/nombre`
2. Hacer commits descriptivos
3. Push y crear Pull Request
4. Revisar y mergear a develop

## Testing

- Backend: pytest
- Mobile: Jest
""",
    },
    ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
*.egg-info/
.pytest_cache/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.expo/
.expo-shared/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite
""",
    "README.md": """# 🛒 MercaSMART

Aplicación inteligente para optimizar tus compras del mercado comparando precios entre supermercados.

## 🎯 Objetivo

Ayudar a las familias a ahorrar dinero sugiriendo dónde comprar cada producto según el mejor precio,
evitando viajes innecesarios entre supermercados.

## 🏗️ Estructura del Proyecto

```
MercaSMART/
├── backend/          # API REST en Python (FastAPI)
├── mobile/           # App móvil en React Native
├── docs/             # Documentación técnica
└── README.md
```

## 🚀 Roadmap

- [x] Setup inicial del proyecto
- [ ] CRUD de Supermercados (Backend)
- [ ] CRUD de Productos (Backend)
- [ ] CRUD de Precios (Backend)
- [ ] Algoritmo de optimización
- [ ] App móvil básica
- [ ] Historial de precios
- [ ] Scraping automático

## 👥 Equipo

Desarrollado con ❤️ para optimizar las compras familiares.

## 📄 Licencia

Privado - Todos los derechos reservados.
""",
    "LICENSE": """MIT License

Copyright (c) 2025 MercaSMART

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
}

def create_structure(base_path, structure):
    """Crea recursivamente la estructura de carpetas y archivos"""
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        if isinstance(content, dict):
            # Es una carpeta
            os.makedirs(path, exist_ok=True)
            print(f"📁 Creada carpeta: {path}")
            create_structure(path, content)
        else:
            # Es un archivo
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 Creado archivo: {path}")

if __name__ == "__main__":
    print("🚀 Creando estructura del proyecto MercaSMART...\n")
    
    # Obtener la ruta actual
    current_dir = os.getcwd()
    print(f"📍 Directorio actual: {current_dir}\n")
    
    # Crear la estructura
    create_structure(current_dir, structure)
    
    print("\n✅ ¡Estructura creada exitosamente!")
    print("\n📋 Próximos pasos:")
    print("1. Revisa los archivos creados en VS Code")
    print("2. Lee el README.md principal")
    print("3. Instala las dependencias del backend:")
    print("   cd backend")
    print("   pip install -r requirements.txt")