from config.database import OracleDB
from flask import jsonify

def store():
    sqlString = """select *
                    from store
                    order by store_no"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    payload = []
    content = {}
    for data_store in res:
        content = { 'store': data_store[0],'name':data_store[3],'status':data_store[2] }
        payload.append(content)
        content = {}
    return jsonify(payload)