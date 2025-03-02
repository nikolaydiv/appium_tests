from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ozon.base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = 'new UiSelector().resourceId("ru.ozon.app.android:id/categoryIv").instance(0)'
    smartphones = 'new UiSelector().resourceId("ru.ozon.app.android:id/backgroundV").instance(6)'

    # Getters

    def get_catalog(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.catalog)))
    def get_smartphones(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.smartphones)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('clicked CATALOG')

    def click_smartphones(self):
        self.get_smartphones().click()
        print('clicked SMARTPHONES')

    # Methods

    def choose_smartphones_category(self):
        self.click_catalog()
        self.click_smartphones()
