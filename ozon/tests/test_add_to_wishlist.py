from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage
from ozon.pages.products_page import ProductsPage
from ozon.pages.filters_page import FiltersPage
from ozon.pages.my_ozon import MyOzonPage
from ozon.pages.wishlist_page import WishlistPage


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

    wp = WishlistPage(driver)
    wp.get_names()

    product_name_pp_1 = pp.get_product_name_1()
    product_name_pp_2 = pp.get_product_name_2()

    product_name_wp_1 = wp.get_product_name_1()
    product_name_wp_2 = wp.get_product_name_2()

    wp.compare_names(product_name_pp_1, product_name_wp_1)
    wp.compare_names(product_name_pp_2, product_name_wp_2)

    wp.clear_wishlist()

    print('FINISH TEST ADD TO WISHLIST')
