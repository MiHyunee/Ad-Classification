from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import pyperclip

def check_alert(driver): #경고창 확인하는 함수
    try:
        driver.switch_to.alert
        return True
    except NoAlertPresentException:
        return False

def reporting(url):
    driver = webdriver.Chrome()

    #네이버 로그인
    loginUrl = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
    uid = 'id'
    upw = 'pw'

    driver.get(loginUrl)
    pyperclip.copy(uid)
    wait(driver, 3).until(EC.element_to_be_clickable((By.NAME, 'id'))).send_keys(Keys.COMMAND, 'v')
    pyperclip.copy(upw)
    driver.find_element_by_name('pw').send_keys(Keys.COMMAND, 'v')

    wait(driver,3).until(EC.element_to_be_clickable((By.ID, 'log.login'))).click()
    if(driver.current_url != "https://www.naver.com/"):
        driver.quit()
        raise LoginError

    # 신고페이지로 이동
    driver.get('https://help.naver.com/support/contents/contents.help?serviceNo=964&categoryNo=2826')

    driver.find_element_by_id('quest_12604').click()
    wait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'quest_13352'))).click()
    wait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'btn_open_badurl_form'))).click()
    driver.find_element_by_id('url_input').send_keys(url)
    driver.find_element_by_id('btn_check_url').click()

    if(check_alert(driver)):
        driver.quit()
        raise UrlError

    driver.find_element_by_id('r1').click()
    driver.find_element_by_id('_btn_add_url').click()

    if(check_alert(driver)):
        driver.quit()
        raise AddError

    #driver.find_element_by_id('btn btn_confrm').click()

def error_handle(app):

    @app.errorhandler(LoginError)
    def handler_error(e):
        return error_response("로그인에 실패했습니다","LoginError"),1001

    @app.errorhandler(UrlError)
    def handle_error(e):
        return error_response("네이버 블로그만 가능합니다. URL을 다시 확인해주세요", "UrlError"),1002

    @app.errorhandler(AddError)
    def handler_error(e):
        return error_response("등록에 실패했습니다.", "AddError"), 1003

def error_response(user_error_message, dev_error_message, status_code):
    response = {
                    "user_error_message" : user_error_message,
                    "dev_error_message" : dev_error_message,
                    "status_code": status_code
                }
    return response

class LoginError(Exception): #로그인 에러 정의
    pass
class UrlError(Exception): #url 에러 정의
    pass
class AddError(Exception): # 등록 실패 에러 정
    pass