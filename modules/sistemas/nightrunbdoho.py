from config.database_bdo import OracleDB_bdoho

def nrstatus_bdoho():
    l_nrstbdoho = nr_status_bdoho()
    print (l_nrstbdoho)
    return l_nrstbdoho

def nr_status_bdoho():
    sqlString = """select *
                   from nr_status
                   where run_date in (select run_date from nightrun)
                   order by start_date desc"""
    ora = OracleDB_bdoho().connect()
    res = ora.execute(sqlString)
    data_nrstbdoho = res.fetchall()
    return data_nrstbdoho