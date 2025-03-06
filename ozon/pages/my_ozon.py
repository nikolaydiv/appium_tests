from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger

class MyOzonPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    wishlist = 'new UiSelector().className("android.widget.LinearLayout").instance(1)'

    # Getters

    def get_wishlist(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.wishlist)))

    # Actions

    def click_wishlist(self):
        self.get_wishlist().click()
        print('clicked WISHLIST')

    # Methods

    def enter_wishlist(self):
        Logger.add_start_step('enter_wishlist')
        self.click_wishlist()
        Logger.add_end_step('enter_wishlist')
