


from SeleniumReview_Pom_structure.Pages.rahulshettyacademy_client_register import RegisterPage
from SeleniumReview_Pom_structure.Utilities.BaseClass import BaseClass


class TestClientRegisterPage(BaseClass):

    def test_register(self,setup):
        driver = setup
        driver.get("https://rahulshettyacademy.com/client/")

        page = RegisterPage(driver)

        page.open_register()
        page.fill_form("francis", "ngbwa", "francispascal@hotmail.de", "6777898878")
        page.select_occupation("Engineer")
        page.select_gender()
        page.set_password("Fr@ncis1983")
        page.accept_terms()
        page.submit_form()