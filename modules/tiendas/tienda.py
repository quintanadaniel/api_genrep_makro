from config.database import OracleDB

def stores():
    l_store = store()
    print (l_store)
    return l_store

def store():
    sqlString = """select STORE_NO, MBS_TYPE, STATUS, NAME, ADDRESS, TOWN, PHONE_NO, BANK_ACCOUNT_NO, BANK_NAME, STORE_TYPE, BUILDING, PROV_COUNTY_STATE, ADDR_PST_CD, POB_NO, POB_PST_CD, TELEX_NO, TELEFAX_NO, BANK_ADDRESS, BANK_TOWN, BANK_COUNTY, BANK_POSTAL_CD, BANK_POB_NO, BANK_POB_PST_CD, EIS_DATE, BONUS_ACTIVE_STORE, OPENING_DATE, LIKE_FOR_LIKE, REGION_NO, E_MAIL, GLN, REFURBISH_DATE, STATE_ID, REGION_PR, SHORT_NAME, CHAIN, COT, DELIV_CD
                    from store
                    order by store_no"""
    ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_store = res.fetchall()
    return data_store