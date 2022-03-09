
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('D:\Drivers\chromedriver.exe')


driver.get('https://www.instagram.com')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username.clear()
username.send_keys("my_username")
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys("my_password")


driver.close()