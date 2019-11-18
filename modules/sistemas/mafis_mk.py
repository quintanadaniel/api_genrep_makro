from config.database import OracleDB

def getmafismkho():
    l_mafismk = get_mafismk()
    print (l_mafismk)
    return l_mafismk

def get_mafismk():
    sqlString = """select * from
                    msa_etl_ctrl_status@stage
                    where (run_date = trunc(sysdate) or run_date = (select run_date from nightrun))
                    order by src_start_date desc,etl_start_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_mafismk = res.fetchall()
    return data_mafismk