from config.database import OracleDB
from flask import jsonify

def profi():
    sqlString = """select origin_name,a.*
                    from mkstg_etl_ctrl_status@stage_profi a ,mkstg_interface_groups@stage_profi b
                    where a.interface_group = b.interface_group
                      and rundate in (select run_date from nightrun)
                      and a.interface_group not in ('TRANSFER','ORDERS')
                    order by 2 desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload_profi = []
    content_profi = {}
    for data_profi in res:
        content_profi = { 'origin_name': data_profi[0],'batch_id':data_profi[1],'rundate':data_profi[2],'origin_id':data_profi[3],'interface_group':data_profi[4],'load_start_date':data_profi[5],'load_end_date':data_profi[6],'status':data_profi[7],'upload_start_date':data_profi[8],'upload_end_date':data_profi[9] }
        payload_profi.append(content_profi)
        content_profi = {}
    return jsonify(payload_profi)
