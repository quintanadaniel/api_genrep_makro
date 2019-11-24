from config.database import OracleDB
from flask import jsonify

def get_mafismk():
    sqlString = """select run_date,ctry_name,proc_name,proc_type,status,src_start_date,src_end_date,etl_start_date,etl_end_date,trg_start_date,trg_end_date from
                    msa_etl_ctrl_status@stage
                    where (run_date = trunc(sysdate) or run_date = (select run_date from nightrun))
                    order by src_start_date desc,etl_start_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload_mafismk = []
    context_mafismk = {}
    for data_mafismk in res:
        context_mafismk = {'run_date': data_mafismk[0],'ctry_name': data_mafismk[1],'proc_name': data_mafismk[2],'proc_type': data_mafismk[3],'status': data_mafismk[4],'src_start_date': data_mafismk[5],'src_end_date': data_mafismk[6],'etl_start_date': data_mafismk[7],'etl_end_date': data_mafismk[8],'trg_start_date': data_mafismk[9],'trg_end_date': data_mafismk[10]}
        payload_mafismk.append(context_mafismk)
        context_mafismk = {}
    return jsonify(payload_mafismk)