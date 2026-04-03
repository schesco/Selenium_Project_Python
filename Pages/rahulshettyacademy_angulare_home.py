import logging
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)

    # CSSLocators

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    icecream_checkbox = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    #gender_male = (By.CSS_SELECTOR, "#exampleFormControlSelect1 > option:nth-child(1)")
    gender_male = (By.XPATH, "//option[contains(text(),'male')]")
    gender_female = (By.XPATH, "//option[contains(text(),'Female')]")
    employment_student = (By.CSS_SELECTOR, "input[value='option1']")
    employment_employed = (By.CSS_SELECTOR, "input[value='option2']")
    dob = (By.CSS_SELECTOR, "input[name='bday']")
    Shop_button= (By.CSS_SELECTOR, "a[href = '/angularepractice/shop']")

    # Actions
    def set_name(self, value):
        self.driver.find_element(*HomePage.name).send_keys(value)
        return value

    def set_email(self, value):
        self.driver.find_element(*HomePage.email).send_keys(value)
        return value

    def set_password(self, value):
        self.driver.find_element(*HomePage.password).send_keys(value)
        return value

    def click_checkbox(self):
        self.driver.find_element(*HomePage.icecream_checkbox).click()
        checkbox = self.driver.find_element(*HomePage.icecream_checkbox)
        return checkbox.is_selected()

    def select_gender_male(self):
        self.driver.find_element(*HomePage.gender_male).click()
        gender_male=self.driver.find_element(*HomePage.gender_male)
        return gender_male.is_selected()

    def select_gender_female(self):
        self.driver.find_element(*HomePage.gender_female).click()
        gender_male=self.driver.find_element(*HomePage.gender_female)
        return gender_male.is_selected()

    def select_student(self):
        self.driver.find_element(*HomePage.employment_student).click()
        student = self.driver.find_element(*HomePage.employment_student)
        return student.is_selected()

    def select_employed(self):
        self.driver.find_element(*HomePage.employment_employed).click()
        employed = self.driver.find_element(*HomePage.employment_employed)
        return employed.is_selected()

    def set_dob(self, value):
        self.driver.find_element(*HomePage.dob).send_keys(value)
        return value
    