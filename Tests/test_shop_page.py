from time import sleep
from Pages.rahulshettyacademy_angulare_shop import ShopPage
from Tests.test_confirm_page import TestConfirmPage
from Utilities.BaseClass import BaseClass

class TestShopPage(BaseClass):
    #@pytest.mark.xfail
    def testShopInput(self, setup):
        driver = setup
        #driver.get("https://rahulshettyacademy.com/angularpractice/")


        Shop = ShopPage(driver)
        Shop.set_shop_view()
        Shop.Choose_Product("iphone X")
        Shop.Choose_Product("Blackberry")
        Shop.Choose_Product("Samsung Note 8")
        Shop.Choose_Product("Nokia Edge")
        Shop.CheckOut()

        ConfirmPage = TestConfirmPage()
        ConfirmPage.testConfirmInput(setup)


