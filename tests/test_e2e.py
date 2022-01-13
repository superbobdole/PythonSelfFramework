from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait, expected_conditions

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import time
import pytest

# @pytest.mark.usefixtures("setup")



class TestOne(BaseClass):
    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                # Add item into cart
                product.find_element_by_xpath("div/button").click()
        # css type[class*='text in class name']
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        # //div/div/div/table/tbody/tr/td/h3/strong
        blackberry = "₹. 50000"
        print(self.driver.find_element_by_xpath("//div/div/div/table/tbody/tr/td/h3/strong").text)
        assert self.driver.find_element_by_xpath("//div/div/div/table/tbody/tr/td/h3/strong").text == blackberry
        # xpath - //class type[@attribute='attribute text']
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//body/app-root[1]/app-shop[1]/div[1]/app-checkout[1]/div[1]/div[2]").click()
        # good example of css selector be;pw
        self.driver.find_element_by_css_selector("[type='submit']").click()

        successtext = self.driver.find_element_by_class_name("alert-success").text
        assert "Success! Thank you!" in successtext
