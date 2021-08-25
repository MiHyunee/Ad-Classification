from flask import Flask
from service.ReportService import error_handle


def create_app():
    app = Flask(__name__)

    #플라스크 앱 생성 시 blueprint적용하기
    from views import main
    app.register_blueprint(main.bp)
    error_handle(app)
    return app