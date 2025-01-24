# Importando Blueprint
from flask import Blueprint, render_template, g, request, redirect, url_for
from todor.auth import login_required  # <-- Importar login_required
from .models import Todo, User # <-- Importar modelos
from todor import db  # <-- Importar la base de datos

# Creando instancia
bp = Blueprint('todo', __name__, url_prefix='/todo')

# Creando ruta y función
@bp.route('/list')
@login_required  # <-- Decorador
def index():
    todos = Todo.query.all()  # <-- Obtener todas las tareas
    return render_template('todo/index.html', todos=todos)  # <-- Pasar las tareas a la plantilla

@bp.route('/create', methods=('GET', 'POST'))  # Añadir métodos GET y POST
@login_required  # Decorador
def create():
    if request.method == 'POST':  # Si la petición es POST
        title = request.form['title']  # Obtener el título del formulario
        desc = request.form['desc']  # Obtener la descripción del formulario
        todo = Todo(g.user.id, title, desc)  # Crear una nueva tarea
        db.session.add(todo)  # Añadir la tarea a la base de datos
        db.session.commit()  # Guardar los cambios en la base de datos
        return redirect(url_for('todo.index'))  # Redirigir a la página principal de tareas

    return render_template('todo/create.html')  # Si la petición es GET, mostrar el formulario

@bp.route('/update/<int:id>', methods=('GET', 'POST'))  # <-- Nueva ruta para actualizar
@login_required
def update(id):
    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False
        db.session.commit()
        return redirect(url_for('todo.index'))

    return render_template('todo/update.html', todo=todo)

@bp.route('/delete/<int:id>')  # <-- Nueva ruta para eliminar
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo