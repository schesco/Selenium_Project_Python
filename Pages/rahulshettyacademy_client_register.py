import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    # Locatoren
    register_link = (By.CSS_SELECTOR, ".login-wrapper-footer-text")
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    mobile = (By.ID, "userMobile")
    dropdown = (By.CSS_SELECTOR, "select[formcontrolname='occupation']")
    gender_male = (By.CSS_SELECTOR, "input[value='Male']")
    password = (By.ID, "userPassword")
    confirm_password = (By.ID, "confirmPassword")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    submit = (By.ID, "login")

    # Methoden
    def open_register(self):
        self.wait.until(EC.element_to_be_clickable(self.register_link)).click()

    def fill_form(self, first, last, email, mobile):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.mobile).send_keys(mobile)

    def select_occupation(self, text):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.dropdown))
        Select(dropdown).select_by_visible_text(text)

    def select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.gender_male)).click()

    def set_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.confirm_password).send_keys(pwd)

    def accept_terms(self):
        self.wait.until(EC.element_to_be_clickable(self.checkbox)).click()

    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable(self.submit)).click()