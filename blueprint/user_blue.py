
from flask import Blueprint, render_template, redirect, request, session
from database import user_dao

user = Blueprint('user_blue', __name__)


# 회원가입
@user.route('/user_join')
def user_join():
    html = render_template('user/user_join.html')
    return html


# 회원가입처리
@user.route('/user_join_pro', methods=['post'])
def user_join_pro() :
    # 정보를 추출해서 user_dao에 넘겨주기
    # request.values.get('name속성값')

    user_name = request.values.get('user_name')
    user_id = request.values.get('user_id')
    user_pw = request.values.get('user_pw')
    user_postal = request.values.get('user_postal')
    user_addr1 = request.values.get('user_addr1')
    user_addr2 = request.values.get('user_addr2')

    # user_dao 에서 add_user_info 함수 호출
    user_dao.add_user_info(user_name, user_id, user_pw,user_postal, user_addr1, user_addr2)
    return '''
            <script>
                alert("가입이 완료되었습니다")
                location.href="./user_login"
            </script>
           '''


# 마이페이지 회원정보 보기
@user.route('/user_mypage')
def user_mypage():
    user_login = session['user_idx']
    user_info = user_dao.getUser_Mypage(user_login)

    data_list = user_dao.getContent_Mypage(user_login)

    html = render_template('user/user_mypage.html', data_dic=user_info, data_list=data_list)
    return html


# 회원정보 수정
@user.route('/user_modify/<user_idx>')
def user_modify(user_idx):

    user_info = user_dao.getUser_Mypage(user_idx)

    html = render_template('user/user_modify.html', data_dic=user_info)
    return html


# 회원정보 수정 처리
@user.route('/user_modify_pro', methods=['post'])
def user_modify_pro() :

    user_pw = request.values.get('user_pw')
    user_postal = request.values.get('user_postal')
    user_addr1 = request.values.get('user_addr1')
    user_addr2 = request.values.get('user_addr2')
    user_idx = session['user_idx']

    user_dao.user_modify(user_pw, user_postal, user_addr1, user_addr2, user_idx)

    return '''
            <script>
                alert("수정이 완료 되었습니다")
                location.href="./user_mypage"
            </script>
           '''

# 로그인
@user.route('/user_login')
def user_login():
    html = render_template('user/user_login.html')
    return html

# 로그인 처리
@user.route('/user_login_pro', methods=['post'])
def user_login_pro():
    # redirect : 응답 결과로 브라우저가 요청할 주소를 전달한다.
    
    # form 전송할 때 지정한 name 값을 넣어주는거야
    user_id = request.values.get('user_id')
    user_pw = request.values.get('user_pw')

    result = user_dao.checkLogin(user_id, user_pw)
    print(user_id, user_pw)

    if result == -1 : # 로그인 실패, DB에서 가져온 정보가 없음
        return '''
            <script>
                alert("아이디나 비밀번호를 확인해주세요")
                location.href = "./user_login"
            </script>
        '''
    else :      # 로그인 성공
        session['login'] = 'YES'
        session['user_idx'] = result
        print(result)     

    return redirect('/')

# 아이디 중복 확인 처리
@user.route('/check_user_id', methods=['post'])
def check_user_id():
    user_id = request.values.get('user_id')
    result = user_dao.check_user_id(user_id)
    return result

# 로그아웃 처리
@user.route('/user_logout')
def user_logout():
    if 'login' in session:
        session.pop('login', None)

    return '''
            <script>
                alert("로그아웃 되었습니다.")
                location.href="/"
            </script>
           '''