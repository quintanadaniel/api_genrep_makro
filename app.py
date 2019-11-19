from flask import Flask
from flask import request, jsonify, render_template, request
from config.database import OracleDB
from modules.clientes.cliente import customers
from modules.sistemas.profi import profi
from modules.sistemas.nightrunho import nr_status
from modules.sistemas.nightrunbdoho import nr_status_bdoho
from modules.sistemas.mafis_mk import get_mafismk
from modules.sistemas.mafis_bdoho import get_mafisbdo
from modules.sistemas.mafis_log_mk import mafismklog
from modules.sistemas.mafis_log_bdoho import mafisbdolog
from modules.pedidos.pedido_sin_sid import ocSinSid
from modules.tiendas.tienda import store
import json

app=Flask(__name__)


@app.route('/')
def Index():
    #return 'Aplicacion conecta a Base de Datos'
    return render_template('index.html')


@app.route('/tiendas/', methods=['GET'])
def getStore():
    l_store = store()
    jsonObj = l_store
    print (jsonObj)
    return jsonObj

@app.route('/clientes/', methods=['GET'])
def getCustomers():
    l_cust = customers()
    return render_template('clientes.html', cust1 = l_cust)


@app.route('/mafismk/', methods=['GET'])
def get_mafis_mk():
    l_mafisMkho = get_mafismk()
    #return render_template('mafis_mk.html', mafismk1 = l_mafisMkho)
    jsonObjMafisMkho = l_mafisMkho
    print(jsonObjMafisMkho)
    return jsonObjMafisMkho

@app.route('/mafisbdoho/', methods=['GET'])
def get_mafis_bdoho():
    l_mafisbdoho = get_mafisbdo()
    #return render_template('mafis_bdoho.html', mafisbdoho1 = l_mafisbdoho)
    jsonObjMafisBdoho = l_mafisbdoho
    print(jsonObjMafisBdoho)
    return jsonObjMafisBdoho

@app.route('/mafismklog/', methods=['GET'])
def mafis_mk_log():
    l_mafisMK_log = mafismklog()
    #return render_template('mafismklogs.html', mafismklog1 = l_mafisMK_log)
    jsonObjMafisMkhoLogs = l_mafisMK_log
    print(jsonObjMafisMkhoLogs)
    return jsonObjMafisMkhoLogs

@app.route('/mafisbdoholog/', methods=['GET'])
def get_mafis_bdoho_log():
    l_mafisbdoho_log = mafisbdolog()
    #return render_template('mafisbdohologs.html', mafisbdoholog1 = l_mafisbdoho_log)
    jsonObjMafisBdohoLogs = l_mafisbdoho_log
    print(jsonObjMafisBdohoLogs)
    return jsonObjMafisBdohoLogs

@app.route('/profimetrics/', methods=['GET'])
def profimet():
    l_profi = profi()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi = l_profi
    print (jsonObjProfi)
    return jsonObjProfi

@app.route('/nrmkho/', methods=['GET'])
def getNr_mkho():
    l_nrst = nr_status()
    #return render_template('nrstatus.html', nrst1 = l_nrst)
    jsonObjNrMkho = l_nrst
    print(jsonObjNrMkho)
    return jsonObjNrMkho

@app.route('/nrstatusbdoho/', methods=['GET'])
def getNr_stat_bdoho():
    l_nrst_bdoho = nr_status_bdoho()
    print (l_nrst_bdoho)
    #return render_template('nrstatusbdoho.html', nrst_bdoho1 = l_nrst_bdoho)
    jsonObjNrBdoho = l_nrst_bdoho
    print(jsonObjNrBdoho)
    return jsonObjNrBdoho

@app.route('/pedsinsid/', methods=['GET'])
def getOcSinSid():
    l_ocsinsid = ocSinSid()
    print (l_ocsinsid)
    #return render_template('ocsinsid.html', ocsinsid = l_ocsinsid)
    jsonObjOcSinSid = l_ocsinsid
    print(jsonObjOcSinSid)
    return jsonObjOcSinSid

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5500,debug=True)