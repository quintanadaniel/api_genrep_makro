from config.database_bdo import OracleDB_bdoho
from flask import jsonify

def nr_status_bdoho():
    sqlString = """select run_date,store_no,prog_name,log_name,start_date,end_date,exit_code
                   from nr_status
                   where run_date in (select run_date from nightrun)
                   order by start_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    payload_nr_bdoho = []
    context_nr_bdoho = {}
    for data_nr_bdoho in res:
        context_nr_bdoho = {'run_date': data_nr_bdoho[0],'store_no': data_nr_bdoho[1],'prog_name': data_nr_bdoho[2],'log_name': data_nr_bdoho[3],'start_date': data_nr_bdoho[4],'end_date': data_nr_bdoho[5],'exit_code': data_nr_bdoho[6]}
        payload_nr_bdoho.append(context_nr_bdoho)
        context_nr_bdoho ={}
    return jsonify(payload_nr_bdoho)