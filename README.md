# Автоматизированное тестирование сервиса "Яндекс Самокат"

![Scooter Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-orange)

## 📋 О проекте
Автотесты для веб-приложения аренды самокатов (QA-стенд: [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/)).

### 🧪 Покрытие тестами
1. **Оформление заказа**
   - Позитивные сценарии с разными наборами данных
   - Проверка всех точек входа (верхняя/нижняя кнопки)
   - Валидация подтверждения заказа

2. **Раздел "Вопросы о важном"**
   - Проверка текста во всех пунктах аккордеона

## 🛠 Технологический стек
| Компонент       | Технология          |
|----------------|--------------------|
| Язык           | Python 3.9+        |
| Фреймворк      | Pytest             |
| Браузер        | Firefox            |
| WebDriver      | Selenium 4.x       |
| Отчетность     | Allure Framework   |
| CI/CD          | (может быть добавлен) |

## 🚀 Быстрый старт

### Установка зависимостей
```bash
pip install -r requirements.txt
Запуск тестов
bash
# Все тесты
pytest tests/ --alluredir=allure-results

# Только тесты заказа
pytest tests/test_scooter_order.py -v

# С отчетом Allure
allure serve allure-results
📁 Структура проекта
.
├── tests/
│   ├── test_scooter_order.py       # Тесты оформления заказа
│   └── test_home_page_accordion.py # Тесты аккордеона FAQ
├── pages/
│   ├── base_page.py                # Базовые методы Selenium
│   ├── home_page.py                # POM главной страницы
│   └── order_page.py               # POM страницы заказа
├── locators/
│   ├── locators_home_page.py       # Локаторы главной страницы
│   └── locators_order_page.py      # Локаторы формы заказа
├── data.py                         # Тестовые данные
├── conftest.py                     # Фикстуры Pytest
├── curl.py                         # Конфигурация URL
└── README.md                       # Этот файл
```
## 📊 Генерация отчетов
**Allure Report Example**

Для генерации отчета:
````
bash
allure generate allure-results -o allure-report --clean
allure open allure-report
````
## 📝 Особенности реализации

   - Page Object Pattern - четкое разделение логики и тестов
- Явные ожидания - стабильность при работе с динамическими элементами

- Параметризация - один тест для множества сценариев

- Allure-интеграция - подробные шаги тестов в отчете