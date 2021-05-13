from flask import Blueprint, render_template, redirect, url_for, request
from service.SearchService import searchBlog
from service.GetSourceService import crawlingSource
from service.ocrService import ocrTest
from service.SvmService import svm
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=["GET"])
def form():
    query = request.args['query']
    print(query)
    blogPageArray = searchBlog(query)
    blogPageArray = crawlingSource(blogPageArray)
    blogPageArray = ocrTest(blogPageArray)
    svm(blogPageArray)
    return query
