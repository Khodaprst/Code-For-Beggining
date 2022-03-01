from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
driver.find_element_by_name('username').send_keys('_m._.ali')
driver.find_element_by_name('password').send_keys(1045421067)
driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').send_keys(Keys.ENTER)
driver.find_element_by_class_name('aOOlW.HoLwm').send_keys(Keys.ENTER)
driver.find_element_by_class_name('XTCLo.x3qfX').send_keys('#Animal')
time.sleep(4)
driver.get('https://www.instagram.com/explore/tags/animal/')
driver.send_keys(Keys.TAB)


#like
#driver.find_element_by_class_name('wpO6b').send_keys(Keys.enter)
#driver.find_element_by_class_name('wpO6b').send_keys(Keys.ENTER)

#driver.find_element_by_class_name('v1Nh3.kIKUG._bz0w').send_keys(Keys.ENTER)

