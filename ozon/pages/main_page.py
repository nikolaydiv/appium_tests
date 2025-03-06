from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = 'new UiSelector().resourceId("ru.ozon.app.android:id/categoryIv").instance(0)'
    smartphones = 'new UiSelector().resourceId("ru.ozon.app.android:id/backgroundV").instance(6)'
    error_logo = 'ru.ozon.app.android:id/errorLogoIv'
    close_error = 'ru.ozon.app.android:id/closeButton'

    # Getters

    def get_catalog(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.catalog)))
    def get_smartphones(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.smartphones)))

    def get_error_logo(self): return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ID, self.error_logo)))

    def get_close_error(self): return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, self.close_error)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('clicked CATALOG')

    def click_smartphones(self):
        self.get_smartphones().click()
        print('clicked SMARTPHONES')

    def click_close_error(self):
        self.get_close_error().click()
        print('closed ERROR')

    # Methods

    def choose_smartphones_category(self):
        Logger.add_start_step(method='choose_smartphones_category')
        # try:
        #     self.click_close_error()
        # except (TimeoutException, NoSuchElementException):
        #     pass
        self.click_catalog()
        self.click_smartphones()
        Logger.add_end_step(method='choose_smartphones_category')
