# простой appium тест с установкой, запуском SN на 1422 и прохождением начального тутора
# тапы производятся попиксельно
import os
import time
import unittest
import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.logger import Logger

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
        project_root = os.path.dirname(os.path.abspath(__file__))
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S.")
        screenshots_folder = os.path.join(project_root, 'screenshots')
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)

        screenshot_folder = os.path.join(screenshots_folder, f'{now_date}')
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

        screenshot_path = os.path.join(screenshot_folder, filename)

        self.driver.save_screenshot(screenshot_path)
        print(f'Saved screenshot: {filename}')
        Logger.add_end_step(method='save_screenshot')
        return screenshot_path

    def test_launch_and_tutor(self) -> None:
        print("Start TEST_LAUNCH_AND_TUTOR")
        time.sleep(10)
        # нажатие ПРИНЯТЬ
        self.driver.tap([(1200, 1000)])
        time.sleep(25)
        # нажатие новой игры слева (слева)
        self.driver.tap([(830, 930)])
        time.sleep(3)
        # ввод 12345 и подтверждение
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(11)
        self.driver.press_keycode(12)
        self.driver.tap([(1200, 430)])
        time.sleep(5)
        # нажатие ИГРАТЬ
        self.driver.tap([(1200, 800)])
        # скип интро ролика
        time.sleep(2)
        self.driver.tap([(1200, 800)])
        self.driver.tap([(1200, 800)])
        time.sleep(5)
        # первое окно с хелен
        self.driver.tap([(1600, 690)])
        time.sleep(3)
        # второе окно с хелен
        self.driver.tap([(1600, 690)])
        time.sleep(3)
        # первый ХО
        self.driver.tap([(1620, 730)])
        time.sleep(3)
        # первый хинт
        self.driver.tap([(1800, 1000)])
        time.sleep(3)
        # зум ин
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
        # подбор хо
        self.driver.tap([(1200, 820)])
        time.sleep(3)
        # зум аут
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
        # финиш тутора и подбор ласт хо
        self.driver.tap([(1200, 800)])
        time.sleep(2)
        self.driver.tap([(640, 580)])
        time.sleep(2)
        self.driver.tap([(1200, 960)])
        time.sleep(5)
        self.save_screenshot('success.png')
        print("Finish TEST_LAUNCH_AND_TUTOR")


if __name__ == '__main__':
    unittest.main()
