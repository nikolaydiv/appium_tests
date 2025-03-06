import datetime
import os
from appium import webdriver


class Base():

    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        ar_word = word
        er_word = result
        assert ar_word == er_word
        print('assert ok')

    def set_start_price(self):  # 250000T
        self.driver.press_keycode(9)
        self.driver.press_keycode(12)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)

    def set_last_price(self):  # 850000T
        self.driver.press_keycode(15)
        self.driver.press_keycode(12)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)
        self.driver.press_keycode(7)

    def delete_values(self):
        for _ in range(7):
            os.system("adb shell input keyevent KEYCODE_DEL")

    def scroll_to_element(self, element):
        self.driver.execute_script("mobile: scroll", {"element": element, "toVisible": True})

    def get_screenshot_wishlist(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'

        screenshots_folder = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'wishlist')

        screenshot_path = os.path.join(screenshots_folder, name_screenshot)

        self.driver.save_screenshot(screenshot_path)

    def get_screenshot_add_to_cart_and_delete(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'

        screenshots_folder = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'add_to_cart_and_delete')

        screenshot_path = os.path.join(screenshots_folder, name_screenshot)

        self.driver.save_screenshot(screenshot_path)
