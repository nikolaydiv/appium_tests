from ozon.pages.start_page import StartPage
from ozon.pages.main_page import MainPage
from ozon.pages.products_page import ProductsPage
from ozon.pages.cart_page import CartPage


def test_add_to_cart_and_delete(appium_driver):
    driver = appium_driver

    print("START TEST ADD TO CART AND DELETE")

    sp = StartPage(driver)
    sp.enter_app()

    mp = MainPage(driver)
    mp.choose_smartphones_category()

    pp = ProductsPage(driver)
    product_name_pp_1 = pp.get_product_name_1()
    product_name_pp_2 = pp.get_product_name_2()

    pp.add_to_cart_and_enter()

    cp = CartPage(driver)
    cp.get_names()

    product_name_cp_1 = cp.get_product_name_1()
    product_name_cp_2 = cp.get_product_name_2()

    cp.compare_names(product_name_pp_1, product_name_cp_2)
    cp.compare_names(product_name_pp_2, product_name_cp_1)
    cp.clear_cart()

    empty_cart_text = cp.get_empty_cart_text()
    cp.compare_names(empty_cart_text, 'Корзина пуста')

    # добавить обновление страницы (не надо, после удаления товаров норм сразу становится) и сравнение текста "Корзина пуста"

    print('FINISH TEST ADD TO CART AND DELETE')
