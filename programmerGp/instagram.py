from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instagram:
    def __init__(self, username, password):
        self.user = username
        self.password = password
        self.driver = webdriver.Chrome()

    def ClosePage(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        user_name = driver.find_element_by_xpath('//input[@name= "username" ]')
        user_pass = driver.find_element_by_xpath('//input[@name = "password"]')
        user_name.send_keys(self.user)
        user_pass.send_keys(self.password)
        user_pass.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.get('https://www.instagram.com/_m._.ali/')
        
        
        #log_user = driver.find_element_by_name('username').send_keys('_m._.ali')
        #log_pass = driver.find_element_by_name('password').send_keys(1045421067)
        #enter_button = driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').send_keys(Keys.ENTER)

    def like(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/', hashtag,'/')     
        
        pic = []
        for tekrar in range(1, 2):
            try:
                driver.execute_script('windows.scrollTo(0, documents.body.scrollHeight)')
                href = driver.find_elements_by_tag_name('a')
                pics = [element.get_attribute('href') for element in href if '.com/p/' in element.get_attribute('href')]
            except Exception:
                continue

            for pic in pics:
                driver.get(pic)
                try:
                    time.sleep(random.randint(1, 3))
                    driver.find_element_by_xpath('//span[@area-label="Like"]').click()
                except Exception:
                    time.sleep(1)

username = '_m._.ali'
password = 1045421067

test = instagram(username, password)
test.Login()

hashtag = 'python'
while True:
    try:
        test.like(hashtag)

    except Exception:
        test.CloseBrower()
        time.sleep(5)
        test = instagram(username, password)
        test.Login()