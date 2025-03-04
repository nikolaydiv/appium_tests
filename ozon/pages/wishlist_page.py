from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ozon.base.base_class import Base
from ozon.pages.products_page import ProductsPage
from ozon.utilities.logger import Logger


class WishlistPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    first_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(0)'
    second_product = 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(1)'
    name_locator = 'tile-name'
    unfav_1 = 'new UiSelector().description("unfavorite-button").instance(0)'
    unfav_2 = 'new UiSelector().description("unfavorite-button")'

    # Getters

    def get_first_product(self): return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.first_product)))

    def get_first_product_name(self):
        product = self.get_first_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_second_product(self): return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.second_product)))

    def get_second_product_name(self):
        product = self.get_second_product()
        return product.find_element(AppiumBy.ACCESSIBILITY_ID, self.name_locator)

    def get_unfav_1(self): return WebDriverWait(self.driver, 10). until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.unfav_1)))

    def get_unfav_2(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.unfav_2)))

    # Actions

    def get_product_name_1(self):
        product_name = self.get_first_product_name().text
        print(f'First product name on wishlist: {product_name}')
        return product_name

    def get_product_name_2(self):
        product_name = self.get_second_product_name().text
        print(f'Second product name on wishlist: {product_name}')
        return product_name

    def click_unfav_1(self):
        self.get_screenshot_wishlist()
        self.get_unfav_1().click()
        print('clicked UNFAV_1')

    def click_unfav_2(self):
        self.get_unfav_2().click()
        print('clicked UNFAV_2')

    # Methods

    def get_names(self):
        self.get_product_name_1()
        self.get_product_name_2()

    def compare_names(self, name_1, name_2):
        Logger.add_start_step(method='compare_names')
        assert name_1 == name_2
        print(f'Названия товаров совпадают. Ожидается: {name_1}, имеем: {name_2}')
        Logger.add_end_step(method='compare_names')

    def clear_wishlist(self):
        self.click_unfav_1()
        self.click_unfav_2()
        self.get_screenshot_wishlist()
        print('CLEARED WISHLIST')
