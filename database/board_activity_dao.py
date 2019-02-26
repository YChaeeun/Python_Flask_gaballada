
import pymysql
from database import connection
from flask import session
    

# 게시판 이름 가져오기 (번호를 주면 게시판 이름 가져오기!)
def get_board_name(board_idx) :
    conn = connection.get_connection()
    sql = '''
        select board_name
        from board_info_table
        where board_idx = %s
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (board_idx))

    result = cursor.fetchone()
    board_name = result[0]

    conn.close()
    return board_name


# 페이지 정보 가져오기....
# 흠.. 테이블 이름마다...??? 으악
def get_paging_info(board_idx, page) :
    conn = connection.get_connection()

    sql = '''
        select count(*)
        from activity_table
        where a_content_status = 1 and a_content_board_idx = %s

    '''
    cursor = conn.cursor()
    cursor.execute(sql, (board_idx))

    # 게시판의 전체 글의 개수 가져오기
    result = cursor.fetchone()
    content_count = result[0]

    page_count = content_count // 10
    if content_count % 10 > 0 :
        page_count += 1
    
    # ex. 지금 2페이지에 있다면 2//10 = 0 이니까 최소값은 0*10+1 = 1
    # max = 1+9 = 10
    # 만약 page_count보다 max가 크면 말이 안되니까 max = page_count로 바꾸기
    min = ((int(page)-1) // 10 ) * 10 +1
    max = min + 9

    if max > page_count :
        max = page_count
    
    prev = min -1
    next = max +1

    conn.close()
    return page_count, min, max, prev, next