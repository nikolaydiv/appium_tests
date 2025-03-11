# простой appium тест с установкой, запуском SN на 1422 и прохождением начального тутора
# тапы производятся через сравнение изображений
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import cv2
from seekers_notes.utilities.logger import Logger

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.mytona.seekersnotes.android',
    appActivity='.GameStartActivity',
    newCommandTimeout=300,
    app='C:/Users/dvd10/Downloads/appium_build.apk',  # path to your apk
    androidInstallTimeout=180000,
    fullReset=True
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        Logger.add_start_step(method='setUpClass')
        cls.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )
        Logger.add_end_step(method='setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        Logger.add_start_step(method='tearDownClass')
        if cls.driver:
            cls.driver.quit()
        Logger.add_end_step(method='tearDownClass')

    def save_screenshot(self, filename: str) -> str:
        Logger.add_start_step(method='save_screenshot')
        screenshot_path = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(screenshot_path)
        print(f'Saved screenshot: {filename}')
        Logger.add_end_step(method='save_screenshot')
        return screenshot_path

    def find_and_tap(self, button_filename: str) -> None:
        Logger.add_start_step(method='find_and_tap')
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
        Logger.add_end_step(method='find_and_tap')

    def test_launch_and_tutor(self) -> None:
        print("Start TESN_LAUCNH_AND_TUTOR")
        time.sleep(10)
        self.find_and_tap('templates/sn/launch/apply.PNG')
        time.sleep(10)
        self.find_and_tap("templates/sn/launch/skip.PNG")
        time.sleep(10)
        self.find_and_tap('templates/sn/launch/choose_progress.PNG')
        time.sleep(1)
        if self.driver.is_keyboard_shown():
            self.driver.press_keycode(8)
            self.driver.press_keycode(9)
            self.driver.press_keycode(10)
            self.driver.press_keycode(11)
            self.driver.press_keycode(12)
        self.find_and_tap('templates/sn/launch/confirm_12345.PNG')
        time.sleep(5)
        self.find_and_tap('templates/sn/launch/play.PNG')
        time.sleep(2)
        self.driver.tap([(1200, 800)])
        self.driver.tap([(1200, 800)])
        time.sleep(5)
        self.find_and_tap('templates/sn/first_tutor/helen_1.PNG')
        time.sleep(3)
        self.find_and_tap('templates/sn/first_tutor/helen_2.PNG')
        time.sleep(3)
        self.find_and_tap('templates/sn/first_tutor/item_1.PNG')
        time.sleep(3)
        self.find_and_tap('templates/sn/first_tutor/hint.PNG')
        time.sleep(3)
        self.driver.execute_script('mobile: pinchOpenGesture', {
            'left': 300,
            'top': 300,
            'width': 300,
            'height': 300,
            'percent': 0.5
        })
        time.sleep(0.5)
        self.driver.execute_script('mobile: pinchCloseGesture', {
            'left': 300,
            'top': 300,
            'width': 300 + 200,
            'height': 300 + 200,
            'percent': 1
        })
        self.find_and_tap('templates/sn/first_tutor/item_2.PNG')
        time.sleep(3)
        self.driver.execute_script('mobile: pinchOpenGesture', {
            'left': 300,
            'top': 300,
            'width': 500,
            'height': 500,
            'percent': 0.5
        })
        time.sleep(0.5)
        self.driver.execute_script('mobile: pinchCloseGesture', {
            'left': 300,
            'top': 300,
            'width': 500 - 200,
            'height': 500 - 200,
            'percent': 1
        })
        time.sleep(2)
        self.driver.tap([(0, 0)])
        time.sleep(2)
        self.find_and_tap('templates/sn/first_tutor/item_3.PNG')
        time.sleep(2)
        self.find_and_tap('templates/sn/first_tutor/ok.PNG')
        time.sleep(2)
        print("Finish TEST_LAUNCH_AND_TUTOR")


if __name__ == '__main__':
    unittest.main()
