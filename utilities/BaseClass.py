import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
<<<<<<< HEAD

    def selectOptionByTexti(self, locator, text):
            sel = Select(locator)
            sel.select_by_visible_text(text)
=======
        print("Hello made some changes1")
        print("Hello made some changes2...")
        print("Hello made some changes3")
        print("Hello made some changes4...")
        print("Hello made some changes5")
        print("Hello made some changes6...")
>>>>>>> fb8307059e41ddb3a61c6c3e1774dfbbf85127af
