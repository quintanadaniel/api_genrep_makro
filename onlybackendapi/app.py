from flask import Flask
from flask import request, jsonify, render_template, request
################################################################
from config.database import OracleDB
################################################################
from modules.clientes.cliente import customers
################################################################
from modules.profimetrics.profi import profi
from modules.profimetrics.prof_logs import get_prof_log
from modules.profimetrics.prof_1701_hosp import get_prof_1701_hosp
from modules.profimetrics.prof_1703_hosp import get_prof_1703_hosp
from modules.profimetrics.prof_1704_hosp import get_prof_1704_hosp
from modules.profimetrics.prof_1716_hosp import get_prof_1716_hosp
################################################################
from modules.sistemas.nightrunho import nr_status
from modules.sistemas.nightrunbdoho import nr_status_bdoho
from modules.sistemas.mafis_mk import get_mafismk
from modules.sistemas.mafis_bdoho import get_mafisbdo
from modules.sistemas.mafis_log_mk import mafismklog
from modules.sistemas.mafis_log_bdoho import mafisbdolog
################################################################
from modules.rep300.mkho300 import get_mkho300
################################################################
from modules.pedidos.pedido_sin_sid import ocSinSid
################################################################
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

##################################################
# API para los procesos de MAFIS makro y Basualdo#
##################################################

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

########################################
# API para los procesos de Profimetrics#
########################################

@app.route('/profimetrics/', methods=['GET'])
def profimet():
    l_profi = profi()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi = l_profi
    print (jsonObjProfi)
    return jsonObjProfi

@app.route('/profimkhologs/', methods=['GET'])
def get_profi_mkho_log():
    l_profi_mkho_log = get_prof_log()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi_mkho_log = l_profi_mkho_log
    print (jsonObjProfi_mkho_log)
    return jsonObjProfi_mkho_log

@app.route('/profmk1701hosp/', methods=['GET'])
def get_profi_1701_hosp_mkho():
    l_profi1701_hosp = get_prof_1701_hosp()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi_1701_hosp = l_profi1701_hosp
    print (jsonObjProfi_1701_hosp)
    return jsonObjProfi_1701_hosp

@app.route('/profmk1703hosp/', methods=['GET'])
def get_profi_1703_hosp_mkho():
    l_profi1703_hosp = get_prof_1703_hosp()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi_1703_hosp = l_profi1703_hosp
    print (jsonObjProfi_1703_hosp)
    return jsonObjProfi_1703_hosp

@app.route('/profmk1704hosp/', methods=['GET'])
def get_profi_1704_hosp_mkho():
    l_prof_1704_hosp = get_prof_1704_hosp()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi_1704_hosp = l_prof_1704_hosp
    print (jsonObjProfi_1704_hosp)
    return jsonObjProfi_1704_hosp

@app.route('/profmk1716hosp/', methods=['GET'])
def get_profi_1716_hosp_mkho():
    l_profi_1716_hosp = get_prof_1716_hosp()
    #return render_template('profimetrics.html', profi1 = l_profi)
    jsonObjProfi_1716_hosp = l_profi_1716_hosp
    print (jsonObjProfi_1716_hosp)
    return jsonObjProfi_1716_hosp

####################################
# API para los procesos de sistemas#
####################################

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

#################################################################
# API para los procesos de los reportes del 300 makro y basualdo#
#################################################################

@app.route('/mkho300/', methods=['GET'])
def get_mkho_300():
    l_mkho300 = get_mkho300()
    print (l_mkho300)
    #return render_template('nrstatusbdoho.html', nrst_bdoho1 = l_nrst_bdoho)
    jsonObjNrmkho300 = l_mkho300
    print(jsonObjNrmkho300)
    return jsonObjNrmkho300

#################################################################
# API para los procesos de pedidos u ordenes de compra Logistica#
#################################################################

@app.route('/pedsinsid/', methods=['GET'])
def getOcSinSid():
    l_ocsinsid = ocSinSid()
    print (l_ocsinsid)
    #return render_template('ocsinsid.html', ocsinsid = l_ocsinsid)
    jsonObjOcSinSid = l_ocsinsid
    print(jsonObjOcSinSid)
    return jsonObjOcSinSid


#################################################################
@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5500,debug=True)