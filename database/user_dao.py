# dao (Database Access Object)
# 데이터베이스 관련 코드를 구현하는 곳

import pymysql
from database import connection
from flask import session

# 회원가입처리 (정보들을 DB에 넣기)
def add_user_info(*data):
    conn = connection.get_connection()

    sql ='''
        insert into user_table
        (user_name, user_id, user_pw,user_postal, user_addr1, user_addr2, user_status)
        values (%s, %s, %s, %s, %s, %s, 1)
    '''

    cursor = conn.cursor()
    cursor.execute(sql, data)

    conn.commit() # 커밋
    conn.close()  # 연결 닫기

# 아이디 중복 확인
def check_user_id(user_id):
    conn = connection.get_connection()

    sql = '''
        select *
        from user_table
        where user_status = 1
              and user_id = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id))

    # 하나만 가져오기!
    row = cursor.fetchone()

    if row == None :
        conn.close()
        return 'YES'
    else :
        conn.close()
        return 'NO'

# 로그인 정보확인 (로그인한 정보가 DB에 있는지?)
def checkLogin(*data):
    conn = connection.get_connection()

    sql = '''
        select user_idx
        from user_table
        where user_id = %s and user_pw = %s
              and user_status = 1
    '''

    cursor = conn.cursor()
    cursor.execute(sql, data)

    result = cursor.fetchone()
    print(result)

    if result == None :
        user_idx = -1
    else :
        user_idx = result[0]

    conn.close()
    
    return user_idx


# 회원정보처리
# 기존 정보는 저장 안함 (...zzz)
def user_modify(*data):
    conn = connection.get_connection() 
    print( '데이터 => ', data )
    sql = '''
        update user_table
        set user_pw = %s,
            user_postal = %s,
            user_addr1 = %s,
            user_addr2 = %s
            where user_idx = %s and user_status = 1

    '''

    cursor = conn.cursor()
    cursor.execute(sql,data)

    conn.commit()
    conn.close()


# 마이페이지 내 정보 가져오기
def getUser_Mypage(user_login):
    conn = connection.get_connection()

    sql = '''
        select user_name, user_id, user_addr1, user_addr2
        from user_table
        where user_idx = %s and user_status = 1
    
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (user_login))

    result = cursor.fetchone()
    user_info = {
        'user_name' : result[0],
        'user_id' : result[1],
        'user_addr1' : result[2],
        'user_addr2' : result[3],
        'user_idx' : user_login
    }
    conn.close()

    return user_info


# 마이페이지 내가 쓴 글 가져오기
def getContent_Mypage(user_idx):
    conn = connection.get_connection()

    user_idx = session['user_idx']
    sql = '''
        select f.f_content_idx, f.f_content_subject, f.f_content_date,f.f_view, f.f_likes, f.f_content_board_idx
               , u.user_id
        from free_table f, user_table u
        where f_content_writer_idx = %s
              and f_content_status = 1
              and f_content_writer_idx = u.user_idx
        order by f.f_content_idx desc
        limit 0, 10
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (user_idx))

    result = cursor.fetchall()

    data_list = []
    for obj in result :
        data_dic ={
            'content_idx' :obj[0],
            'content_subject' : obj[1],
            'content_date' : obj[2],
            'content_writer_name' : obj[6],
            'content_view' : obj[3],
            'content_likes' : obj[4],
            'board_idx' : obj[5]
        }
        data_list.append(data_dic)

    conn.close()

    return data_list