from config.database_bdo import OracleDB_bdoho
from flask import jsonify

def get_mafisbdo():
    sqlString = """select run_date,ctry_name,proc_name,proc_type,status,src_start_date,src_end_date,etl_start_date,etl_end_date,trg_start_date,trg_end_date from
                    msa_etl_ctrl_status@stage
                    where (run_date = trunc(sysdate) or run_date = (select run_date from nightrun))
                    order by src_start_date desc,etl_start_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    payload_mafisbdo = []
    context_mafisbdo = {}
    for data_mafisbdo in res:
        contaxt_mafisbdo = {'run_date': data_mafisbdo[0],'ctry_name': data_mafisbdo[1],'proc_name': data_mafisbdo[2],'proc_type': data_mafisbdo[3],'status': data_mafisbdo[4],'src_start_date': data_mafisbdo[5],'src_end_date': data_mafisbdo[6],'etl_start_date': data_mafisbdo[7],'etl_end_date': data_mafisbdo[8],'trg_start_date': data_mafisbdo[9],'trg_end_date': data_mafisbdo[10]}
        payload_mafisbdo.append(context_mafisbdo)
        context_mafisbdo = {}
    return jsonify(payload_mafisbdo)