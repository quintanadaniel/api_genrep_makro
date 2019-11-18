from config.database_bdo import OracleDB_bdoho

def mafisbdoho_log():
    l_mafisbdoholog = mafis_bdoho_log()
    print (l_mafisbdoholog)
    return l_mafisbdoholog

def mafis_bdoho_log():
    sqlString = """select * from
                    MAFIS_STAGE
                    where source <> 'MK_AR_RECIBOS'
                    and trunc(created_date) = trunc(sysdate)
                    order by created_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    data_mafisbdoholog = res.fetchall()
    return data_mafisbdoholog