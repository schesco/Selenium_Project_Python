from time import sleep
from SeleniumReview_Pom_structure.Pages.rahulshettyacademy_final_tabs import PurchasePage
from SeleniumReview_Pom_structure.Utilities.BaseClass import BaseClass

class TestPurchasePage(BaseClass):
    #@pytest.mark.xfail
    def testPurchase(self, setup):
        driver = setup

        PurchasePage_object=PurchasePage(driver)
        PurchasePage_object.setCountry()
        PurchasePage_object.selectCountry()
        PurchasePage_object.purchaseProduct()
        PurchasePage_object.policy()
        PurchasePage_object.readResult_state()
        sleep(5)
        driver.quit()




