import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='ru.ozon.app.android',
    appActivity='ru.ozon.app.android.ui.start.AppHostActivity',
    newCommandTimeout=300,
    fullReset=False,
    noReset=True,
    dontStopAppOnReset=True,
    skipDeviceInitialization=True
)

appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope="module")
def appium_driver():
    print('start module')
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    print('finish module')
    time.sleep(1)
    driver.quit()
