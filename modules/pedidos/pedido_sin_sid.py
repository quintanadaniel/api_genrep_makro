from config.database import OracleDB

def get_OcSinSid():
    l_ocSinSid = ocSinSid()
    print (l_ocSinSid)
    return l_ocSinSid

def ocSinSid():
    sqlString = """select * from
                    t_sin_sid
                    order by tda,oc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_oc_sin_sid = res.fetchall()
    return data_oc_sin_sid