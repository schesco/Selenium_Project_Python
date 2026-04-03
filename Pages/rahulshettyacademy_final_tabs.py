import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PurchasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # CSSLocators
    input_country = (By.ID,"country")
    select_country = (By.XPATH, "//li[normalize-space()='Germany']")
    purchase_Button = (By.XPATH,"//input[@type='submit']")
    Condition_check = (By.CSS_SELECTOR, "label[for='checkbox2']")

    # Actions
    def setCountry(self):
        self.driver.find_element(*self.input_country).send_keys("germa")
        sleep(0.5)
        #self.log.info(f"shop Geclickt")

    def selectCountry(self):
        country = self.wait.until(
            EC.element_to_be_clickable(self.select_country)
        )
        country.click()

    def purchaseProduct(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.purchase_Button)
        )
        button.click()
    def policy(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.Condition_check)
        )
        checkbox.click()


    def readResult_state(self):
        successMassage = self.wait.until(
            EC.visibility_of_element_located(self.Condition_check)
        ).text
        print(successMassage)
