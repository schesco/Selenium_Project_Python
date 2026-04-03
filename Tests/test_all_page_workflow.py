from time import sleep

from Pages.rahulshettyacademy_angulare_shop import ShopPage
from Pages.rahulshettyacademy_angular_confirm import ConfirmPage
from Pages.rahulshettyacademy_final_tabs import PurchasePage
from Pages.rahulshettyacademy_angulare_home import HomePage
from Pages.rahulshettyacademy_client_register import RegisterPage
from Utilities.BaseClass import BaseClass
from Utilities.Expected import expect
from Tests.test_shop_page import TestShopPage

class TestAllPageWorkflow(BaseClass):

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



        Shop = ShopPage(driver)
        Shop.set_shop_view()
        Shop.Choose_Product("iphone X")
        Shop.Choose_Product("Blackberry")
        Shop.Choose_Product("Samsung Note 8")
        Shop.Choose_Product("Nokia Edge")
        Shop.CheckOut()


        ConfirmShop = ConfirmPage(driver)
        ConfirmShop.set_product_number("iphone X",5)
        ConfirmShop.set_product_number("Nokia Edge",1)
        ConfirmShop.set_product_number("Samsung Note 8",2)
        ConfirmShop.set_product_number("Blackberry", 4)
        ConfirmShop.give_price_total()
        ConfirmShop.Check_out()


        PurchasePage_object=PurchasePage(driver)
        PurchasePage_object.setCountry()
        PurchasePage_object.selectCountry()
        PurchasePage_object.purchaseProduct()
        PurchasePage_object.policy()
        PurchasePage_object.readResult_state()
        sleep(5)


        driver.get("https://rahulshettyacademy.com/client/")

        page = RegisterPage(driver)

        page.open_register()
        page.fill_form("francis", "ngbwa", "francispascal@hotmail.de", "6777898878")
        page.select_occupation("Engineer")
        page.select_gender()
        page.set_password("Fr@ncis1983")
        page.accept_terms()
        page.submit_form()





