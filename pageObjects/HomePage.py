
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions
from utilities.BaseClass import BaseClass

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "//a[contains(text(),'Sffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffhop')]")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
        # self.driver.find_element_by_xpath("//a[coffffffffffffffffffffffffffffffntains(text(),'Shop')]").click()