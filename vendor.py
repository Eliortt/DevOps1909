from selenium import webdriver
from time import sleep
d = webdriver.Chrome()
d.get("https://vendor-dev.spinomenal.com/")
sleep(5)
d.find_element(by="id", value="select2-chosen-8").click()
