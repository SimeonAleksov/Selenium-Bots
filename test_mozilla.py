from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("user-agent=John")
driver = webdriver.Chrome("C:\\chromedriver.exe", chrome_options=opts)
driver.get("https://www.whoishostingthis.com/tools/user-agent/")
sleep(60)
