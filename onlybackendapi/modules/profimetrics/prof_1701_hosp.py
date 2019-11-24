from onlybackendapi.config.database import OracleDB
from flask import jsonify

def get_prof_1701_hosp():
    sqlstr = """select batch_id,error_ind||' - '||(SELECT rv_meaning FROM CG_REF_CODES WHERE RV_DOMAIN = 'PROF_ERROR' and rv_low_value = a.error_ind) error_ind,product_id,store_id,approved_price,approved_date,effective_date,due_date,offer_id,price_type,prc_attr_01_no,prc_attr_02_no,prc_attr_03_no,prc_attr_04_no,prc_attr_05_no,prc_attr_06_no,prc_attr_01_char,prc_attr_02_char,prc_attr_03_char,prc_attr_04_char,prc_attr_05_char,prc_attr_06_char,prc_attr_01_flag,prc_attr_02_flag,prc_attr_03_flag,prc_attr_04_flag,prc_attr_05_flag,prc_attr_06_flag,origin_id,create_user_id
                from
                prof_1701_hosp a
                where batch_id in (select batch_id
                                    from mkstg_etl_ctrl_status@stage_profi
                                    where rundate in (select run_date from nightrun)
                                    and interface_group not in ('TRANSFER','ORDERS')
                                    and origin_id = 1)"""
    ora = OracleDB().connect()
    res = ora.execute(sqlstr)
    payload_prof_1701_hosp = []
    context_prof_1701_hosp = {}
    for data_prof1701log in res:
        context_prof_1701_hosp = {'batch_id': data_prof1701log[0],'error_ind': data_prof1701log[1],'product_id': data_prof1701log[2],'store_id': data_prof1701log[3],'approved_price': data_prof1701log[4],'approved_date': data_prof1701log[5],'effective_date': data_prof1701log[6],'due_date': data_prof1701log[7],'offer_id': data_prof1701log[8],'price_type': data_prof1701log[9],'prc_attr_01_no': data_prof1701log[10],'prc_attr_02_no': data_prof1701log[11],'prc_attr_03_no': data_prof1701log[12],'prc_attr_04_no': data_prof1701log[13],'prc_attr_05_no': data_prof1701log[14],'prc_attr_06_no': data_prof1701log[15],'prc_attr_01_char': data_prof1701log[16],'prc_attr_02_char': data_prof1701log[17],'prc_attr_03_char': data_prof1701log[18],'prc_attr_04_char': data_prof1701log[19],'prc_attr_05_char': data_prof1701log[20],'prc_attr_06_char': data_prof1701log[21],'prc_attr_01_flag': data_prof1701log[22],'prc_attr_02_flag': data_prof1701log[23],'prc_attr_03_flag': data_prof1701log[24],'prc_attr_04_flag': data_prof1701log[25],'prc_attr_05_flag': data_prof1701log[26],'prc_attr_06_flag': data_prof1701log[27],'origin_id': data_prof1701log[28],'create_user_id': data_prof1701log[29] }
        payload_prof_1701_hosp.append(context_prof_1701_hosp)
        context_prof_1701_hosp = {}
    return jsonify(payload_prof_1701_hosp)