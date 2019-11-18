from config.database import OracleDB

def mafisMK_log():
    l_mafismklog = mafismklog()
    print (l_mafismklog)
    return l_mafismklog

def mafismklog():
    sqlString = """select * from
                    MAFIS_STAGE
                    where source <> 'MK_AR_RECIBOS'
                    and trunc(created_date) = trunc(sysdate)
                    order by created_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_mafismklog = res.fetchall()
    return data_mafismklog