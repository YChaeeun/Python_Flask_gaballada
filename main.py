# main.py

from flask import Flask, render_template, request
from blueprint import board_blue_free,user_blue, board_blue_app, board_blue_phone, board_blue_web, board_blue_activity, board_blue_example, board_blue_club, board_blue_study
from database import connection

# 웹 서버 역활을 하기위한 객체를 생성한다.
app = Flask(__name__)
# 블루플린트를 등록한다.
app.register_blueprint(board_blue_free.board_blue_f, url_prefix='/boards')
app.register_blueprint(board_blue_app.board_blue_app, url_prefix='/boards')
app.register_blueprint(board_blue_phone.board_blue_phone, url_prefix='/boards')
app.register_blueprint(board_blue_web.board_blue_web, url_prefix='/boards')
app.register_blueprint(board_blue_activity.board_blue_activity, url_prefix='/boards')
app.register_blueprint(board_blue_example.board_blue_example, url_prefix='/boards')
app.register_blueprint(board_blue_club.board_blue_club, url_prefix='/boards')
app.register_blueprint(board_blue_study.board_blue_study, url_prefix='/boards')
app.register_blueprint(user_blue.user, url_prefix='/user')
# 세션 사용을 위해 secret key를 등록한다.
app.secret_key = 'owiefjlsfsnlnsnvo'

# 주소만 입력해서 요청했을 때 호출되는 함수
@app.route('/')
def index():
    # 데이터 베이스 접속
    '''
    conn = connection.get_connection()
    # 쿼리문

    sql = ''' 
    '''
        select app_content_subject as content_subject, 
	    app_content_text as content_text,
        app_likes as likes
        from app_table
        union all
        select web_content_subject, web_content_text, web_likes
        from web_service_table
        union all
        select m_content_subject, m_content_text, m_likes
        from m_service_table
        order by likes desc
        limit 0, 5;
            '''
    # 쿼리문실행
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    # 결과를 가져온다.
    result = cursor.fetchall()
    # 데이터를 담는다.
    list1 = []
    for row in result:
        dic1 = {
            'content_subject': row[0],
            'content_text': row[1],
            'likes': row[2]
        }

        list1.append(dic1)
    conn.close()

    #html = render_template('index.html', #data_list=list1)
    '''
    html = render_template('index.html')
    return html

# 웹 서버를 실행한다.
# host : 접속할 컴퓨터의 IP, 0.0.0.0으로 셋팅하면 모든 컴퓨터 허용
# port : 포트번호 설정, 80이면 웹 브라우저에서 포트번호 생략가능
#app.run(host='0.0.0.0', port=80)
if __name__ == '__main__' :
    app.run(debug=True)