from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pyautogui as py
import time

class LinkedInNetworkingBot():
    def __init__(self, email, password, driver, keyword):
        self.email = str(email)
        self.password = str(password)
        self.driver = driver
        self.keyword = str(keyword).title()

    def loadSite(self):
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)
    
    def login(self):
        input_email = self.driver.find_element(By.ID, "username")
        input_password = self.driver.find_element(By.ID, "password")
        input_email.send_keys(self.email)
        input_password.send_keys(self.password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    
    def keywordSearch(self):
        input_search = self.driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
        input_search.send_keys(self.keyword)
        py.press("enter")

    def peopleIdentifier():
        ...

    


    


    




