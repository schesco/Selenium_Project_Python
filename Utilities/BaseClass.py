import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseClass:

    @pytest.fixture
    def setup(self):
        # Logger konfigurieren
       # logger = logging.getLogger(__name__)
        #logger.setLevel(logging.INFO)

       # if not logger.handlers:
        #    fileHandler = logging.FileHandler("test.log")
        #    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        #    fileHandler.setFormatter(formatter)
        #    logger.addHandler(fileHandler)

       # logger.info("=== Test startet ===")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()

       # logger.info("Browser gestartet und maximiert")

        yield driver

        #logger.info("Browser wird geschlossen")
        driver.quit()
        #logger.info("=== Test beendet ===")