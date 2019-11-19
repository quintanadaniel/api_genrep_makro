from config.database_bdo import OracleDB_bdoho
from flask import jsonify

def mafisbdolog():
    sqlString = """select source,attribute1,global_attribute_category,accounting_date,reg_proc,created_date,month_date,proc_num from
                    MAFIS_STAGE
                    where source <> 'MK_AR_RECIBOS'
                    and trunc(created_date) = trunc(sysdate)
                    order by created_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    payload_mafisbdoholog = []
    content_mafisbdoholog = {}
    for data_mafisbdoholog in res:
        content_mafisbdoholog = {'source': data_mafisbdoholog[0],'attribute1': data_mafisbdoholog[1],'global_attribute_category': data_mafisbdoholog[2],'accounting_date': data_mafisbdoholog[3],'reg_proc': data_mafisbdoholog[4],'created_date': data_mafisbdoholog[5],'month_date': data_mafisbdoholog[6],'proc_num': data_mafisbdoholog[7] }
        payload_mafisbdoholog.append(content_mafisbdoholog)
        content_mafisbdoholog = {}
    return jsonify(payload_mafisbdoholog)