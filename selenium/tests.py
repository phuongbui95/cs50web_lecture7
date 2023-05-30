from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.google.com")

sleep(60)
