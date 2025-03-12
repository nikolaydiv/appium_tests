from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage
from ozon.pages.products_page import ProductsPage


def test_search_history(appium_driver):
    driver = appium_driver

    print("START TEST SEARCH HISTORY")

    sp = StartPage(driver)
    sp.enter_app()

    mp = MainPage(driver)
    mp.find_by_name()

    pp = ProductsPage(driver)
    pp.various_searches()

    search_name_1 = pp.get_name_search_history_1()
    search_name_2 = pp.get_name_search_history_2()
    search_name_3 = pp.get_name_search_history_3()

    pp.compare_names('nvidia', search_name_1)
    pp.compare_names('iphone', search_name_2)
    pp.compare_names('nike', search_name_3)

    pp.click_clear_search_history()

    print('END TEST SEARCH HISTORY')
