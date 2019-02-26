from flask import Blueprint, render_template, request, session
from functools import wraps
import time
from database import board_activity_dao

board_blue_activity = Blueprint('board_activity', __name__)

# 글 목록 activity 게시판 글 목록
@board_blue_activity.route('/board_activity_list', defaults={'board_idx' : 6, 'page' : 1})
@board_blue_activity.route('/board_activity_list/<board_idx>', defaults={'page' : 1})
@board_blue_activity.route('/board_activity_list/<board_idx>/<page>')
def board_activity_list(board_idx, page) :

    # 게시판 정보를 가져온다.
    board_name = board_activity_dao.get_board_name(board_idx)

    # 페이징 관련 정보를 가져온다.
    page_count, min, max, prev, next = board_activity_dao.get_paging_info(board_idx, page)

    data_dic = {
        'board_idx' : board_idx,
        'board_name' : board_name,
        'page_count' : page_count,
        'min' : min,
        'max' : max,
        'prev' : prev,
        'next' : next,
        'page' : int(page)
    }

    html = render_template('board_activity/board_activity_list.html', data_dic=data_dic)
    return html