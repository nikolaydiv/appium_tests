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
    second_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/tileGridItemCl").instance(1)'
    name_locator = 'tile-name'
    price_locator = 'price.price'
    fav_1 = 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(0)'
    fav_2 = 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(1)'
    my_ozon = 'ru.ozon.app.android:id/menu_profile'

    # Getters

    def get_filters(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.filters)))

    def get_first_product(self): return WebDriverWait(self.driver, 10). until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.first_product)))

    def get_first_product_name(self):
        product = self.get_first_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_second_product(self): return WebDriverWait(self.driver, 10). until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.second_product)))

    def get_second_product_name(self):
        product = self.get_second_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_fav_1(self): return WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.fav_1)))

    def get_fav_2(self): return WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.fav_2)))

    def get_my_ozon(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.my_ozon)))

    # Actions

    def click_get_filters(self):
        self.get_filters().click()
        print('clicked FILTERS')

    def get_products_text(self):
        product_name_element_1 = self.get_first_product_name()
        product_name_1 = product_name_element_1.text
        print(f'First product name: {product_name_1}')

        product_name_element_2 = self.get_second_product_name()
        product_name_2 = product_name_element_2.text
        print(f'Second product name: {product_name_2}')

    def click_favs(self):
        self.get_fav_1().click()
        print('clicked FAV_1')
        self.get_fav_2().click()
        print('CLICKED FAV_2')

    def click_my_ozon(self):
        self.get_my_ozon().click()
        print('clicked MY OZON')

    # Methods
    def click_filters(self):
        self.click_get_filters()

    def get_names_fav_my_ozon(self):
        self.get_products_text()
        self.click_favs()
        self.click_my_ozon()
