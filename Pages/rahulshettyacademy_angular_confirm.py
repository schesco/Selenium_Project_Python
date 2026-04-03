
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        #self.log = logging.getLogger(__name__)
        #self.driver.find_element(By.CSS_SELECTOR, "ul li a[href='/angularpractice/shop']").click()

    #Locators
    Iphone_product=(By.XPATH,"(//td//input[1][@id='exampleInputEmail1'])[1]")
    Samsung_product = (By.XPATH, "(//td//input[1][@id='exampleInputEmail1'])[2]")
    Blackberry_product = (By.XPATH, "(//td//input[1][@id='exampleInputEmail1'])[3]")
    Nokia_product = (By.XPATH, "(//td//input[1][@id='exampleInputEmail1'])[4]")
    price_Total = (By.XPATH, "//td[@class='text-right']//h3")
    Checkout = (By.XPATH, "(//button[@type='button'])[7]")

    # actions
    def set_product_number(self,name:str, number=None):

         match name:
            case "iphone X":
                self.wait.until(EC.visibility_of_element_located(self.Iphone_product)).clear()
                self.wait.until(EC.visibility_of_element_located(self.Iphone_product)).send_keys(number)
               # self.log.info(f"set iphone X")
            case "Samsung Note 8":
                self.wait.until(EC.visibility_of_element_located(self.Samsung_product)).clear()
                self.wait.until(EC.visibility_of_element_located(self.Samsung_product)).send_keys(number)
                #self.log.info(f"set iphone X")
            case "Blackberry":
                self.wait.until(EC.visibility_of_element_located(self.Blackberry_product)).clear()
                self.wait.until(EC.visibility_of_element_located(self.Blackberry_product)).send_keys(number)
                #self.log.info(f"set iphone X")
            case "Nokia Edge":
                self.wait.until(EC.visibility_of_element_located(self.Nokia_product)).clear()
                self.wait.until(EC.visibility_of_element_located(self.Nokia_product)).send_keys(number)
                #self.log.info(f"set iphone X")



    def give_price_total(self):
        TotalAmount=self.driver.find_element(*ConfirmPage.price_Total).text
        #self.log.info(f"Price Total{TotalAmount}")
        print(f"Price Total{TotalAmount}")
        pass

    def Check_out(self):
        check = self.wait.until(
            EC.element_to_be_clickable(ConfirmPage.Checkout)
        )
        check.click()
        #self.driver.find_element().click()
        pass
