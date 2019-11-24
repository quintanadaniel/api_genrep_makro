from config.database import OracleDB
from flask import jsonify

def get_mkho300():
    sqlstr = """select re.rep_grp_no,
                re.descr,
                de.dept_no,
                de.descr,
                m.art_grp_no,
                gp.descr,
                m.store_no,
                to_char(m.mcant,'999999990,99') canti,
                to_char(m.mventas,'999999990,99') ventas,
                to_char(m.mlucro,'999999990,99') lucro,
                to_char(m.mmcom,'999999990,99') marcom,
                to_char(m.majustes,'999999990,99') ajustes,
                to_char(m.mbonif,'999999990,99') bonif,
                to_char(m.mvaloriz,'999999990,99') valoriz,
                to_char((m.mlucfin - m.mtransf_int) / (m.mventas+ 0.001) * 100,'999999990,99') marfin,
                to_char(m.mcompras,'999999990,99') rm,
                to_char(d.stock,'999999990,99') Stock
            from art_grp gp,
                    dept de,
                    rep_grp re,
                    tble300m m,
                    tble300d d
            where m.art_grp_no=gp.art_grp_no
            and gp.dept_no=de.dept_no
            and de.rep_grp_no=re.rep_grp_no
            and m.art_grp_no=d.art_grp_no (+)
            and m.store_no=d.store_no(+)
            order by 1,3,5,7"""
    ora = OracleDB().connect()
    res_mkho300 = ora.execute(sqlstr)
    payload_mkho300 = []
    context_mkho300 = {}
    for data_mkho300 in res_mkho300:
        context_mkho300 = {'area': data_mkho300[0],'descr_area': data_mkho300[1],'depto': data_mkho300[2],'descr_depto': data_mkho300[3],'grupo': data_mkho300[4],'descr_grupo': data_mkho300[5],'tienda': data_mkho300[6],'canti': data_mkho300[7],'ventas': data_mkho300[8],'lucro': data_mkho300[9],'marcom': data_mkho300[10],'ajustes': data_mkho300[11],'bonif': data_mkho300[12],'valoriz': data_mkho300[13],'marfin': data_mkho300[14],'rm': data_mkho300[15],'Stock': data_mkho300[16] }
        payload_mkho300.append(context_mkho300)
        context_mkho300 = {}
    return jsonify(payload_mkho300)
