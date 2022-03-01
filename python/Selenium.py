from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

serach_box = input('what do you want to search: ')
answer: input("ready to search:")


driver = webdriver.Chrome()
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys(serach_box)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(2)
driver.execute_script('window.scrollTo(0, 300)')
time.sleep(2)
driver.execute_script('window.scrollTo(0, 600)')
time.sleep(2)
driver.execute_script('window.scrollTo(0, 200)')
time.sleep(2)

driver.quit()
print('\n \n-see you.')