# ?!

from flask import Blueprint, render_template, request, session
from functools import wraps
import time
from database import board_m_dao

board_blue_phone = Blueprint('board_phone', __name__)


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



# phone 글 목록 보기
@board_blue_phone.route('/board_m_list', defaults={'board_idx': 2, 'page': 1})
@board_blue_phone.route('/board_m_list/<board_idx>', defaults={'page': 1})
@board_blue_phone.route('/board_m_list/<board_idx>/<page>')
def board_m_list(board_idx, page):
    board_name = board_m_dao.get_board_name(board_idx)

    page_count, min, max, prev, next = board_m_dao.get_paging_info(board_idx, page)

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

    content_list = board_m_dao.getContentlist(board_idx, page)

    html = render_template('board_phone/board_m_list.html', data_dic=data_dic, data_list=content_list)
    return html


# phone 글 내용 보기
@board_blue_phone.route('/board_m_read', defaults={'board_idx': 2, 'content_idx': 1})
@board_blue_phone.route('/board_m_read/<board_idx>', defaults={'content_idx': 1})
@board_blue_phone.route('/board_m_read/<board_idx>/<content_idx>')
def board_m_read(board_idx, content_idx):
    board_m_dao.addView(board_idx, content_idx)
    content = board_m_dao.readContent(board_idx, content_idx)
    board_name = [
        board_m_dao.get_board_name(board_idx)
    ]

    html = render_template('board_phone/board_m_read.html', data_dic=content, data_list=board_name)
    return html

# 글 작성하기
@board_blue_phone.route('/board_m_write', defaults={'board_idx': 2})
@board_blue_phone.route('/board_m_write/<board_idx>')
@loginCheckDeco
def board_m_write(board_idx):
    data_dic = {
        'board_idx': board_idx
    }

    html = render_template('board_phone/board_m_write.html', data_dic=data_dic)
    return html


# phone 작성 완료 처리
@board_blue_phone.route('/board_m_write_pro', methods=['post'])
def board_m_write_pro():
    #board_m_idx = request.values.get('board_m_idx')
    board_m_subject = request.values.get('board_subject')
    board_m_text = request.values.get('board_text')

    if 'board_image' in request.files:
        board_image = request.files['board_image']
        file_name = str(int(time.time())) + board_image.filename

        path = 'static/upload/' + file_name
        board_image.save(path)
    else:
        file_name = None

    board_m_dao.addContentData_m(board_m_subject, session['user_idx'], board_m_text, file_name)

    return '''
            <script>
                alert("저장되었습니다")
                location.href="./board_m_list"
            </script>
           '''


# phone 글 수정하기
@board_blue_phone.route('/board_m_modify', defaults={'board_idx': 2, 'content_idx': 1})
@board_blue_phone.route('/board_m_modify/<board_idx>', defaults={'content_idx': 1})
@board_blue_phone.route('/board_m_modify/<board_idx>/<content_idx>')
def board_m_modify(board_idx, content_idx):
    print('수정하는 페이지', board_idx, content_idx)
    data_dic = board_m_dao.readContent(board_idx, content_idx)

    html = render_template('board_phone/board_m_modify.html', data_dic=data_dic)
    return html


# 수정 처리
@board_blue_phone.route('/board_m_modify_pro', methods=['post'])
def board_m_modify_pro():
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
    board_m_dao.updateContent(board_subject, board_text, file_name, user_idx, content_idx)

    return '''
        <script>
            alert("수정되었습니다")
            location.href="./board_m_list"
        </script>
        '''


# 자유게시판 글 삭제하기 (글 상태 0으로 바꾸기)
@board_blue_phone.route('/board_m_delete', defaults={'board_idx': 2, 'content_idx': 1})
@board_blue_phone.route('/board_m_delete/<board_idx>', defaults={'content_idx': 1})
@board_blue_phone.route('/board_m_delete/<board_idx>/<content_idx>')
def board_m_delete(board_idx, content_idx):
    board_m_dao.deleteContent(board_idx, content_idx)

    return '''
            <script>
                alert("삭제되었습니다")
                location.href="/boards/board_m_list"
            </script>
           '''