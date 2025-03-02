from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
import time

from ozon.base.base_class import Base


class ProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filters = 'new UiSelector().className("android.view.ViewGroup").instance(6)'
    first_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(0)'
    name_locator = 'tile-name'

    # Getters

    def get_filters(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.filters)))

    def get_first_product(self): return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.first_product)

    def get_first_product_name(self):
        first_product = self.get_first_product()
        return first_product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    # Actions

    def click_get_filters(self):
        self.get_filters().click()
        print('clicked FILTERS')

    def get_first_product_text(self):
        product_name_element = self.get_first_product_name()
        product_name = product_name_element.text
        print(f'First product name: {product_name}')

    # Methods
    def click_filters(self):
        self.click_get_filters()
        self.get_first_product_text()

