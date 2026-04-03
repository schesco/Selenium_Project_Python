from time import sleep
from SeleniumReview_Pom_structure.Tests.Test_PurchasePage import TestPurchasePage
from SeleniumReview_Pom_structure.Pages.rahulshettyacademy_angular_confirm import ConfirmPage
from SeleniumReview_Pom_structure.Utilities.BaseClass import BaseClass

class TestConfirmPage(BaseClass):
    #@pytest.mark.xfail
    def testConfirmInput(self, setup):
        driver = setup

        ConfirmShop = ConfirmPage(driver)
        ConfirmShop.set_product_number("iphone X",5)
        ConfirmShop.set_product_number("Nokia Edge",1)
        ConfirmShop.set_product_number("Samsung Note 8",2)
        ConfirmShop.set_product_number("Blackberry", 4)
        ConfirmShop.give_price_total()
        ConfirmShop.Check_out()

        by_object=TestPurchasePage()
        by_object.testPurchase(setup)







