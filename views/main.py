from flask import Blueprint, render_template, redirect, url_for, request
from service.SearchService import searchBlog
from service.GetSourceService import crawlingSource
from service.ocrService import ocrTest
from service.SvmService import svm
from service.DataMiningService import tokenizer, token2vec
from service.SvmTrainingService import svmTraining
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

from service.cnnTest import cnnTest

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=["GET"])
def form():
    query = request.args['query']
    print(query)
    blogPageArray = searchBlog(query)
    blogPageArray = crawlingSource(blogPageArray)
    blogPageArray = ocrTest(blogPageArray)
    x_data, y_data = tokenizer()
    x_sequence = token2vec(x_data)
    svmTraining(x_sequence, y_data)

    return query
