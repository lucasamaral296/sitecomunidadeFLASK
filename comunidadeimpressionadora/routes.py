from flask import render_template, request, redirect, flash, url_for
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user

lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda']


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # exibir msg de 'login' com sucesso
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            # redirecionar para a homepage
            return redirect(url_for('home'))
        else:
            flash('Falha no Login, E-mail ou senha incorretos.', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        # criar Usuario
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        # adicionar a sessao
        database.session.add(usuario)
        # commit na sessao
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/sair')
def sair():
    logout_user()
    flash('Logout feito com sucesso.', 'alert-success')
    return redirect((url_for('home')))


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/post/criar')
def criar_post():
    return render_template('criarpost.html')


