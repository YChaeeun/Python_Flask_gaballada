import pymysql
from database import connection

# 글 목록을 가져온다.
def getContentlist(board_idx, page) :
    conn = connection.get_connection()

    # 현재 페이지에 대한 글 시작 인덱스를 계산한다.
    start_idx = (int(page) - 1) * 10

    sql = '''
                select ex_content_idx, ex_content_subject, ex_content_date
                from  ex_table
                where ex_content_status = 1 and ex_content_board_idx = %s
                order by ex_content_idx desc
                limit %s,10
          '''
    cursor = conn.cursor()
    cursor.execute(sql, (board_idx, start_idx))

    row = cursor.fetchall()

    # 데이터를 담을 리스트
    data_list = []
    # 리스트에 데이터를 담는다.
    for obj in row :
        data_dic = {
            'content_idx' : obj[0],
            'content_subject' : obj[1],
            'content_date' : obj[2]
        }
        data_list.append(data_dic)

    conn.close()
    return data_list


# 게시판 정보를 가져온다.
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


# 페이징 정보를 구하는 함수
def get_paging_info(board_idx, page) :
    conn = connection.get_connection()
    # 글 전체의 개수를 가져온다.
    sql1 = '''
            select count(*)
            from ex_table
            where ex_content_board_idx=%s
                  and ex_content_status=1
           '''
    cursor = conn.cursor()
    cursor.execute(sql1, (board_idx))
    result1 = cursor.fetchone()
    content_count = result1[0]

    # 전체 페이지의 개수를 개산한다.
    page_count = content_count // 10
    if content_count % 10 > 0 :
        page_count += 1

    # pagenation 최소 최대값
    min = ((int(page) - 1) // 10) * 10 + 1
    max = min + 9

    # 최대값이 전체 페이지 수보다 많으면 전체 페이지수로
    # 셋팅한다.
    if max > page_count :
        max = page_count

    # 이전버튼과 다음 버튼을 누를때 보여줄 페이지 번호
    prev = min - 1
    next = max + 1

    conn.close()
    return page_count, min, max, prev, next



def getboard_exread(board_idx, content_idx) :
    conn = connection.get_connection()


    sql = '''
                select ex_content_subject, ex_test, ex_input, ex_output, ex_time_limit, ex_memory_limit, ex_content_idx
                from  ex_table
                where ex_content_status = 1 and ex_content_board_idx = %s  and ex_content_idx = %s
            
          '''
    cursor = conn.cursor()
    cursor.execute(sql, (board_idx, content_idx))

    row = cursor.fetchall()

    # 데이터를 담을 리스트
    data_list = []
    # 리스트에 데이터를 담는다.
    for obj in row :
        data_dic = {
            'content_subject' : obj[0],
            'test' : obj[1],
            'input' : obj[2],
            'output' : obj[3],
            'time_limit' : obj[4],
            'memory_limit' : obj[5],
            'content_idx' : obj[6]
        }
        data_list.append(data_dic)

    conn.close()
    return data_list