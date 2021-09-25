from flask import Blueprint, request, jsonify
from service.SvmService import SvmService
from service.ReportService import reporting
from service.SourceService import SourceService
from concurrent.futures import ThreadPoolExecutor
from dataStream.producer import put_to_stream
from dataStream.consumer import get_records
import time
import boto3


#Blueprint클래스로 객체 생성시 이름, 모듈명, url_prefix값 전달
bp = Blueprint('main', __name__, url_prefix='/')

#Kinesis Stream 생성
client = boto3.client('kinesis', region_name='ap-northeast-1')

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

    # 프론트에서 검색어 받아오는거 필요함 word =
    put_to_stream('***', word, time.time(),'search-word')  # stream에 검색어 입력
    return jsonify(results=results), 200

@bp.route('/report', methods=['POST'])
def report():
    url = request.get_json()[0]
    put_to_stream('***', url, time.time(),'reported-url')
    return reporting(url)

@bp.route('/admin_search_word', methods=['POST'])
def stream():
    get_records('search-word')

@bp.route('/admin_report', methods=['GET'])
def stream2():
    get_records('reported-url')

@bp.before_app_first_request
def setUp():
    global svm
    svm = SvmService()
    global svmService
    svmService = SvmService()

