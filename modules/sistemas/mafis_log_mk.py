from config.database import OracleDB
from flask import jsonify

def mafismklog():
    sqlString = """select source,attribute1,global_attribute_category,accounting_date,reg_proc,created_date,month_date,proc_num from
                    MAFIS_STAGE
                    where source <> 'MK_AR_RECIBOS'
                    and trunc(created_date) = trunc(sysdate)
                    order by created_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload_mafismkholog = []
    content_mafismkholog = {}
    for data_mafismkholog in res:
        content_mafismkholog = {'source': data_mafismkholog[0],'attribute1': data_mafismkholog[1],'global_attribute_category': data_mafismkholog[2],'accounting_date': data_mafismkholog[3],'reg_proc': data_mafismkholog[4],'created_date': data_mafismkholog[5],'month_date': data_mafismkholog[6],'proc_num': data_mafismkholog[7] }
        payload_mafismkholog.append(content_mafismkholog)
        content_mafismkholog = {}
    return jsonify(payload_mafismkholog)