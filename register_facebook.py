from selenium import webdriver
import time


def start_facebook_driver(seconds):
    global _inputs
    global _selects
    global _buttons
    global driver

    driver = webdriver.Chrome('C:\\chromedriver.exe')
    driver.get('https://www.facebook.com/')

    time.sleep(2)

    _inputs = driver.find_elements_by_xpath('//form[@id="reg"]//input')
    _selects = driver.find_elements_by_xpath('//form[@id="reg"]//select')
    _buttons = driver.find_elements_by_xpath('//form[@id="reg"]//button')
    time.sleep(seconds)


def facebook_reg(email, first_name, last_name, password, seconds):
    for input in _inputs:
        print input.get_attribute('name')
        if input.get_attribute('name') == 'firstname':
            input.send_keys(first_name)
            time.sleep(3)
        if input.get_attribute('name') == 'lastname':
            input.send_keys(last_name)
            time.sleep(3)
        if input.get_attribute('name') == 'reg_email__':
            input.send_keys(email)
            time.sleep(3)
        if input.get_attribute('name') == 'reg_passwd__':
            input.send_keys(password)
            time.sleep(3)
        if input.get_attribute('name') == 'reg_email_confirmation__':
            input.send_keys(email)
            time.sleep(3)
        if input.get_attribute('name') == 'sex':
            driver.find_elements_by_xpath(".//input[@type='radio' and @value='1']")[0].click()
            time.sleep(3)
        if input.get_attribute('name') == 'websubmit':
            input.click()
    time.sleep(seconds)


def facebook_birhdate(month, day, year, seconds):
    for select in _selects:
        if select.get_attribute('name') == 'birthday_month':
            select.send_keys(month)
            time.sleep(3)
        if select.get_attribute('name') == 'birthday_day':
            select.send_keys(day)
            time.sleep(3)
        if select.get_attribute('name') == 'birthday_year':
            select.send_keys(year)
            time.sleep(3)
    time.sleep(seconds)


def facebook_submit(seconds):
    for button in _buttons:
        if button.get_attribute("name") == 'websubmit':
            button.click()
            print "Creating account . . ."
    time.sleep(seconds)


def facebook_close():
    print "Closing webdriver . . ."
    driver.quit()


def check_error():
    _inputs1 = driver.find_elements_by_xpath('//form[@id="reg"]//input')
    for input in _inputs1:
        if input.get_attribute('name') == "reg_error_inner":
            print input.get_attribute('name')
            return True
    return False

