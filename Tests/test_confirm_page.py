from time import sleep
from Tests.test_purchase_page import TestPurchasePage
from Pages.rahulshettyacademy_angular_confirm import ConfirmPage
from Utilities.BaseClass import BaseClass

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







