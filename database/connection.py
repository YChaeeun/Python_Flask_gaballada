# DB 연결 코드

import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234'
                            ,db ='project_db', charset='utf8')
    return conn