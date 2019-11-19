from config.database import OracleDB
from flask import jsonify

def nr_status():
    sqlString = """select run_date,store_no,prog_name,log_name,start_date,end_date,exit_code
                   from nr_status
                   where run_date in (select run_date from nightrun)
                   order by start_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload_nr_mkho = []
    context_nr_mkho = {}
    for data_nr_mkho in res:
        context_nr_mkho = {'run_date': data_nr_mkho[0],'store_no': data_nr_mkho[1],'prog_name': data_nr_mkho[2],'log_name': data_nr_mkho[3],'start_date': data_nr_mkho[4],'end_date': data_nr_mkho[5],'exit_code': data_nr_mkho[6]}
        payload_nr_mkho.append(context_nr_mkho)
        context_nr_mkho ={}
    return jsonify(payload_nr_mkho)