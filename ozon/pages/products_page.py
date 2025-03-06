from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
import time

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger


class ProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filters = 'new UiSelector().className("android.view.ViewGroup").instance(6)'
    first_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(0)'
    second_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/tileGridItemCl").instance(1)'
    name_locator = 'tile-name'
    fav_1 = 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(0)'
    fav_2 = 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(1)'
    my_ozon = 'ru.ozon.app.android:id/menu_profile'
    add_to_cart_1 = 'new UiSelector().resourceId("ru.ozon.app.android:id/firstButton").instance(0)'
    add_to_cart_2 = 'new UiSelector().description("ozonAddToCart")'
    cart = 'ru.ozon.app.android:id/menu_cart'

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

    def get_add_to_cart_1(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.add_to_cart_1)))

    def get_add_to_cart_2(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.add_to_cart_2)))

    def get_cart(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.cart)))

    # Actions

    def click_get_filters(self):
        self.get_filters().click()
        print('clicked FILTERS')

    def get_product_name_1(self):
        product_name = self.get_first_product_name().text
        print(f'First product name on products page: {product_name}')
        return product_name

    def get_product_name_2(self):
        product_name = self.get_second_product_name().text
        print(f'Second product name on products page: {product_name}')
        return product_name

    def click_favs(self):
        self.get_fav_1().click()
        print('clicked FAV_1')
        self.get_fav_2().click()
        print('CLICKED FAV_2')

    def click_my_ozon(self):
        self.get_my_ozon().click()
        print('clicked MY OZON')

    def click_add_to_cart_1(self):
        self.get_add_to_cart_1().click()
        print('clicked ADD TO CART 1')

    def click_add_to_cart_2(self):
        self.get_add_to_cart_2().click()
        print('clicked ADD TO CART 2')

    def click_get_cart(self):
        self.get_cart().click()
        print('clicked CART')

    # Methods
    def enter_filters(self):
        Logger.add_start_step(method='enter_filters')
        self.click_get_filters()
        Logger.add_end_step(method='enter_filters')

    def get_names_fav_my_ozon(self):
        Logger.add_start_step(method='get_names_fav_my_ozon')
        self.get_product_name_1()
        self.get_product_name_2()
        self.click_favs()
        self.click_my_ozon()
        Logger.add_end_step(method='get_names_fav_my_ozon')

    def add_to_cart_and_enter(self):
        Logger.add_start_step('add_to_cart_and_enter')
        self.click_add_to_cart_1()
        self.get_product_name_1()
        self.click_add_to_cart_2()
        self.get_product_name_2()
        self.get_screenshot_add_to_cart_and_delete()
        self.click_get_cart()
        Logger.add_end_step('add_to_cart_and_enter')


