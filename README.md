📌 Описание проекта:

Этот проект автоматизирует процесс покупки товаров в онлайн-магазине с использованием Selenium, Pytest и Page Object Model.

Сценарий для автоматизации:

Пользователь:
1. Заходит на сайт: www.foodinni.ru/.
2. Нажимает на кнопку авторизации "Вход/Регистрация".
3. Заполняет поле "Логин"(значение: "test_cup_1@example.ru").
4. Заполняет поле "Пароль"(значение: "test_cup_user_1_2025").
5. Нажимает на кнопку "Войти".
6. Нажимает на раздел "Бумажные стаканы".
7. Выбирает в блоке фильтров "Подбор по параметрам": Объем (полный объем), мл "300(430)" и Цвет "Фиолетовый",
далее нажимает на "Показать".
8. Добавляет в корзину бумажные стаканы "Стакан бумажный одноразовый рифленый двухслойный 300 мл МИКС EM90-430-0480".
9. Запоминает название стаканов и их цену.
10. Нажимает на главный логотип компании, в шапке сайта.
11. Нажимает на раздел "Крышки для стаканов".
12. В подразделе "Каталог продукции" выбирает "Пластиковые крышки".
13. Добавляет в корзину крышки "Крышка универсальная для стаканов D90 мм, черная, флип-топ Для стаканов 300мл - 500мл CH-90UB-K"
14. Запоминает название крышек и их цену.
15. Нажимает на главный логотип компании, в шапке сайта.
16. Нажимает на иконку "Корзина".
17. Нажимает на кнопку "Оформить заказ".
18. Переход к заполнению данных, жмет на кнопку "Далее". 
19. Вводит данные о регионе доставки(значение: "Санкт-Петербург").
20. Жмет на кнопку "Далее".
21. Оставляет способ доставки без изменений(значение: "Забрать со склада (СПБ)").
22. Жмет на кнопку "Далее".
23. Выбирает способ оплаты(значение: "Наличными при получении").
24. Жмет на кнопку "Далее".
25. Переходит к блоку заполнения личных данных.
26. Вводит ФИО(значение: "test_cup")
27. Вводит почту(значение: "test_cup_1@example.ru")
28. Вводит телефон(значение: "+79991111111")
29. Проверят, что названия и цены обоих товаров совпадают.
30. Проверяет, что общая сумма товаров совпадает с итоговой на экране.

🏗️ Структура проекта

selenium_project_foodinni/
│── base/                  # Базовые классы для Page Object
│   ├── __init__.py
│   ├── base_class.py       # Базовый класс с общими методами для страниц
│
│── pages/                 # Page Object Model (POM) для различных страниц сайта
│   ├── __init__.py
│   ├── cart_page.py        # Страница корзины
│   ├── cup_lids_page.py    # Страница крышек для стаканов
│   ├── main_page.py        # Главная страница
│   ├── paper_cups_page.py  # Страница бумажных стаканов
│   ├── payment_page.py     # Страница оплаты
│
│── screen/                # Скриншоты для дополнительных проверок
│──test_results/           # Результаты отчета Allure
│── tests/                 # Тестовые сценарии
│   ├── __init__.py
│   ├── conftest.py         # Настройки Pytest
│   ├── test_buy_two_product.py  # Тест на покупку двух товаров
│
│── .gitignore             # Файл для игнорирования ненужных файлов в Git
|── pytest.ini             # Файл настроек конфигурации для Pytest
│── requirements.txt       # Список зависимостей для установки
│── README.md 

🔧 Установка
Для работы Allure необходимо установить его с главного сайта:

https://allurereport.org/docs/install-for-windows/

Клонируйте репозиторий:
git clone https://github.com/DmitryMel30/Selenium_project_foodinni.git
cd selenium_project_foodinni

Установите зависимости из requirements.txt:

pip install -r requirements.txt

🚀 Запуск тестов

Запустите тесты с помощью pytest:

python -m pytest -s -v

для просмотра отчетов, необходимо в командной строке:

 - ввести allure serve test_result/

📜 Используемые технологии:
Python 3.10,
Allure 2,
Selenium 4,
Pytest 8,
Page Object Model (POM),
Chrome WebDriver.