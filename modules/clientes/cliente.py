from flask import Flask
from flask import request, jsonify, render_template, request
from config.database import OracleDB


def customers():
    l_cust = cust()
    print (l_cust)
    return l_cust

def cust():
    sqlString = """"SELECT STORE_NO, CUST_NO, CUST_TYPE_NO, CARD_TYPE_NO, DIS_NO,
                            STORE_UPD, CUST_CHECK_DIG, STATUS, REG_DATE, USERID, NAME,
                            ADDRESS, TOWN, NBR_MMAIL, IND_CHEQUES, EXP_DATE, LAST_MUT_DATE,
                            CUST_BL_CD, BUILDING, POST_CD_ADDR, POB_NO, POST_CD_POB, BANK_ACCOUNT_NO, PHONE_NO,
                             FISC_NO, MEMO, FIRST_VISIT_DATE, LAST_VISIT_DATE, TELEFAX_NO, EMAIL_ADDR, BONUS_IND,
                             BONUS_BALANCE, PROVINCE, TOP_CUST_IND, PROMOTER_CD, LAST_PROMO_DATE, DELIVERY_CD,
                             DATE_DELETED, RDC_VISIT_DATE, MOVIL, BUYER_NAME, POTENCIAL_PURCHASE_MONTH
                    FROM cust where store_no = 1 and rownum<10
                    order by store_no,cust_no"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_cust = res.fetchall()
    return data_cust