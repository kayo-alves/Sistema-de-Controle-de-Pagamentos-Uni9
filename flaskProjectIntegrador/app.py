from operator import truediv
from flask import Flask, render_template, redirect, request, flash, get_flashed_messages
import mysql.connector


logado = True
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ARTHURZIN'


@app.route('/', methods=['GET'])
def home():
    global logado
    logado = False
    return render_template("index.html")


@app.route('/login', methods=['GET','POST'])
def login():  # put application's code here
    global logado
    logado = False
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        if nome == "Ledalog" and senha == "123456":
            logado = True
            return redirect("/LedaLog")
        else:
            flash('USUARIO OU SENHA INCORRETO')
            return redirect("/login")


    return render_template('Login.html')

@app.route('/LedaLog', methods=['GET'])
def usuario():
    if logado == True:

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select * from funcionario;')
            usuarios = cursor.fetchall()

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select * from empresa where id_emp= 120;')
            empresa = cursor.fetchall()

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select c.id_cargo, c.nome, f.nome, id_funcionario, c.salario from  cargo c inner join funcionario f on c.id_cargo = f.id_cargo;')
            cargo = cursor.fetchall()

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select * from departamento;')
            departamento = cursor.fetchall()

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select fd.id_funcionario, f.nome, fd.id_depart, d.nome as nome_departamento, fd.data_locacao, fd.data_saida from funcionario_departamento fd inner join funcionario f on fd.id_funcionario = f.id_funcionario inner join departamento d on d.id_depart = fd.id_depart;')
            funcionario_departamento = cursor.fetchall()

        return render_template('LedaLog.html', usuarios=usuarios, empresa=empresa, cargo=cargo, departamento=departamento, funcionario_departamento=funcionario_departamento)
    if logado == False:
        return redirect("/login")

@app.route('/cadastrarFuncionario', methods=['POST', 'GET'])
def cadastrarFuncionario():
    global logado

    nome = request.form.get('nome')
    CPF = request.form.get('CPF')
    endereco = request.form.get('endereco')
    dt_contratacao = request.form.get('dt_contratacao')
    id_cargo = int(request.form.get('id_cargo')) if request.form.get('id_cargo') else None
    id_empresa = int(request.form.get('id_empresa')) if request.form.get('id_empresa') else None

    print(
        f"Dados recebidos: nome={nome}, CPF={CPF}, endereco={endereco}, dt_contratacao={dt_contratacao}, id_cargo={id_cargo}, id_empresa={id_empresa}")

    try:
        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute(f"insert into funcionario values (default, '{nome}','{CPF}', '{endereco}', '{dt_contratacao}', '{id_cargo}', '{id_empresa}');")


            cursor.close()
            conect_BD.close()
            flash("Funcionário cadastrado com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao cadastrar funcionário: {e}", "danger")

    logado = True
    return redirect('/LedaLog?aba=cadastrarFuncionario')

@app.route('/excluirFuncionario', methods=['POST'])
def excluirFuncionario():
    global logado

    usuarioID= request.form.get('usuarioExcluir')

    conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

    if conect_BD.is_connected():
        cursor = conect_BD.cursor()
        cursor.execute(f"delete from funcionario where id_funcionario='{usuarioID}';")

    if conect_BD.is_connected():
        cursor.close()
        conect_BD.close()


    logado = True
    return redirect('/LedaLog?aba=cadastrarFuncionario')





# with open('usuario.json') as usuariosTemp:
#     usuarios = json.load(usuariosTemp)
# cont=0
# for usuario in usuarios:
#     cont += 1
#     if nome == ''
#     if usuario['nome'] == nome and usuario['senha'] == senha:
#         return redirect("/usuario")
#
# if cont >=len(usuarios):
#     flash('USUARIO OU SENHA INCORRETO')
#     return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)
