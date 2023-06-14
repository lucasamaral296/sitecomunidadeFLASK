from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Meu site esta no ar!</p>"

@app.route('/contato')
def contato():
    return 'Qualquer duvida entre em contato'


if __name__ == "__main__":
    app.run(debug=True)
