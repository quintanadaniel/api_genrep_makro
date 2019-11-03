from config.database import OracleDB


def profis():
    l_profi = profi()
    print (l_profi)
    return l_profi

def profi():
    sqlString = """select origin_name,a.*
                    from mkstg_etl_ctrl_status@stage_profi a ,mkstg_interface_groups@stage_profi b
                    where a.interface_group = b.interface_group
                      and rundate in (select run_date from nightrun)
                      and a.interface_group not in ('TRANSFER','ORDERS')
                    order by 2 desc"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_profi = res.fetchall()
    return data_profi