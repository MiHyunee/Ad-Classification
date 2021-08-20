from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from service.SearchService import dataCrawling
from service.GetSourceService import rxCrawling
from service.OcrService import rxOcr
from service.SvmService import rxSvm
from service.SvmTrainingService import svmTraining
from service.ReportService import reporting
from concurrent.futures import ThreadPoolExecutor
import time

#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/training', methods=["GET"])
def train():
    svmTraining()

def flow(blogArray):
    blogPageArray = rxCrawling(blogArray)
    blogPageArray = rxOcr(blogPageArray)
    predict = rxSvm(blogPageArray)
    return predict

@bp.route('/search', methods=["POST"])
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
    reporting(url)

    return '', 204
