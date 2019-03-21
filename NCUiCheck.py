# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:25:34 2019
@主題:中央大學人資系統自動簽到程式
@作者: 羅聖明 a.k.a 神奇寶貝訓練家
@實作方式:以腳本方式結合Chrome進行自動簽到

@系統需求:需先pip install selenium 、以及下載符合版本的ChromeDriver(下載點:http://chromedriver.chromium.org/downloads)
@需求:[使用者帳號]、[使用者密碼]、[工作事項]

"""

from selenium import webdriver

#輸入帳號密碼
###需求:[使用者帳號]
userName= ('')
###需求:[使用者密碼]
userPass= ('') 
###需求:[工作事項]
work= "登記成績、回覆學生問題"

chromedriver = executable_path=r"C:/..../chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get('https://cis.ncu.edu.tw/HumanSys/')
driver.set_window_position(0,0) #瀏覽器位置

#點選登入
driver.find_element_by_xpath('//*[@id="cssmenu"]/ul/li/a').click()

#輸入帳號密碼
driver.find_element_by_xpath('//*[@id="userid_input"]').send_keys(userName)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/form/fieldset/div[2]/div/input').send_keys(userPass)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/form/fieldset/div[3]/div/button').click()

#跳轉頁面[ 簽到退作業]
driver.get('https://cis.ncu.edu.tw/HumanSys/student/stdSignIn')

#跳轉頁面[ 新增簽到頁面]
driver.find_element_by_xpath('//*[@id="table1"]/tbody/tr[2]/td[6]/a[1]').click()

#輸入工作內容
driver.find_element_by_xpath('//*[@id="AttendWork"]').clear
driver.find_element_by_xpath('//*[@id="AttendWork"]').send_keys(work)


#檢查目前簽到狀態(透過簽到是否存在來判定)

if len(driver.find_elements_by_xpath('//*[@id="signin"]')) == 1:
    #新增簽到
 #   driver.find_element_by_xpath('//*[@id="signin"]').click()
    print("新增簽到")
elif len(driver.find_elements_by_xpath('//*[@id="signout"]')) == 1:
    #新增簽退
#    driver.find_element_by_xpath('//*[@id="signout"]').click()
    print("新增簽退")




#關閉視窗[新增簽退(功能)]
driver.close()
