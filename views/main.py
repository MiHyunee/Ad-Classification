from flask import Blueprint, render_template, redirect, url_for, request
from service.SearchService import searchBlog

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=["GET"])
def form():
    query = request.args['query']
    print(query)
    searchBlog(query)
    return query
