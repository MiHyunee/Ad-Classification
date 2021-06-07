from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from service.SearchService import searchBlog, dataCrawling
from service.GetSourceService import crawlingSource
from service.OcrService import ocrTest
from service.SvmService import svm
from service.SvmTrainingService import svmTraining
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=["POST"])
def form():

    if request.method == 'POST':
        print("통신 성공")
        res = request.get_json()[0]
        blogPageArray = dataCrawling(res)
        blogPageArray = crawlingSource(blogPageArray)
        blogPageArray = ocrTest(blogPageArray)
        blogArray, predict = svm(blogPageArray)
        for i in predict:
            print(i)

        return jsonify(results = predict), 200


@bp.route('/training', methods=["GET"])
def train():
    svmTraining()
