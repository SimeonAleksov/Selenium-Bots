# main.py
import sys
from selenium import webdriver
import generate_users as gen
import save_all_users as save
import tutanota
import facebook
from selenium.webdriver.chrome.options import Options
PROXY = sys.argv[1]  # "XXX.XXX.XXX.XXX:XX"
chrome_proxy = webdriver.ChromeOptions()
chrome_proxy.add_argument(f'--proxy-server={PROXY}')

print("Starting webdriver")
# Changing the user agent in chrome
opts = Options()
opts.add_argument("user-agent=John")
driver = webdriver.Chrome('C:\\chromedriver.exe', chrome_options=opts)

# driver.set_window_position(-3000, 0)
print("webdriver is hidden successfully")

email, first_name, last_name, password, month, day, year = gen.save_text_file()
personal_data = gen.save_text_file()
check_register = tutanota.register(driver, personal_data[0], personal_data[3])

if check_register:
    print("Succesfully created tutanota account")
else:
    print("There was an error")


save.save_users()

if check_register:
    email = email + "@tutanota.com"
    facebook.register(driver, *personal_data)
    facebook.turn_off_desktop_notification_on_register(driver)
else:
    print("has captcha")
    code = tutanota.save_confirmation_code_facebook(driver, email, password)
