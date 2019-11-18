from config.database import OracleDB

def nrstatus():
    l_nrst = nr_status()
    print (l_nrst)
    return l_nrst

def nr_status():
    sqlString = """select *
                   from nr_status
                   where run_date in (select run_date from nightrun)
                   order by start_date desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_nrst = res.fetchall()
    return data_nrst