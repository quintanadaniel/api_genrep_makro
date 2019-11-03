import cx_Oracle
from sqlalchemy import create_engine
#from decouple import config
from pprint import pprint
import datetime
from flask import jsonify


class OracleDB:
    """
       OracleDB Database
    """
    def __init__(self):
        self.username = 'dba_ho'
        self.password = 'yvc02tvf'
        self.hostname = '10.49.2.24'
        self.port = '1525'
        self.sid = 'MBSHO'
        self.engine = None
        self.conn = None
        self.rconn = None
        self.oracle_connection_string = ('oracle+cx_oracle://{username}:{password}@' +
            cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
        )

    def connect(self):
        try:
            self.engine = create_engine(
                self.oracle_connection_string.format(
                    username=self.username,
                    password=self.password,
                    hostname=self.hostname,
                    port=self.port,
                    service_name=self.sid,
                ), pool_size=100)
            self.conn = self.engine.connect()
            self.rconn = self.engine.raw_connection()
            return self.conn 
            print("conected...")

        except cx_Oracle.DatabaseError as e:
            self.engine = None
            print(e)
            exit(1)

    def stores(self):
            res = self.conn.execute("SELECT store_no,name,address||' '||town address,prov_county_state,store_type,gln,cot,deliv_cd,status FROM store order by store_no")
            data = res.fetchall()
            return data

    def nr_status(self):
            res = self.conn.execute("select * from nr_status where run_date in (select run_date from nightrun) order by start_date desc")
            data_nrstatus = res.fetchall()
            return data_nrstatus

    def connection_close(self):
        self.conn.close()
        print("Not Conected...")


if __name__ == '__main__':
    ora = OracleDB()
    ora.connect()
    ora.stores()
    ora.nr_status()
    ora.connection_close()