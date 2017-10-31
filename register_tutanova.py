from selenium import webdriver
import time


def start_email_driver(seconds):
    global driver
    global _inputs
    global _buttons

    driver = webdriver.Chrome('C:\\chromedriver.exe')
    driver.get('https://app.tutanota.com/#register')

    time.sleep(3)

    _inputs = driver.find_elements_by_xpath('//form[@class="recordContainer"]//input')
    _buttons = driver.find_elements_by_xpath('//form[@class="recordContainer"]//button')
    time.sleep(seconds)


def register(email, password, seconds):
    for input in _inputs:
        print input.get_attribute('id')
        if input.get_attribute('id') == 'mailAddress':
            input.send_keys(email)
            time.sleep(3)
        if input.get_attribute('id') == 'newpassword':
            input.send_keys(password)
            time.sleep(3)
        if input.get_attribute('id') == 'newpassword2':
            input.send_keys(password)
            time.sleep(3)
        if input.get_attribute('id') == 'termsInput':
            input.click()
            time.sleep(3)
        time.sleep(seconds)


def final_submit(seconds):
    for button in _buttons:
        if button.get_attribute('type') == 'submit':
            button.submit()

    print "Registering e-mail . . ."
    time.sleep(seconds)





def close():
    print "Registration successfully, closing driver"
    driver.quit()
