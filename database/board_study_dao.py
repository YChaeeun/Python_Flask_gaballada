
import pymysql
from database import connection
from flask import session

# 글 저장하기
# 게시판 별로 따로 만들어야 해??
# 조회수와 좋아요 정보 갱신하는 거 어떻게 할지 아직 안했숨
def addContentData_s(*data) :
    conn = connection.get_connection()

    sql = '''
        insert into study_table
            (s_content_subject, s_content_writer_idx, 
             s_content_date, s_content_text, s_content_file,
             s_content_status, s_content_board_idx)
            values (%s, %s, curdate(), %s, %s, 1, 5)
    '''

    cursor = conn.cursor()
    cursor.execute(sql, data)

    conn.commit()
    conn.close()
    

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
            from study_table
            where s_content_board_idx=%s
                  and s_content_status=1
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


# 글 목록 가져오기
def getContentlist(board_idx, page):
    conn = connection.get_connection()
    
    # 현재 페이지에서 첫번째 게시글의 번호!
    start_idx = (int(page)-1)*10

    sql = '''
            select a1.s_content_idx, a1.s_content_subject, a2.user_id, a1.s_content_date
            from study_table a1, user_table a2
            where a1.s_content_writer_idx = a2.user_idx and a1.s_content_status = 1 and a1.s_content_board_idx = %s
            order by a1.s_content_idx desc
            limit %s, 10
    '''

    cursor = conn.cursor()
    cursor.execute(sql,(board_idx,start_idx))

    row = cursor.fetchall()
    data_list =[]

    for obj in row :
        data_dic = {
            'content_idx' :obj[0],
            'content_subject' : obj[1],
            'content_writer_name' : obj[2],
            'content_date' : obj[3]
        }
        data_list.append(data_dic)
    
    conn.close()

    return data_list


# 글 읽어오기
def readContent(board_idx, content_idx) :
    conn = connection.get_connection()
    sql = '''
        select a1.s_content_subject, a1.s_content_idx, a1.s_content_date, a1.s_content_text, a1.s_content_file,
	                a2.user_id, a2.user_idx
            from study_table a1, user_table a2
            where a1.s_content_board_idx = %s and a1.s_content_status = 1
	                and a1.s_content_idx = %s
	                and a1.s_content_writer_idx = a2.user_idx
    '''

    board_name = get_board_name(board_idx)

    cursor = conn.cursor()
    cursor.execute(sql, (board_idx, content_idx))

    result = cursor.fetchone()
    data_dic = {
        'content_subject' : result[0],
        'content_idx' : result[1],
        'content_date' : result[2],
        'content_text' :result[3],
        'content_file' : result[4],
        'content_writer_name' : result[5],
        'board_name' : board_name,
        'board_idx' : board_idx,
        'user_idx' : result[6]
        }

    conn.close()
    return data_dic

# 글 수정한거 업데이트 하기
# 이전 글은 status만 바꾸고, 새로운 내용으로 insert하기
def updateContent(board_subject, board_text, file_name, user_idx, content_idx):
    conn = connection.get_connection()
    sql = '''
        update study_table
            set s_content_subject = %s, s_content_text = %s, s_content_file = %s
            where s_content_writer_idx = %s and s_content_idx = %s and s_content_board_idx = 5
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (board_subject, board_text, file_name, user_idx, content_idx))

    conn.commit()
    conn.close()


# 글 삭제하기 (상태값만 바꿔서 안보이게 처리)
def deleteContent(board_idx, content_idx):
    conn = connection.get_connection()

    user_idx = session['user_idx']
    sql = '''
        update study_table
        set s_content_status = 0
        where s_content_idx = %s and s_content_writer_idx = %s
              and s_content_board_idx = %s and s_content_status = 1
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (content_idx, user_idx, board_idx))

    conn.commit()
    cursor.close()
