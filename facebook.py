# facebook.py

import time
import config_facebook as cfg


def login(driver, email, password):
    driver.get(cfg.URL_LOGIN_REGISTER)
    _inputs = driver.find_elements_by_xpath(cfg.XPATH_INPUTS_LOGIN)

    for input in _inputs:
        if input.get_attribute('id') == 'email':
            input.send_keys(email)
            time.sleep(3)
        if input.get_attribute('id') == 'pass':
            input.send_keys(password)
            time.sleep(3)
        if input.get_attribute('type') == 'submit':
            input.submit()
            break
    time.sleep(4)


def register(driver, email, first_name, last_name, password, month, day, year):
    driver.get(cfg.URL_LOGIN_REGISTER)
    _inputs = driver.find_elements_by_xpath(cfg.XPATH_INPUTS_REGISTER)
    _buttons = driver.find_elements_by_xpath(cfg.XPATH_BUTTONS_REGISTER)
    _selects = driver.find_elements_by_xpath(cfg.XPATH_SELECTS_REGISTER)

    # fill all inputs
    for input in _inputs:
        print(input.get_attribute('name'))
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
            driver.find_elements_by_xpath(
                ".//input[@type='radio' and @value='1']")[0].click()
            time.sleep(3)

    # set values in all selects
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

    # submit form
    submit_button = find_submit_button(_buttons)
    submit_button.click()
    time.sleep(5)
    check_errors_on_register(driver, submit_button)
    time.sleep(5)
    # turn_off_desktop_notification_on_register(driver)
    # time.sleep(5)


def check_errors_on_register(driver, submit_button):
    # check for errors after click on register
    _inputs_after_click_register = driver.find_elements_by_xpath(
        cfg.XPATH_INPUTS_REGISTER)
    if _inputs_after_click_register:
        for input in _inputs_after_click_register:
            if input.get_attribute('name') == "reg_error_inner":
                submit_button.click()


def turn_off_desktop_notification_on_register(driver):
    driver.get(cfg.URL_DESKTOP_NOTIFICATIONS)
    cancel = driver.find_element_by_link_text("Not Now")
    if cancel:
        cancel.click()


def find_submit_button(_buttons):
    for button in _buttons:
        if button.get_attribute("name") == 'websubmit':
            return button


def confirm_account(driver, email, password):
    driver.get()
    code = read_code(email)
    return code


def read_code(email):
    # open file with codes and find the one we need
    with open('confirm_facebook_codes.txt', 'r') as file:
        line = file.readline()
        if email in line:
            file.close()
            return line[-5:]
