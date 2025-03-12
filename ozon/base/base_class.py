import datetime
import os
import time

import cv2
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

    def set_article(self):
        # 1223426636
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(11)
        self.driver.press_keycode(9)
        self.driver.press_keycode(13)
        self.driver.press_keycode(13)
        self.driver.press_keycode(10)
        self.driver.press_keycode(13)
        self.driver.press_keycode(66)

    def set_name(self, name):
        if name == 'nike':
            self.driver.press_keycode(42)
            self.driver.press_keycode(37)
            self.driver.press_keycode(39)
            self.driver.press_keycode(33)
            self.driver.press_keycode(66)
        elif name == 'iphone':
            self.driver.press_keycode(37)
            self.driver.press_keycode(44)
            self.driver.press_keycode(36)
            self.driver.press_keycode(43)
            self.driver.press_keycode(42)
            self.driver.press_keycode(33)
            self.driver.press_keycode(66)
        elif name == 'nvidia':
            self.driver.press_keycode(42)
            self.driver.press_keycode(50)
            self.driver.press_keycode(37)
            self.driver.press_keycode(32)
            self.driver.press_keycode(37)
            self.driver.press_keycode(29)
            self.driver.press_keycode(66)

    def swipe_to_refresh(self):
        self.driver.execute_script('mobile: scrollGesture', {
            'left': 500,
            'top': 1000,
            'width': 100,
            'height': 800,
            'direction': 'up',
            'percent': 1.0,
            'speed': 3000
        })
        time.sleep(2)

    def delete_values(self):
        for _ in range(7):
            os.system("adb shell input keyevent KEYCODE_DEL")

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

    def get_screenshot_find_by_article(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'

        screenshots_folder = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'find_by_article')

        screenshot_path = os.path.join(screenshots_folder, name_screenshot)

        self.driver.save_screenshot(screenshot_path)

    def get_screenshot_find_by_name(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'

        screenshots_folder = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'find_by_name')

        screenshot_path = os.path.join(screenshots_folder, name_screenshot)

        self.driver.save_screenshot(screenshot_path)

    def get_screenshot_search_history(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'

        screenshots_folder = os.path.join(os.path.dirname(__file__), '..', 'screenshots', 'search_history')

        screenshot_path = os.path.join(screenshots_folder, name_screenshot)

        self.driver.save_screenshot(screenshot_path)

    def save_screenshot(self, filename: str) -> str:
        screenshot_path = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(screenshot_path)
        print(f'Saved screenshot: {filename}')
        return screenshot_path

    def is_it_element(self, template: str) -> bool:
        screenshot_path = self.save_screenshot("is_it_element.png")
        self.driver.save_screenshot(screenshot_path)
        screenshot = cv2.imread(screenshot_path)
        template_path = os.path.join(os.getcwd(), template)

        template = cv2.imread(template_path)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        h, w = template.shape[:2]
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
        result_image_path = os.path.join(os.getcwd(), "is_it_element_result.png")
        cv2.imwrite(result_image_path, screenshot)

        print(f'Max val is_it_element: {max_val}')

        if max_val > 0.6:
            return True
        else:
            return False
