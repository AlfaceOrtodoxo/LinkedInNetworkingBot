from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time

driver = wb.Firefox()

email = ''
password = ''


def main():
    loadSite()
    login(email, password)
    search()

def search(keyword):
    input_search = driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
    input_search.send_keys(keyword)


def login(email, password):
    input_email = driver.find_element(By.ID, "username")
    input_password = driver.find_element(By.ID, "password")
    input_email.send_keys(email)
    input_password.send_keys(password)
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

def loadSite():
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)



