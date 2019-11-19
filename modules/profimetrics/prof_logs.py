from config.database import OracleDB
from flask import jsonify

def get_prof_log():
    sqlstr = """select rundate,a.batch_id batch_id,prog_name,seq_no,text
                from
                prof_1703_hosp
                where batch_id in (select batch_id
                                    from mkstg_etl_ctrl_status@stage_profi
                                    where rundate in (select run_date from nightrun)
                                    and interface_group not in ('TRANSFER','ORDERS')
                                    and origin_id = 1)"""
    ora = OracleDB().connect()
    res = ora.execute(sqlstr)
    payload_prof_log = []
    context_prof_log = {}
    for data_proflog in res:
        context_prof_log = {'rundate': data_proflog[0],'batch_id': data_proflog[1],'prog_name': data_proflog[2],'seq_no': data_proflog[3],'text': data_proflog[4] }
        payload_prof_log.append(context_prof_log)
        context_prof_log = {}
    return jsonify(payload_prof_log)