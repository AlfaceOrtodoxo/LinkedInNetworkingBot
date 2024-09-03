from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pyautogui as py
import time

class LinkedInNetworkingBot():
    def __init__(self, email, password, driver, keyword):
        self.email = str(email)
        self.password = str(password)
        self.driver = driver
        self.keyword = str(keyword).title().replace(" ", "%20")

    def loadSite(self):
        self.driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
    
    def login(self):
        input_email = self.driver.find_element(By.ID, "username")
        input_password = self.driver.find_element(By.ID, "password")
        input_email.clear()
        input_password.clear()
        input_email.send_keys(self.email)
        input_password.send_keys(self.password)
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    
    def keywordSearch(self):
        input_search = self.driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
        input_search.send_keys(self.keyword)
        py.press("enter")

    def peopleIdentifier(self):
        namelist = []
        self.driver.get(f"https://www.linkedin.com/search/results/people/?keywords={self.keyword}&origin=SWITCH_SEARCH_VERTICAL")
        time.sleep(5)
        for name in range(1, 11):            
            elements = self.driver.find_elements(By.XPATH, f"/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{name}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]")
            for element in elements:
                namelist.append(element.text)
        return namelist[0:10] 

    def connect(self):
        time.sleep(5)
        for name in self.peopleIdentifier():
            person = self.driver.find_element(By.XPATH, f"//*[text()='{name}']")
            person.click()
            time.sleep(2)
            position = py.locateCenterOnScreen('ConnectButton.png', confidence = 0.8)
            if position:
                try:
                    py.click(position)
                except ValueError as err:
                    print('Unable to connect...')
                    continue
            

Bot = LinkedInNetworkingBot("", "", wb.Firefox(), '')
 
def main():
    Bot.loadSite()
    Bot.login()
    Bot.peopleIdentifier()
    Bot.connect()

main()

    






    


    




