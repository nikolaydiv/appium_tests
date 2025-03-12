from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage
from ozon.pages.products_page import ProductsPage


def test_find_by_name(appium_driver):
    driver = appium_driver

    print("START TEST FIND BY NAME")

    sp = StartPage(driver)
    sp.enter_app()

    mp = MainPage(driver)
    mp.find_by_name()

    pp = ProductsPage(driver)
    pp.check_search_by_name()

    print('END TEST FIND BY NAME')
