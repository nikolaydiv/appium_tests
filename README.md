Проба разных тестов на Appium. No NDA data.

На данный момент имеются:
1. seekers_notes/[sn_by_pixel_1422.py](https://github.com/nikolaydiv/appium_tests/blob/main/seekers_notes/sn_by_pixel_1422.py) - запуск SN на девайсе с разрешением 1422 и прохождение начального туториала. Все действия осуществляются через тапы на пиксели.
2. seekers_notes/[sn_by_image_1422.py](https://github.com/nikolaydiv/appium_tests/blob/main/seekers_notes/sn_by_image_1422.py) - запуск SN и осуществление действий через сравнение изображений. Для девайсов с разрешением 1422.
3. seekers_notes/sn_offers/[offers.py](https://github.com/nikolaydiv/appium_tests/blob/main/seekers_notes/sn_offers/offers.py) - автоматизация проверки пула офферов определенного типа в SN.
4. tests/[test_add_to_wishlist.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_add_to_wishlist.py) - запуск OZON, проставление фильтров, добавление товаров в список желаемого, проверка соответствия добавленных итемов, очистка списка желаемого, проверка очистки списка желаемого.
5. tests/[test_add_to_cart_and_delete.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_add_to_cart_and_delete.py) - запуск OZON, добавление товаров в корзину, проверка соответствия добавленных товаров, очистка корзины, проверка очистки корзины.
6. tests/[test_find_by_article.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_find_by_article.py) - запуск OZON, поиск товара через ввод артикула, проверка корректности найденного итема.
7. tests/[test_find_by_name.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_find_by_name.py) - запуск OZON, поиск товара по названию, проверка соответствия найденных итемов.
8. tests/[test_search_history.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_search_history.py) - запуск OZON, ввод нескольких поисковых запросов, проверка сохранения и соответствия ранее введенных запросов, проверка очистки истории поиска.
