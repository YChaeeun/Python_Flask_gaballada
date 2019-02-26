from flask import Blueprint, render_template, request, session
from functools import wraps
import time
from database import board_ex_dao

board_blue_example = Blueprint('board_example', __name__)

# example 글 목록 보기
@board_blue_example.route('/board_ex_list', defaults={'board_idx': 4, 'page': 1})
@board_blue_example.route('/board_ex_list/<board_idx>', defaults={'page': 1})
@board_blue_example.route('/board_ex_list/<board_idx>/<page>')
def board_ex_list(board_idx, page):
    board_name = board_ex_dao.get_board_name(board_idx)

    page_count, min, max, prev, next = board_ex_dao.get_paging_info(board_idx, page)

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

    content_list = board_ex_dao.getContentlist(board_idx, page)

    html = render_template('board_example/board_ex_list.html', data_dic=data_dic, data_list=content_list)
    return html


@board_blue_example.route('/board_ex_read', defaults={'board_idx': 4, 'content_idx': 1})
@board_blue_example.route('/board_ex_read/<board_idx>', defaults={'content_idx': 1})
@board_blue_example.route('/board_ex_read/<board_idx>/<content_idx>')
def board_ex_read(board_idx, content_idx) :

    content_list = board_ex_dao.getboard_exread(board_idx,content_idx)

    html = render_template('board_example/board_ex_read.html', data_list=content_list)
    return html
    