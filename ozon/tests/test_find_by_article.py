from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage


def test_find_by_article(appium_driver):
    driver = appium_driver

    print("START TEST FIND BY ARTICLE")

    sp = StartPage(driver)
    sp.enter_app()

    mp = MainPage(driver)
    mp.find_by_article()

    print('END TEST FIND BY ARTICLE')
