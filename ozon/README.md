Несколько сценариев автоматизированных проверок Appium в мобильном приложении OZON для Android.

На данный момент имеются:
1. tests/[test_add_to_wishlist.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_add_to_wishlist.py) - запуск OZON, проставление фильтров, добавление товаров в список желаемого, проверка соответствия добавленных итемов, очистка списка желаемого, проверка очистки списка желаемого.
2. tests/[test_add_to_cart_and_delete.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_add_to_cart_and_delete.py) - запуск OZON, добавление товаров в корзину, проверка соответствия добавленных товаров, очистка корзины, проверка очистки корзины.
3. tests/[test_find_by_article.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_find_by_article.py) - запуск OZON, поиск товара через ввод артикула, проверка корректности найденного итема.
4. tests/[test_find_by_name.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_find_by_name.py) - запуск OZON, поиск товара по названию, проверка соответствия найденных итемов.
5. tests/[test_search_history.py](https://github.com/nikolaydiv/appium_tests/blob/main/ozon/tests/test_search_history.py) - запуск OZON, ввод нескольких поисковых запросов, проверка сохранения и соответствия ранее введенных запросов, проверка очистки истории поиска.
