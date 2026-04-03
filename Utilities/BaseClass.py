import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseClass:

    @pytest.fixture
    def setup(self):
        chrome_options = Options()

        if os.getenv("CI"):
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.maximize_window()
        else:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()

        yield driver
        driver.quit()