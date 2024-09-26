from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ARTHURZIN'


@app.route('/', methods=['GET'])
def home():
    return render_template("Home.html")


@app.route('/login', methods=['GET','POST'])
def login():  # put application's code here
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        print(nome, senha)
        return redirect('/usuario')
    return render_template('Login.html')

@app.route('/usuario', methods=['GET'])
def usuario():
    return render_template('Usuario.html')


if __name__ == '__main__':
    app.run(debug=True)
