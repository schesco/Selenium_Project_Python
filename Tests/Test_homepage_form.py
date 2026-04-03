from time import sleep
import pytest
from unittest import expectedFailure
from SeleniumReview_Pom_structure.Pages.rahulshettyacademy_angulare_home import HomePage
from SeleniumReview_Pom_structure.Utilities.BaseClass import BaseClass
from SeleniumReview_Pom_structure.Utilities.Expected import expect
from SeleniumReview_Pom_structure.Tests.Test_ShopPage import TestShopPage
import time
class TestHomePage(BaseClass):
    #@pytest.mark.xfail
    def testHomepageform(self, setup):
        driver = setup
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.implicitly_wait(10)
        TestName= "Francis"
        TestEmail = "hello@gmail.com"
        TestPassword= "123456"
        TestCheckbox=True
        TestGenderMale=True
        TestGenderfeMale= True
        TestStudent =True
        Testemployed = True



        home = HomePage(driver)


        expect.equal( home.set_name("Francis"), TestName)
        expect.equal(home.set_email("hello@gmail.com"),TestEmail)
        expect.equal(home.set_password("123456"), TestPassword)
        expect.true(home.click_checkbox() == TestCheckbox)
        expect.true(home.select_gender_male() == TestGenderMale)
        expect.true(home.select_gender_female() == TestGenderfeMale)
        expect.true(home.select_student() == TestStudent)
        expect.true(home.select_employed() ==   Testemployed)
        home.set_dob("28")
        sleep(1)
        home.set_dob("03")
        sleep(1)
        home.set_dob("2026")
        sleep(1)
        obj=TestShopPage()
        obj.testShopInput(setup)





