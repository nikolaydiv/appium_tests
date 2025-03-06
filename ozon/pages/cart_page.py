from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium import webdriver
import time

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_product = 'new UiSelector().className("androidx.recyclerview.widget.RecyclerView").instance(1)'
    second_product_1 = 'new UiSelector().className("androidx.recyclerview.widget.RecyclerView").instance(2)'
    second_product_2 = 'new UiSelector().className("androidx.recyclerview.widget.RecyclerView").instance(3)'
    name_locator = 'text'
    remove_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/removeButton").instance(0)'
    confirm_remove = 'android:id/button1'

    # Getters

    def get_first_product(self): return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.first_product)))

    def get_first_product_name(self):
        product = self.get_first_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_second_product(self):  # android_uiautomator непостоянный, подумать
        try:
            print(f'Ищу элемент {self.second_product_1}')
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.second_product_1)))
        except (NoSuchElementException, TimeoutException):
            print(f'Первый локатор не найден. Ищу второй элемент {self.second_product_2}')
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.second_product_2))
            )

    def get_second_product_name(self):
        product = self.get_second_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_remove_product(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.remove_product)))

    def get_confirm_remove(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, self.confirm_remove)))

    # Actions

    def get_product_name_1(self):
        product_name = self.get_first_product_name().text
        print(f'First product name in cart page: {product_name}')
        return product_name

    def get_product_name_2(self):
        product_name = self.get_second_product_name().text
        print(f'Second product name in cart page: {product_name}')
        return product_name

    def click_remove_product(self):
        self.get_remove_product().click()
        print(f'clicked REMOVE PRODUCT')

    def click_confirm_remove(self):
        self.get_confirm_remove().click()
        print(f'clicked CONFIRM REMOVE')

    # Methods

    def get_names(self):
        time.sleep(2)
        self.get_product_name_1()
        self.get_product_name_2()

    def compare_names(self, name_1, name_2):
        assert name_1[:50] == name_2[:50]
        print(f'Названия товаров совпадают. Ожидается: {name_1}, имеем: {name_2}')

    def clear_cart(self):
        self.click_remove_product()
        self.click_confirm_remove()
