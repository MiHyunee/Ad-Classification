from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from service.SearchService import searchBlog, dataCrawling
from service.GetSourceService import crawlingSource, rxCrawling
from service.OcrService import ocrTest, rxOcr
from service.SvmService import svm, rxSvm
from service.SvmTrainingService import svmTraining
from service.ReportService import report
from model.BlogPage import BlogPage
from model.ImagePath import ImagePath
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/search', methods=["POST"])
def form():

    if request.method == 'POST':
        print("통신 성공")
        startTime = time.time()
        res = request.get_json()[0]
        blogPageArray = dataCrawling(res)
        blogPageArray = crawlingSource(blogPageArray)
        blogPageArray = ocrTest(blogPageArray)
        blogArray, predict = svm(blogPageArray)
        for i in predict:
            print(i)

        print(time.time()-startTime)

        return jsonify(results = predict), 200


@bp.route('/training', methods=["GET"])
def train():
    svmTraining()

def flow(blogArray):
    blogPageArray = rxCrawling(blogArray)
    blogPageArray = rxOcr(blogPageArray)
    predict = rxSvm(blogPageArray)
    return predict

@bp.route('/concurrent', methods=["POST"])
def concurrent():
    print("****병렬****")
    res = request.get_json()[0]
    blogPageArray = dataCrawling(res)

    concurrentTime = time.time()

    pool = ThreadPoolExecutor(max_workers=4)
    results = list(pool.map(flow, blogPageArray))

    print(time.time()-concurrentTime)
    return jsonify(results=results), 200

@bp.route('/report', methods=['POST'])
def report():
    url = request.get_json()[0]
    report(url)

    return '', 204
