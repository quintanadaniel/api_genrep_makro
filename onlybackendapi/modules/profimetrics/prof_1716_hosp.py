from onlybackendapi.config.database import OracleDB
from flask import jsonify

def get_prof_1716_hosp():
    sqlstr = """select batch_id,error_ind||' - '||(select rv_meaning from cg_ref_codes where rv_domain = 'PROF_ERROR' and rv_low_value = a.error_ind) error_ind,offer_id,sku_id,qty,offer_list_flag,val_type,val,publish_price,promo_price,pz_id,review_comments,price_relation_group,nb_conditional_group_id,nb_publish_sku_desc,nb_page_num,nb_possible_pages,nb_exclude_from_offer,nb_super_offer_flag,nb_daily_offer_flag,nb_pv_flag,nb_pv_factor,nb_pv_price,nb_unit_prc_flag,nb_unit_prc_value,nb_unit_prc_te,nb_unit_prc_pack_size,nb_unit_prc_uom,nb_uplift_sls_qty,nb_uplift_sls_val,nb_own_brand_flag,offer_product_attr_01_char,offer_product_attr_02_char,offer_product_attr_03_char,offer_product_attr_04_char,origin_id,record_status,create_user_id,create_datetime,last_update_user_id,last_update_datetime
                from
                prof_1716_hosp a
                where batch_id in (select batch_id
                                    from mkstg_etl_ctrl_status@stage_profi
                                    where rundate in (select run_date from nightrun)
                                    and interface_group not in ('TRANSFER','ORDERS')
                                    and origin_id = 1)"""
    ora = OracleDB().connect()
    res = ora.execute(sqlstr)
    payload_prof_1716_hosp = []
    context_prof_1716_hosp = {}
    for data_prof1716hosp in res:
        context_prof_1716_hosp = {'batch_id': data_prof1716hosp[0],'error_ind': data_prof1716hosp[1],'offer_id': data_prof1716hosp[2],'sku_id': data_prof1716hosp[3],'qty': data_prof1716hosp[4],'offer_list_flag': data_prof1716hosp[5],'val_type': data_prof1716hosp[6],'val': data_prof1716hosp[7],'publish_price': data_prof1716hosp[8],'promo_price': data_prof1716hosp[9],'pz_id': data_prof1716hosp[10],'review_comments': data_prof1716hosp[11],'price_relation_group': data_prof1716hosp[12],'nb_conditional_group_id': data_prof1716hosp[13],'nb_publish_sku_desc': data_prof1716hosp[14],'nb_page_num': data_prof1716hosp[15],'nb_possible_pages': data_prof1716hosp[16],'nb_exclude_from_offer': data_prof1716hosp[17],'nb_super_offer_flag': data_prof1716hosp[18],'nb_daily_offer_flag': data_prof1716hosp[19],'nb_pv_flag': data_prof1716hosp[20],'nb_pv_factor': data_prof1716hosp[21],'nb_pv_price': data_prof1716hosp[22],'nb_unit_prc_flag': data_prof1716hosp[23],'nb_unit_prc_value': data_prof1716hosp[24],'nb_unit_prc_te': data_prof1716hosp[25],'nb_unit_prc_pack_size': data_prof1716hosp[26],'nb_unit_prc_uom': data_prof1716hosp[27],'nb_uplift_sls_qty': data_prof1716hosp[28],'nb_uplift_sls_val': data_prof1716hosp[29],'nb_own_brand_flag': data_prof1716hosp[30],'offer_product_attr_01_char': data_prof1716hosp[31],'offer_product_attr_02_char': data_prof1716hosp[32],'offer_product_attr_03_char': data_prof1716hosp[33],'offer_product_attr_04_char': data_prof1716hosp[34],'origin_id': data_prof1716hosp[35],'record_status': data_prof1716hosp[36],'create_user_id': data_prof1716hosp[37],'create_datetime': data_prof1716hosp[38],'last_update_user_id': data_prof1716hosp[39],'last_update_datetime': data_prof1716hosp[40] }
        payload_prof_1716_hosp.append(context_prof_1716_hosp)
        context_prof_1716_hosp = {}
    return jsonify(payload_prof_1716_hosp)