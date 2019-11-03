from flask import Flask
from flask import request, jsonify, render_template, request
from config.database import OracleDB
from modules.clientes.cliente import customers
from modules.sistemas.profi import  profis
app=Flask(__name__)


@app.route('/')
def Index():
    #return 'Aplicacion conecta a Base de Datos'
    return render_template('index.html')


@app.route('/tiendas/', methods=['GET'])
def all_store():
    ora = OracleDB()
    ora.connect()
    ora.stores()
    l_res = ora.stores()
    print (l_res)
    return render_template('tiendas.html', store = l_res)
    #return l_res

@app.route('/clientes/', methods=['GET'])
def getCustomers():
    l_cust = customers()
    return render_template('clientes.html', cust1 = l_cust)


@app.route('/profimetrics/', methods=['GET'])
def profimet():
    l_profi = profis()
    return render_template('profimetrics.html', profi1 = l_profi)

@app.route('/nrstatus/', methods=['GET'])
def nr_stat():
    ora = OracleDB()
    ora.connect()
    ora.nr_status()
    l_nrst = ora.nr_status()
    print (l_nrst)
    return render_template('nrstatus.html', nrst1 = l_nrst)

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
    app.run(port=5500,debug=True)