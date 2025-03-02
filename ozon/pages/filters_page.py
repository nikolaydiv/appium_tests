from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
import time

from ozon.base.base_class import Base


class FiltersPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    apple = 'new UiSelector().className("android.view.ViewGroup").instance(13)'
    is_original_text = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("ru.ozon.app.android:id/cell").childSelector(new UiSelector().text("Оригинальный товар")))'
    is_original_checkbox = 'new UiSelector().resourceId("ru.ozon.app.android:id/toggleSw").instance(0)'
    seller_ozon_checkbox = 'new UiSelector().text("OZON")'
    start_price = 'ru.ozon.app.android:id/rangeFromLl'
    last_price = 'ru.ozon.app.android:id/rangeToLl'
    apply = 'new UiSelector().description("applyButton")'

    # Getters

    def get_apple(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.apple)))

    def get_is_original_text(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.is_original_text)))

    def get_is_original_checkbox(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.is_original_checkbox)))

    def get_seller_ozon_checkbox(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.seller_ozon_checkbox)))

    def get_start_price(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, self.start_price)))

    def get_last_price(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ID, self.last_price)))

    def get_apply(self): return WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, self.apply)))

    # Actions

    def click_apple(self):
        self.get_apple().click()
        print('clicked APPLE')

    def scroll_to_is_original(self):
        self.get_is_original_text()
        print('scrolled to IS ORIGINAL')

    def click_is_original(self):
        self.get_is_original_checkbox().click()
        print('clicked IS ORIGINAL')

    def click_seller_ozon(self):
        self.get_seller_ozon_checkbox().click()
        print('clicked SELLER OZON')

    def click_and_set_start_price(self):
        self.get_start_price().click()
        print('clicked START PRICE')
        time.sleep(1)
        self.delete_values()
        time.sleep(1)
        self.set_start_price()
        print('set START PRICE')
        time.sleep(1)

    def click_and_set_last_price(self):
        self.get_last_price().click()
        print('clicked LAST PRICE')
        time.sleep(1)
        self.delete_values()
        time.sleep(1)
        self.set_last_price()
        print('set LAST PRICE')
        time.sleep(1)

    def click_apply(self):
        self.get_apply().click()
        print('clicked APPLY')

    # Methods
    def set_filters(self):
        self.click_apple()
        self.scroll_to_is_original()
        self.click_is_original()
        self.click_seller_ozon()
        self.click_and_set_start_price()
        self.click_and_set_last_price()
        self.driver.hide_keyboard()
        self.click_apply()
        time.sleep(3)
