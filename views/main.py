from flask import Blueprint, request, jsonify
from service.SvmService import SvmService
from service.ReportService import reporting
from service.SourceService import SourceService
from concurrent.futures import ThreadPoolExecutor
import time


#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/training', methods=["GET"])
def train():
    svm.svmTraining()

    return '', 204

@bp.route('/search', methods=["POST"])
def concurrent():
    res = request.get_json()[0]
    blogPageArray = SourceService.transform_url(res)

    concurrentTime = time.time()

    pool = ThreadPoolExecutor(max_workers=4)
    results = list(pool.map(svmService.rxSvm, blogPageArray))

    print(time.time()-concurrentTime)
    return jsonify(results=results), 200

@bp.route('/report', methods=['POST'])
def report():
    url = request.get_json()[0]
    return reporting(url)

@bp.before_app_first_request
def setUp():
    global svm
    svm = SvmService()
    global svmService
    svmService = SvmService()

