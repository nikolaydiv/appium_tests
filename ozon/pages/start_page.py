from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from ozon.base.base_class import Base
from ozon.utilities.logger import Logger


class StartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    notif_later = "ru.ozon.app.android:id/remindLater"

    # Getters

    def get_notif_later(self): return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, self.notif_later)))

    # Actions

    def click_notif_later(self):
        self.get_notif_later().click()
        print('clicked NOTIF LATER')

    # Methods

    def enter_app(self):
        Logger.add_start_step(method='enter_app')
        for _ in range(3):
            try:
                self.click_notif_later()
                break
            except StaleElementReferenceException:
                raise Exception('Не удалось запустить тест')
        Logger.add_end_step(method='enter_app')
