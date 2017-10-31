# tutunota. py

import time
import config_emails as cfg
# XPATH files
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(driver, email, password):
    driver.get(cfg.URL_LOGIN)
    _inputs = driver.find_elements_by_xpath(cfg.XPATH_INPUTS_LOGIN)
    _buttons = driver.find_elements_by_xpath(cfg.XPATH_BUTTONS_LOGIN)

    for input in _inputs:
        if input.get_attribute('id') == 'loginMailAddress':
            input.send_keys(email)
            time.sleep(3)
        if input.get_attribute('id') == 'loginPassphrase':
            input.send_keys(password)
            time.sleep(3)

    for button in _buttons:
        if button.get_attribute('type') == 'submit':
            button.submit()
    time.sleep(4)


def register(driver, email, password):
    driver.get(cfg.URL_REGISTER)
    time.sleep(5)
    _inputs = driver.find_elements_by_xpath(cfg.XPATH_INPUTS_REGISTER)
    _buttons = driver.find_elements_by_xpath(cfg.XPATH_BUTTONS_REGISTER)

    for input in _inputs:
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
            time.sleep(5)

    if has_captcha(driver):
        return False

    for button in _buttons:
        if button.get_attribute('type') == 'submit':
            button.submit()
    try:
        # Added function to wait for page to load
        print("Waiting for page to load . . .")
        el_present = EC.presence_of_element_located((By.ID, 'submitLogin'))
        WebDriverWait(driver, 5).until(el_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    # TODO: check if current window is inbox
    print("Moving on . . . ")
    time.sleep(10)
    return True


def save_confirmation_code_facebook(driver, email, password):
    login(driver, email, password)
    time.sleep(10)
    _subjects = driver.find_elements_by_xpath(cfg.XPATH_INBOX_EMAIL_SUBJECTS)
    for subject in _subjects:
        code = subject.text[0:5]
        if code.isdigit():
            with open('confirm_facebook_codes.txt', 'a') as file:
                file.write(email + ":" + code + '\n')
                file.close()


def has_captcha(driver):
    _inputs = driver.find_elements_by_xpath(cfg.XPATH_INPUTS_LOGIN)
    for input in _inputs:
        if input.get_attribute('id') == 'captcha':
            return True
    return False
