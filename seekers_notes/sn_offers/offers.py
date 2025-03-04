# 1422 offers automation
import base64
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
import cv2
from tags_functions import (update_tags_11_1_function, update_tags_10_1_function,
                            update_tags_9_1_function, update_tags_3_1_function)
from seekers_notes.utilities import Logger

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

    def start_video(self):
        Logger.add_start_step(method='start_video')
        self.driver.start_recording_screen()
        Logger.add_end_step(method='start_video')

    def stop_video(self, output_file):
        Logger.add_start_step('stop_video')
        encoded_video = self.driver.stop_recording_screen()
        with open(output_file, "wb") as video_file:
            video_file.write(base64.b64decode(encoded_video))
        Logger.add_end_step(method='stop_video')

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

    def is_it_element(self, ticket_template: str) -> bool:
        Logger.add_start_step(method='is_it_element')
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
        Logger.add_end_step(method='is_it_element')

        if max_val > 0.6:
            return True
        else:
            return False

    def release_and_request(self):
        Logger.add_start_step(method='release_and_request')
        self.driver.tap([(1200, 710)])  # release
        self.driver.tap([(1200, 645)])  # request
        self.driver.tap([(1200, 710)])
        self.driver.tap([(1200, 645)])
        Logger.add_end_step(method='release_and_request')

    def close_popup(self):
        while self.is_it_element('templates/sn/offers/close_x.png'):
            self.driver.back()
            time.sleep(5)

    def wait_for_ticket_lto(self, template, filename):
        while not self.is_it_element(template):
            self.driver.back()
            time.sleep(5)
        if self.is_it_element(template):
            self.save_screenshot(filename)
            self.driver.back()

    def wait_for_ticket_oto(self, template, filename):
        while not self.is_it_element(template):
            self.driver.back()
            time.sleep(5)
        if self.is_it_element(template):
            self.save_screenshot(filename)
            self.driver.back()
            time.sleep(3)
            self.driver.tap([(990, 920)])  # confirm oto close

    def first_steps(self, function):
        Logger.add_start_step(method='first_steps')
        time.sleep(10)
        while self.is_it_element('templates/sn/offers/play.png') is False:
            time.sleep(1)
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
        function()
        self.release_and_request()
        for i in range(1, 7):
            self.driver.tap([(1100, 334)])  # +1 lvl
        self.driver.tap([(1094, 400)])
        time.sleep(3)
        self.driver.tap([(0, 0)])
        self.driver.tap([(0, 0)])  # skip hook
        time.sleep(3)
        self.driver.tap([(1480, 740)])  # ok after lvl up
        time.sleep(1)
        self.driver.tap([(1200, 970)])  # daily gift continue
        time.sleep(5)
        while self.is_it_element('templates/sn/offers/close_x.png') is True:
            self.find_and_tap('templates/sn/offers/close_x.png')
            time.sleep(5)
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
        self.driver.tap([(1486, 731)])  # OK give 10 access
        time.sleep(1)
        self.driver.back()  # close me window
        time.sleep(2)
        self.driver.tap([(230, 400)])  # tap first quest
        time.sleep(3)
        self.driver.tap([(2200, 50)])  # complete first quest (brief)
        time.sleep(3)
        self.driver.tap([(1550, 1000)])  # complete first quest (debrief)
        time.sleep(1)
        self.driver.tap([(0, 0)])
        time.sleep(0.5)
        self.driver.tap([(0, 0)])
        time.sleep(0.5)
        self.driver.tap([(0, 0)])  # skip dialogue

        # first offer
        time.sleep(10)
        while self.is_it_element('templates/sn/offers/ticket_template.png') is False:
            self.driver.back()
            time.sleep(5)
        if self.is_it_element('templates/sn/offers/ticket_template.png') is True:
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
        while self.is_it_element('templates/sn/offers/ticket_template.png') is False:
            self.driver.back()
            time.sleep(5)
        if self.is_it_element('templates/sn/offers/ticket_template.png') is True:
            self.save_screenshot("oto_1.png")
            self.driver.back()
            time.sleep(2)
            self.driver.tap([(990, 920)])  # confirm oto close
        Logger.add_end_step(method='first_steps')

    def test_ticket_11(self) -> None:
        print('Start TEST_TICKET_11')
        self.first_steps(update_tags_11_1_function)
        # iterations
        for i in range(2, 12):
            function_name = f'update_tags_11_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            self.close_popup()
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            self.wait_for_ticket_lto('templates/sn/offers/offer_template.png', f'lto_{i}.png')
            time.sleep(7)
            self.close_popup()
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            self.wait_for_ticket_oto('templates/sn/offers/offer_template.png', f'oto_{i}.png')
        print('Finish TEST_TICKET_11')

    def test_ticket_10(self) -> None:
        print('Start test_ticket_10')
        self.first_steps(update_tags_10_1_function)
        # iterations
        for i in range(2, 11):
            function_name = f'update_tags_10_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            self.close_popup()
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            self.wait_for_ticket_lto('templates/sn/offers/offer_template.png', f'lto_{i}.png')
            time.sleep(7)
            self.close_popup()
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            self.wait_for_ticket_oto('templates/sn/offers/offer_template.png', f'oto_{i}.png')
        print('Finish test_ticket_10')

    def test_ticket_9(self) -> None:
        print('Start test_ticket_9')
        self.first_steps(update_tags_9_1_function)
        # iterations
        for i in range(2, 10):
            function_name = f'update_tags_9_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            self.close_popup()
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            self.wait_for_ticket_lto('templates/sn/offers/offer_template.png', f'lto_{i}.png')
            time.sleep(7)
            self.close_popup()
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            self.wait_for_ticket_oto('templates/sn/offers/offer_template.png', f'oto_{i}.png')
        print('Finish test_ticket_9')

    def test_ticket_3(self) -> None:
        print('Start test_ticket_3')
        self.first_steps(update_tags_3_1_function)
        # iterations
        for i in range(2, 7):
            function_name = f'update_tags_3_{i}_function'
            func = globals().get(function_name)
            func()
            time.sleep(5)
            self.close_popup()
            self.driver.tap([(1719, 213)])  # cheats mm
            self.release_and_request()
            time.sleep(7)
            self.wait_for_ticket_lto('templates/sn/offers/offer_template.png', f'lto_{i}.png')
            time.sleep(7)
            self.close_popup()
            self.driver.tap([(600, 460)])  # tap some trigger
            time.sleep(0.5)
            self.driver.tap([(1000, 560)])  # tap set
            time.sleep(7)
            self.wait_for_ticket_oto('templates/sn/offers/offer_template.png', f'oto_{i}.png')
        print('Finish test_ticket_3')


if __name__ == '__main__':
    unittest.main()
