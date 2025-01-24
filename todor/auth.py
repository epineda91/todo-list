@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user == None:
            error = "Nombre de usuario incorrecto"
        elif not check_password_hash(user.password, password):
            error = "Contraseña incorrecta"

        if error == None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))

        flash(error)

    return render_template('auth/login.html')