from config.database_bdo import OracleDB_bdoho

def getmafisbdoho():
    l_mafisbdoho = get_mafisbdoho()
    print (l_mafisbdoho)
    return l_mafisbdoho

def get_mafisbdoho():
    sqlString = """select * from
                    msa_etl_ctrl_status@stage
                    where (run_date = trunc(sysdate) or run_date = (select run_date from nightrun))
                    order by src_start_date desc,etl_start_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    data_mafisbdoho = res.fetchall()
    return data_mafisbdoho