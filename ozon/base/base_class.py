import datetime
import os


class Base():

    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        ar_word = word.text
        er_word = result.text
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