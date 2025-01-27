# 1422 offers automation
import base64
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import cv2
from tags_functions import (update_tags_11_1_function, update_tags_10_1_function, update_tags_9_1_function,
                            update_tags_3_1_function)

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.mytona.seekersnotes.android',
    appActivity='.GameStartActivity',
    newCommandTimeout=300,
    fullReset=False,
    noReset=True,
    dontStopAppOnReset=True,
    skipDeviceInitialization=True
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

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            cls.driver.quit()

    def start_video(self):
        self.driver.start_recording_screen()

    def stop_video(self, output_file):
        encoded_video = self.driver.stop_recording_screen()
        with open(output_file, "wb") as video_file:
            video_file.write(base64.b64decode(encoded_video))

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

    def is_it_element(self, ticket_template: str) -> bool:
        screenshot_path = self.save_screenshot("is_it_element.png")
        self.driver.save_screenshot(screenshot_path)
        screenshot = cv2.imread(screenshot_path)
        template_path = os.path.join(os.getcwd(), ticket_template)

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

    def release_and_request(self):
        self.driver.tap([(1200, 710)])  # release
        self.driver.tap([(1200, 645)])  # request
        self.driver.tap([(1200, 710)])
        self.driver.tap([(1200, 645)])

    def first_steps(self):
        while self.is_it_element('templates/sn/offers/play.png') is False:
            time.sleep(10)
        self.find_and_tap('templates/sn/offers/play.png')
        time.sleep(5)
        self.driver.tap([(2200, 65)])  # settings mm
        time.sleep(0.5)
        self.driver.tap([(2025, 310)])  # cheats settings
        time.sleep(0.5)
        self.driver.tap([(2010, 160)])  # close settings
        time.sleep(0.5)
        self.driver.tap([(1719, 213)])  # cheats mm
        time.sleep(0.5)
        self.driver.tap([(1640, 150)])  # lvl_up off
        time.sleep(0.5)
        self.driver.tap([(1250, 525)])  # no tutor
        time.sleep(0.5)
        self.driver.tap([(1097, 213)])  # payer
        time.sleep(0.5)
        self.driver.tap([(1217, 728)])  # payer ok
        time.sleep(0.5)

    def second_steps(self):
        self.release_and_request()
        for i in range(1, 7):
            self.driver.tap([(1100, 334)])  # +1 lvl
        self.driver.tap([(1094, 400)])  # 7 lvl
        time.sleep(3)
        self.driver.tap([(0, 0)])
        self.driver.tap([(0, 0)])  # skip hook
        time.sleep(3)
        self.driver.tap([(1480, 740)])  # ok after lvl up
        time.sleep(1)
        self.driver.tap([(1200, 970)])  # daily gift continue
        time.sleep(5)
        while self.is_it_element('templates/sn/offers/close_x.png') is True:
            self.driver.back()
            time.sleep(7)
        self.driver.tap([(1325, 647)])  # friend cheat
        time.sleep(1)
        self.driver.tap([(150, 930)])  # back to mm from friend
        time.sleep(5)
        while self.is_it_element('templates/sn/offers/close_x.png') is True:
            self.driver.back()
            time.sleep(5)
        self.driver.tap([(230, 400)])  # tap key me
        time.sleep(3)
        self.driver.tap([(2200, 50)])  # complete key me (brief)
        time.sleep(3)
        self.driver.tap([(1550, 1000)])  # complete key me (debrief)
        time.sleep(3)
        self.driver.tap([(1480, 730)])  # OK give 10 access
        time.sleep(2)
        self.driver.back()  # close me window
        time.sleep(2)
        self.driver.tap([(230, 400)])  # tap first quest
        time.sleep(3)
        self.driver.tap([(2200, 50)])  # complete first quest (brief)
        time.sleep(3)
        self.driver.tap([(1550, 1000)])  # complete first quest (debrief)

    def first_offer(self):
        time.sleep(10)
        while self.is_it_element('templates/sn/offers/offer_template.png') is False:
            self.driver.back()
            time.sleep(5)
        if self.is_it_element('templates/sn/offers/offer_template.png') is True:
            self.save_screenshot("lto_1.png")
            self.driver.back()
        time.sleep(5)
        while self.is_it_element('templates/sn/offers/close_x.png') is True:
            self.driver.back()
            time.sleep(5)
        self.driver.tap([(1719, 213)])  # cheats mm
        time.sleep(0.5)
        self.driver.tap([(975, 206)])  # offers
        time.sleep(0.5)
        self.driver.tap([(666, 213)])  # triggers
        time.sleep(0.5)
        self.driver.tap([(600, 460)])  # some trigger
        time.sleep(0.5)
        self.driver.tap([(1140, 360)])  # tap input field
        self.driver.press_keycode(67)  # delete value
        self.driver.press_keycode(10)  # enter 3
        self.driver.hide_keyboard()
        self.driver.tap([(1000, 560)])  # tap set
        time.sleep(5)
        while self.is_it_element('templates/sn/offers/offer_template.png') is False:
            self.driver.back()
            time.sleep(5)
        if self.is_it_element('templates/sn/offers/offer_template.png') is True:
            self.save_screenshot("oto_1.png")
            self.driver.back()
            time.sleep(2)
            self.driver.tap([(990, 920)])  # confirm oto close

    def test_offer_11(self) -> None:
        self.first_steps()
        update_tags_11_1_function()
        self.second_steps()
        time.sleep(10)
        self.first_offer()
        # iterations
        for i in range(2, 12):
            function_name = f'update_tags_11_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'lto_{i}.png')
                self.driver.back()
            time.sleep(7)
            while self.is_it_element('templates/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'oto_{i}.png')
                self.driver.back()
                time.sleep(2)
                self.driver.tap([(990, 920)])  # confirm oto close

    def test_offer_10(self) -> None:
        self.first_steps()
        update_tags_10_1_function()
        self.second_steps()
        time.sleep(10)
        self.first_offer()
        # iterations
        for i in range(2, 11):
            function_name = f'update_tags_10_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'lto_{i}.png')
                self.driver.back()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'oto_{i}.png')
                self.driver.back()
                time.sleep(2)
                self.driver.tap([(990, 920)])  # confirm oto close

    def test_offer_9(self) -> None:
        self.first_steps()
        update_tags_9_1_function()
        self.second_steps()
        time.sleep(10)
        self.first_offer()
        # iterations
        for i in range(2, 10):
            function_name = f'update_tags_9_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'lto_{i}.png')
                self.driver.back()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'oto_{i}.png')
                self.driver.back()
                time.sleep(2)
                self.driver.tap([(990, 920)])  # confirm oto close

    def test_offer_3(self) -> None:
        self.first_steps()
        update_tags_3_1_function()
        self.second_steps()
        time.sleep(10)
        self.first_offer()
        # iterations
        for i in range(2, 7):
            function_name = f'update_tags_3_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'lto_{i}.png')
                self.driver.back()
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/close_x.png') is True:
                self.driver.back()
                time.sleep(5)
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            while self.is_it_element('templates/sn/offers/offer_template.png') is False:
                self.driver.back()
                time.sleep(5)
            if self.is_it_element('templates/sn/offers/offer_template.png') is True:
                self.save_screenshot(f'oto_{i}.png')
                self.driver.back()
                time.sleep(2)
                self.driver.tap([(990, 920)])  # confirm oto close


if __name__ == '__main__':
    unittest.main()
