from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ozon.base.base_class import Base


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
        self.click_notif_later()
