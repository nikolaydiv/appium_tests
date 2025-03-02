from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage
from ozon.pages.products_page import ProductsPage
from ozon.pages.filters_page import FiltersPage
from ozon.pages.my_ozon import MyOzonPage


def test_wishlist(appium_driver):
    driver = appium_driver

    print("START TEST ADD TO WISHLIST")

    sp = StartPage(driver)
    sp.enter_app()

    mp = MainPage(driver)
    mp.choose_smartphones_category()

    pp = ProductsPage(driver)
    pp.click_filters()

    fp = FiltersPage(driver)
    fp.set_filters()

    pp.get_names_fav_my_ozon()

    mop = MyOzonPage(driver)
    mop.enter_wishlist()
