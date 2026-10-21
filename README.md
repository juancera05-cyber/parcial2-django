# Parcial 2 - Django Backend

Sistema para gestionar proyectos y sus tareas, hecho con Django nativo y SQLite.
Curso: Desarrollo de aplicaciones Web I -- 4E.

## Estructura

- `parcial2/` configuración del proyecto (`gestion` está en `INSTALLED_APPS`).
- `gestion/models.py` modelos `Proyecto` y `Tarea` (una tarea pertenece a un proyecto, `ForeignKey` con `on_delete=models.CASCADE`).
- `gestion/admin.py` ambos modelos registrados en el administrador.
- `db.sqlite3` base de datos con 3 proyectos y 2 tareas por proyecto.
- `capturas/` lista de proyectos y lista de tareas en el administrador.

## Cómo ejecutarlo

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Entrar a http://127.0.0.1:8000/admin/ con las credenciales de `credenciales.txt`.
