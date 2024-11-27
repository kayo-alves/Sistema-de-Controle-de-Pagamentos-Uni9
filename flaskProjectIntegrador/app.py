
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
    global logado
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


@app.route('/LedaLog/Pagamento', methods=['POST', 'GET'])
def pagamento():
    global logado
    if logado == True:

        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()
            cursor.execute('select f.id_funcionario, f.nome, c.salario, c.id_cargo, c.nome as nome_cargo from funcionario f inner join cargo c on f.id_cargo = c.id_cargo order by f.id_funcionario;')
            listapagamento = cursor.fetchall()


        return render_template('Pagamentos.html', listapagamento=listapagamento)
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

@app.route('/pagamentos', methods=['POST', 'GET'])
def pagamentos():
    global logado

    # Obtendo os dados do formulário
    id_funcionario = request.form.get('ID Funcionário')
    pagamento_total = request.form.get('Pagamento Total')
    desconto = request.form.get('Desconto')
    dt_pagamento = request.form.get('dt_pagamento')
    hora_extra = request.form.get('hora_extra')

    # Verificações para garantir que os campos não estão vazios
    if not all([id_funcionario, pagamento_total, desconto, dt_pagamento, hora_extra]):
        flash("Todos os campos são obrigatórios.", "danger")
        return redirect('/pagamentos')

    try:
        pagamento_total = float(pagamento_total)  # Convertendo para float
        desconto = float(desconto)  # Convertendo para float
        hora_extra = int(hora_extra)  # Convertendo para inteiro
    except ValueError:
        flash("Por favor, insira valores válidos para pagamento, desconto e hora extra.", "danger")
        return redirect('/pagamentos')

    # Cálculo do pagamento final
    hora_normal = pagamento_total / 220  # O valor da hora normal (considerando 220 horas no mês)
    valor_hora_extra = hora_normal * 1.5  # O valor da hora extra é 1,5 vezes o valor da hora normal
    pagamento_final = (pagamento_total - desconto) +  (hora_extra * valor_hora_extra) # Subtrai o desconto e adiciona o valor das horas extras

    # Arredondando para 2 casas decimais antes de enviar para o banco
    pagamento_final = round(pagamento_final, 2)
    desconto = round(desconto, 2)

    # Converter as horas extras para o formato TIME (HH:MM:00)
    hora_extra_formatada = f"{hora_extra}:00:00"

    try:
        # Conectando ao banco de dados
        conect_BD = mysql.connector.connect(host='localhost', database='meu_banco', user='root', password='')

        if conect_BD.is_connected():
            cursor = conect_BD.cursor()

            # Comando para inserir os dados no banco de dados
            cursor.execute(f"INSERT INTO pagamento (hora_extra, data_pag, pag_total, id_funcionario, desconto) "
                           f"VALUES ('{hora_extra_formatada}', '{dt_pagamento}', '{pagamento_final}', '{id_funcionario}', '{desconto}');")

            # Commit e fechamento de conexão
            conect_BD.commit()
            cursor.close()
            conect_BD.close()
            flash("Funcionário cadastrado com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao cadastrar funcionário: {e}", "danger")

    logado = True
    return redirect('/LedaLog/Pagamento')
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
