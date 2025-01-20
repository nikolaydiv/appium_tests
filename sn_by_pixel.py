# простой appium тест с установкой, запуском SN на 1422 и прохождением начального тутора
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    appPackage='com.mytona.seekersnotes.android',
    appActivity='.GameStartActivity',
    app='C:/Users/dvd10/Downloads/appium_build.apk',  # path to your apk
    fullReset=True
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

    def test_launch_app(self) -> None:
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

    def test_pass_tutor(self) -> None:
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
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
