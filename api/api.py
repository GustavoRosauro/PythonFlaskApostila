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
    cur.execute('SELECT * FROM ALUNO')
    data = cur.fetchall()
    cur.close()
    response = Response(json.dumps(data), mimetype="application/json")
    return response

app.run(debug=True)