from config.database import OracleDB
from flask import jsonify

def ocSinSid():
    sqlString = """select oc,tda,transf,nro_art,descr,sal_tda80,ult_fec_sal,ent_tda,ent_ho,ult_fec_entr,sid_pend,cant_pend,cant_pend_ho,ped_tda,est_ped_tda,trf_tda,trf_desde_ped,valor from
                    t_sin_sid
                    order by tda,oc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload_ocsinsid = []
    context_ocsinsid = {}
    for data_oc_sin_sid in res:
        context_ocsinsid = {'oc': data_oc_sin_sid[0],'tda,transf': data_oc_sin_sid[1],'nro_art': data_oc_sin_sid[2],'descr': data_oc_sin_sid[3],'sal_tda80': data_oc_sin_sid[4],'ult_fec_sal': data_oc_sin_sid[5],'ent_tda': data_oc_sin_sid[6],'ent_ho': data_oc_sin_sid[7],'ult_fec_entr': data_oc_sin_sid[8],'sid_pend': data_oc_sin_sid[9],'cant_pend': data_oc_sin_sid[10],'cant_pend_ho': data_oc_sin_sid[11],'ped_tda': data_oc_sin_sid[12],'est_ped_tda': data_oc_sin_sid[13],'trf_tda': data_oc_sin_sid[14],'trf_desde_ped': data_oc_sin_sid[15],'valor': data_oc_sin_sid[16] }
        payload_ocsinsid.append(context_ocsinsid)
        context_ocsinsid = {}
    return jsonify(payload_ocsinsid)