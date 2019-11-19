from config.database import OracleDB
from flask import jsonify

def get_prof_1704_hosp():
    sqlstr = """select batch_id,error_ind,offer_id,store_id,pz_group_id,origin_id,record_status,create_user_id,create_datetime,last_update_user_id,last_update_datetime
                from
                prof_1704_hosp
                where batch_id in (select batch_id
                                    from mkstg_etl_ctrl_status@stage_profi
                                    where rundate in (select run_date from nightrun)
                                    and interface_group not in ('TRANSFER','ORDERS')
                                    and origin_id = 1)"""
    ora = OracleDB().connect()
    res = ora.execute(sqlstr)
    payload_prof_1704_hosp = []
    context_prof_1704_hosp = {}
    for data_prof1704log in res:
        context_prof_1704_hosp = {'batch_id': data_prof1704log[0],'error_ind': data_prof1704log[1],'offer_id': data_prof1704log[2],'store_id': data_prof1704log[3],'pz_group_id': data_prof1704log[4],'origin_id': data_prof1704log[5],'record_status': data_prof1704log[6],'create_user_id': data_prof1704log[7],'create_datetime': data_prof1704log[8],'last_update_user_id': data_prof1704log[8],'last_update_datetime': data_prof1704log[8] }
        payload_prof_1704_hosp.append(context_prof_1704_hosp)
        context_prof_1704_hosp = {}
    return jsonify(payload_prof_1704_hosp)