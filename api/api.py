import json

from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'apex'
mysql = MySQL(app)
cors = CORS(app, resources={"*": {"origins": "*"}})
@app.route('/', methods=['get'])
def home():
    cur = mysql.connect.cursor()
    listaP = list()
    cur.execute('SELECT * FROM ALUNO')
    data = cur.fetchall()
    for pessoa in data:
        p = {
            "id": pessoa[0],
            "nome": pessoa[1],
            "idade": pessoa[2]
        }
        listaP.append(p)
    cur.close()
    response = Response(json.dumps(listaP), mimetype="application/json")
    return response


@app.route('/', methods=['post'])
def inserir():
    db = mysql.connect
    cur = db.cursor()
    dados = (request.json['nome'], request.json['idade'])
    sqlInsert = "INSERT INTO ALUNO (NOME,IDADE) values (%s, %s)"
    cur.execute(sqlInsert, dados)
    db.commit()
    return jsonify("inserido com sucesso")

@app.route('/<int:id>',methods=['delete'])
def deletar(id):
    db = mysql.connect
    cur = db.cursor()
    sqlDelete = "DELETE FROM ALUNO WHERE ID ="+str(id)
    cur.execute(sqlDelete)
    db.commit()
    return jsonify("removido com sucesso !")

@app.route('/<int:id>', methods=['put'])
def editar(id):
    db = mysql.connect
    cur = db.cursor()
    dados = (request.json['nome'], request.json['idade'])
    sqlUpdate = "update aluno set nome = %s, idade = %s where id ="+str(id)
    cur.execute(sqlUpdate, dados)
    db.commit()
    return jsonify("Alterado com sucesso!!")


app.run(debug=True)