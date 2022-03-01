from Selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('enter a name: ')
msg = input('enter your message: ')
count = int(input('how many times: '))

input('almost done... \nclick anything: ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

message = driver.find_element_by_class_name('_2S1VP')

for tekrar in range(count):
    message.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click