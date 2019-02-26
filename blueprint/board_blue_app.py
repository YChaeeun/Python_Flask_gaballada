# ?!

from flask import Blueprint, render_template, request, session
from functools import wraps
import time
from database import board_app_dao

board_blue_app = Blueprint('board_app', __name__)


def loginCheckDeco(f):
    @wraps(f)
    def deco1(*args, **kwargs):
        if session.get('login', None) is None:
            return '''
                <script>
                    alert('로그인 해주세요')
                    location.href="../user/user_login"
                </script>
            '''
        return f(*args, **kwargs)

    return deco1


# app 글 목록 보기
@board_blue_app.route('/board_app_list', defaults={'board_idx': 1, 'page': 1})
@board_blue_app.route('/board_app_list/<board_idx>', defaults={'page': 1})
@board_blue_app.route('/board_app_list/<board_idx>/<page>')
def board_app_list(board_idx, page):
    board_name = board_app_dao.get_board_name(board_idx)

    page_count, min, max, prev, next = board_app_dao.get_paging_info(board_idx, page)

    data_dic = {
        'board_idx': board_idx,
        'board_name': board_name,
        'page_count': page_count,
        'min': min,
        'max': max,
        'prev': prev,
        'next': next,
        'page': int(page)
    }

    content_list = board_app_dao.getContentlist(board_idx, page)

    html = render_template('board_app/board_app_list.html', data_dic=data_dic, data_list=content_list)
    return html


# app 글 내용 보기
@board_blue_app.route('/board_app_read', defaults={'board_idx': 1, 'content_idx': 1})
@board_blue_app.route('/board_app_read/<board_idx>', defaults={'content_idx': 1})
@board_blue_app.route('/board_app_read/<board_idx>/<content_idx>')
def board_app_read(board_idx, content_idx):
    board_app_dao.addView(board_idx, content_idx)
    content = board_app_dao.readContent(board_idx, content_idx)
    board_name = [
        board_app_dao.get_board_name(board_idx)
    ]

    html = render_template('board_app/board_app_read.html', data_dic=content, data_list=board_name)
    return html


# 글 작성하기
@board_blue_app.route('/board_app_write', defaults={'board_idx': 1})
@board_blue_app.route('/board_app_write/<board_idx>')
@loginCheckDeco
def board_app_write(board_idx):
    data_dic = {
        'board_idx': board_idx
    }

    html = render_template('board_app/board_app_write.html', data_dic=data_dic)
    return html


# app 작성 완료 처리
@board_blue_app.route('/board_app_write_pro', methods=['post'])
def board_app_write_pro():
    #board_app_idx = request.values.get('board_idx')
    board_app_subject = request.values.get('board_subject')
    board_app_text = request.values.get('board_text')

    if 'board_image' in request.files:
        board_image = request.files['board_image']
        file_name = str(int(time.time())) + board_image.filename

        path = 'static/upload/' + file_name
        board_image.save(path)
    else:
        file_name = None

    board_app_dao.addContentData_a(board_app_subject, session['user_idx'], board_app_text, file_name)

    return '''
            <script>
                alert("저장되었습니다")
                location.href="./board_app_list"
            </script>
           '''


# app 글 수정하기
@board_blue_app.route('/board_app_modify', defaults={'board_idx': 1, 'content_idx': 1})
@board_blue_app.route('/board_app_modify/<board_idx>', defaults={'content_idx': 1})
@board_blue_app.route('/board_app_modify/<board_idx>/<content_idx>')
def board_app_modify(board_idx, content_idx):
    print('수정하는 페이지', board_idx, content_idx)
    data_dic = board_app_dao.readContent(board_idx, content_idx)

    html = render_template('board_app/board_app_modify.html', data_dic=data_dic)
    return html


# 수정 처리
@board_blue_app.route('/board_app_modify_pro', methods=['post'])
def board_app_modify_pro():
    # board_idx = request.values.get('board_idx')
    content_idx = request.values.get('content_idx')
    board_subject = request.values.get('board_subject')
    board_text = request.values.get('board_text')

    if 'board_image' in request.files:
        board_image = request.files['board_image']
        file_name = str(int(time.time())) + board_image.filename

        path = 'static/upload' + file_name
        board_image.save(path)
    else:
        file_name = None

    user_idx = session['user_idx']

    print('넘겨주는값', board_subject, board_text, file_name, user_idx, content_idx)
    board_app_dao.updateContent(board_subject, board_text, file_name, user_idx, content_idx)

    return '''
        <script>
            alert("수정되었습니다")
            location.href="./board_app_list"
        </script>
        '''


# app 글 삭제하기 (글 상태 0으로 바꾸기)
@board_blue_app.route('/board_app_delete', defaults={'board_idx': 1, 'content_idx': 1})
@board_blue_app.route('/board_app_delete/<board_idx>', defaults={'content_idx': 1})
@board_blue_app.route('/board_app_delete/<board_idx>/<content_idx>')
def board_app_delete(board_idx, content_idx):
    board_app_dao.deleteContent(board_idx, content_idx)

    return '''
            <script>
                alert("삭제되었습니다")
                location.href="/boards/board_app_list"
            </script>
           '''