from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda']

app.config['SECRET_KEY'] = '6037c3d29cc427f4051a2521ea3adf25168c7b44057fa953'

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
