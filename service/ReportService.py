from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


#front에서 URL받아오기
url = 'ddd'
#url = 'https://blog.naver.com/ll55kk678/222430846656' #크롤링할때처럼 PostView어쩌고 말고 다른걸로 바꿔야

def report(url):
    driver = webdriver.Chrome()

    #네이버 로그인
    loginUrl = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
    uid = 'll55kk'
    upw = 'wndghkalsrnr'

    driver.get(loginUrl)
    pyperclip.copy(uid)
    wait(driver, 3).until(EC.element_to_be_clickable((By.NAME, 'id'))).send_keys(Keys.COMMAND, 'v')
    pyperclip.copy(upw)
    driver.find_element_by_name('pw').send_keys(Keys.COMMAND, 'v')

    try:
        driver.find_element_by_id('log.login').click()
        driver.find_element_by_class_name('error')
        print('로그인 실패')#로그인 실패했다고 알려주기
        driver.quit()
    except:
        # 신고페이지로 이동
        driver.get('https://help.naver.com/support/contents/contents.help?serviceNo=964&categoryNo=2826')

        driver.find_element_by_id('quest_12604').click()
        wait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'quest_13352'))).click()
        wait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'btn_open_badurl_form'))).click()
        driver.find_element_by_id('url_input').send_keys(url)
        driver.find_element_by_id('btn_check_url').click()
        try:
            wait(driver, 1).until(EC.alert_is_present())
            Alert(driver).accept()
            driver.quit()
            print('url 이상')#url실패 사실 프론트에 알려주기
        except:
            driver.find_element_by_id('r1').click()
            driver.find_element_by_id('_btn_add_url').click()
            try:
                wait(driver, 1).until(EC.alert_is_present())
                Alert(driver).accept()
                driver.quit()
                print('등록 실패')#등록실패 사실 프론트에 알려주기
            except :
                print('good')
                #driver.find_element_by_id('btn btn_confrm').click()
                #완료되었음을 알려주기

report(url)