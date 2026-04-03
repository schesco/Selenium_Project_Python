import logging
from time import sleep

from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    # CSSLocators
    Shop_button = (By.CSS_SELECTOR, "ul li a[href='/angularpractice/shop']")
    Product_elements = (By.XPATH , "//app-card")
    Checkout_Button = (By.XPATH , "//a[@class='nav-link btn btn-primary']")


    # Actions
    def set_shop_view(self):
        self.driver.find_element(*ShopPage.Shop_button).click()
        sleep(0.5)
        #self.log.info(f"shop Geclickt")

    def Choose_Product(self, productName=None):
        Alle_elements=self.driver.find_elements(*ShopPage.Product_elements)
        for Product in Alle_elements:
            if productName in Product.text:
                #self.log.info(f"product name is : {productName}")
                index = Alle_elements.index(Product)
                index_str= str(index+1)
                self.driver.find_element(By.XPATH,f"//app-card[{index_str}]//div[1]//div[2]//button[1]").click()
        return productName


    def CheckOut(self):
        self.driver.find_element(*ShopPage.Checkout_Button).click()
        print("hallo checkout")


