from time import sleep
from SeleniumReview_Pom_structure.Pages.rahulshettyacademy_angulare_shop import ShopPage
from SeleniumReview_Pom_structure.Tests.test_ConfirmPage import TestConfirmPage
from SeleniumReview_Pom_structure.Utilities.BaseClass import BaseClass

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


