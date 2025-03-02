import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
import unittest
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='ru.ozon.app.android',
    appActivity='ru.ozon.app.android.ui.start.AppHostActivity',
    newCommandTimeout=300,
    fullReset=False,
    noReset=True,
    dontStopAppOnReset=True,
    skipDeviceInitialization=True
)

appium_server_url = 'http://localhost:4723'


class OzonAppium(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            cls.driver.quit()

    def start_price(self):  # 250000 т
        self.driver.press_keycode(9)
        self.driver.press_keycode(12)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)

    def last_price(self):  # 850000 т
        self.driver.press_keycode(15)
        self.driver.press_keycode(12)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("assert ok")

    def test_check(self) -> None:
        time.sleep(5)
        notif_later = self.driver.find_element(AppiumBy.ID, "ru.ozon.app.android:id/remindLater")
        notif_later.click()
        time.sleep(1)
        catalog = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("ru.ozon.app.android:id/categoryIv").instance(0)')
        catalog.click()
        time.sleep(1)
        smartphones = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("ru.ozon.app.android:id/backgroundV").instance(6)')
        smartphones.click()
        filters = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(6)')
        filters.click()
        time.sleep(1)
        apple = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(13)')
        apple.click()
        time.sleep(1)
        is_original_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("ru.ozon.app.android:id/cell").childSelector(new UiSelector().text("Оригинальный товар")))')
        is_original = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/toggleSw").instance(0)')
        is_original.click()
        time.sleep(1)
        seller_ozon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OZON")')
        seller_ozon.click()
        time.sleep(1)
        start_price = self.driver.find_element(AppiumBy.ID, "ru.ozon.app.android:id/rangeFromLl")
        start_price.click()
        for _ in range(7):
            os.system("adb shell input keyevent KEYCODE_DEL")
        time.sleep(1)
        self.start_price()
        last_price = self.driver.find_element(AppiumBy.ID, "ru.ozon.app.android:id/rangeToLl")
        last_price.click()
        time.sleep(3)
        for _ in range(7):
            os.system("adb shell input keyevent KEYCODE_DEL")
        self.last_price()
        self.driver.hide_keyboard()
        apply = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("applyButton")')
        apply.click()
        time.sleep(2)
        first_product = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(0)')
        first_product_name_locator = first_product.find_element(AppiumBy.ACCESSIBILITY_ID, "tile-name")
        first_product_name_text = first_product_name_locator.text
        print(first_product_name_text)
        add_to_wishlist_1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(0)')
        add_to_wishlist_1.click()
        second_product = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(1)')
        second_product_name_locator = second_product.find_element(AppiumBy.ACCESSIBILITY_ID, "tile-name")
        second_product_name_text = second_product_name_locator.text
        print(second_product_name_text)
        add_to_wishlist_2 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(1)')
        add_to_wishlist_2.click()
        third_product = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(2)')
        third_product_name_locator = third_product.find_element(AppiumBy.ACCESSIBILITY_ID, "tile-name")
        third_product_name_text = third_product_name_locator.text
        print(third_product_name_text)
        add_to_wishlist_3 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/favIcon").instance(2)')
        add_to_wishlist_3.click()
        my_ozon = self.driver.find_element(AppiumBy.ID, 'ru.ozon.app.android:id/menu_profile')
        my_ozon.click()
        time.sleep(2)
        wishlist = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/ivIcon").instance(0)')
        wishlist.click()
        time.sleep(2)
        wishlist_product_1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(0)')
        wishlist_product_1_locator = wishlist_product_1.find_element(AppiumBy.ACCESSIBILITY_ID, 'tile-name')
        self.assert_word(wishlist_product_1_locator, third_product_name_text)
        wishlist_product_2 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(1)')
        wishlist_product_2_locator = wishlist_product_2.find_element(AppiumBy.ACCESSIBILITY_ID, 'tile-name')
        self.assert_word(wishlist_product_2_locator, second_product_name_text)
        wishlist_product_3 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ru.ozon.app.android:id/contentElementsVAL").instance(2)')
        wishlist_product_3_locator = wishlist_product_3.find_element(AppiumBy.ACCESSIBILITY_ID, 'tile-name')
        self.assert_word(wishlist_product_3_locator, first_product_name_text)


if __name__ == '__main__':
    unittest.main()
