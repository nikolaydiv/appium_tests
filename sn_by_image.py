# IN PROGRESS

import time
import unittest

import psutil
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import cv2

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    appPackage='com.mytona.seekersnotes.android',
    appActivity='.GameStartActivity'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     if cls.driver:
    #         cls.driver.quit()

    def save_screenshot(self, filename: str) -> str:
        screenshot_path = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(screenshot_path)
        print(f'Saved screenshot: {filename}')
        return screenshot_path

    def find_and_tap(self, button_filename: str) -> None:
        screenshot_path = self.save_screenshot("screenshot.png")
        self.driver.save_screenshot(screenshot_path)
        screenshot = cv2.imread(screenshot_path)
        template_path = os.path.join(os.getcwd(), button_filename)

        template = cv2.imread(template_path)
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        h, w = template.shape[:2]
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
        result_image_path = os.path.join(os.getcwd(), "result.png")
        cv2.imwrite(result_image_path, screenshot)

        print(f'Результат сохранен в {result_image_path}')
        if max_val < 0.6:
            print(f'Уровень совпадения: {max_val}')
            raise Exception(f'Кнопка {button_filename} не найдена')

        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        self.driver.tap([(center_x, center_y)])
        print(f'Кнопка {button_filename} найдена и нажата по координатам: {center_x}, {center_y}')

    def test_launch_app(self) -> None:
        time.sleep(10)
        self.find_and_tap('apply_button.PNG')
        time.sleep(10)
        self.find_and_tap("skip_button.PNG")
        time.sleep(10)
        self.find_and_tap('choose_progress.PNG')
        if self.driver.is_keyboard_shown():
            self.driver.press_keycode(8)
            self.driver.press_keycode(9)
            self.driver.press_keycode(10)
            self.driver.press_keycode(11)
            self.driver.press_keycode(12)


if __name__ == '__main__':
    unittest.main()
