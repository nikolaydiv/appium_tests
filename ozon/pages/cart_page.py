from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_product = 'new UiSelector().className("androidx.recyclerview.widget.RecyclerView").instance(1)'
    second_product_1 = '(//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/splitV2ItemRootCl"])[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView'
    second_product_2 = '(//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/splitV2ItemRootCl"])[3]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView'
    name_locator = 'text'
    remove_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/removeButton").instance(0)'
    confirm_remove = 'android:id/button1'

    # Getters

    def get_first_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.first_product)))

    def get_first_product_name(self):
        product = self.get_first_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_second_product(self):  # android_uiautomator непостоянный, поэтому взял XPATH
        try:
            print(f'Ищу элемент по первому локатору')
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, self.second_product_1)))
            return self.driver.find_element(AppiumBy.XPATH, self.second_product_1)
        except (TimeoutException, NoSuchElementException):
            print(f'Элемент по первому локатору не найден. Ищу по второму локатору')
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, self.second_product_2)))
                return self.driver.find_element(AppiumBy.XPATH, self.second_product_2)
            except (TimeoutException, NoSuchElementException):
                print('Оба локатора не найдены')
                raise Exception

    def get_second_product_name(self):
        product = self.get_second_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_remove_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.remove_product)))

    def get_confirm_remove(self):
        return WebDriverWait(self.driver, 10).until(
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
        Logger.add_start_step(method='get_names')
        time.sleep(2)
        self.get_screenshot_add_to_cart_and_delete()
        self.get_product_name_1()
        self.get_product_name_2()
        Logger.add_end_step(method='get_names')

    def compare_names(self, name_1, name_2):
        Logger.add_start_step(method='compare_names')
        assert name_1[:50] == name_2[:50]
        print(f'Названия товаров совпадают. Ожидается: {name_1}, имеем: {name_2}')
        Logger.add_end_step(method='compare_names')

    def clear_cart(self):
        Logger.add_start_step(method='clear_cart')
        self.click_remove_product()
        self.click_confirm_remove()
        time.sleep(5)
        self.click_remove_product()
        self.click_confirm_remove()
        time.sleep(5)
        self.get_screenshot_add_to_cart_and_delete()
        print('cleared CART')
        Logger.add_end_step(method='clear_cart')
