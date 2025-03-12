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
    search_field = 'ru.ozon.app.android:id/searchTv'
    back_arrow = 'ru.ozon.app.android:id/image'
    clear_search_field = 'ru.ozon.app.android:id/ivClearSearch'
    search_history_1 = 'new UiSelector().description("tagButton").instance(0)'
    search_history_2 = 'new UiSelector().description("tagButton").instance(1)'
    search_history_3 = 'new UiSelector().description("tagButton").instance(2)'
    search_history_content_desc = 'ButtonV3.titleLabel'
    cancel_search = 'ru.ozon.app.android:id/cancelButton'
    clear_search_history = 'ru.ozon.app.android:id/clearBtnAtomView'

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

    def get_search_field(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.search_field)))

    def get_back_arrow(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.back_arrow)))

    def get_clear_search(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.clear_search_field)))

    def get_cancel_search(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.cancel_search)))

    def get_search_history_1(self): return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.search_history_1)))

    def get_text_search_history_1(self):
        history_name = self.get_search_history_1()
        return history_name.find_element(AppiumBy.ACCESSIBILITY_ID, self.search_history_content_desc)

    def get_search_history_2(self): return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.search_history_2)))

    def get_text_search_history_2(self):
        history_name = self.get_search_history_2()
        return history_name.find_element(AppiumBy.ACCESSIBILITY_ID, self.search_history_content_desc)

    def get_search_history_3(self): return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, self.search_history_3)))

    def get_text_search_history_3(self):
        history_name = self.get_search_history_3()
        return history_name.find_element(AppiumBy.ACCESSIBILITY_ID, self.search_history_content_desc)

    def get_clear_search_history(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.clear_search_history)))

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

    def get_name_search_history_1(self):
        name = self.get_text_search_history_1().text
        return name

    def get_name_search_history_2(self):
        name = self.get_text_search_history_2().text
        return name

    def get_name_search_history_3(self):
        name = self.get_text_search_history_3().text
        return name

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

    def click_back_arrow(self):
        self.get_back_arrow().click()
        print('clicked BACK ARROW')

    def click_search_field(self):
        self.get_search_field().click()
        print('clicked SEARCH FIELD')

    def click_clear_search(self):
        self.get_clear_search().click()
        print('clicked CLEAR SEARCH')

    def click_cancel_search(self):
        self.get_cancel_search().click()
        print('clicked CANCEL SEARCH')

    def click_clear_search_history(self):
        self.get_clear_search_history().click()
        print('clicked CLEAR SEARCH HISTORY')

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

    def check_search_by_name(self):
        Logger.add_start_step('check_search_by_name')
        product_1 = self.get_product_name_1()
        product_2 = self.get_product_name_2()
        if 'Nike' in product_1 and 'Nike' in product_2:
            print('CORRECT SEARCH BY NAME')
            self.get_screenshot_find_by_name()
        else:
            print('INCORRECT SEARCH BY NAME')
            self.get_screenshot_find_by_name()
            raise Exception
        Logger.add_end_step('check_search_by_name')

    def various_searches(self):
        Logger.add_start_step(method='various_searches')
        self.click_back_arrow()
        self.click_clear_search()
        self.set_name('iphone')
        self.click_back_arrow()
        self.click_clear_search()
        self.set_name('nvidia')
        self.click_back_arrow()
        self.click_clear_search()
        self.click_cancel_search()
        self.click_search_field()  # нес-ко раз, т.к. последний введенный поиск не всегда сохраняется
        self.click_cancel_search()
        self.click_search_field()
        time.sleep(3)
        self.get_screenshot_search_history()
        Logger.add_end_step(method='various_searches')

    def compare_names(self, name_1, name_2):
        Logger.add_start_step(method='compare_names')
        assert name_1 == name_2
        print(f'История поиска совпадает. Ожидается: {name_1}, имеем: {name_2}')
        Logger.add_end_step(method='compare_names')
