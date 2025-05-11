from tests.conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
import data



class TestScooterOrder:
    @allure.title("Проверка позитивного сценария заказа самоката")
    @pytest.mark.parametrize("test_data", data.DataScooterOrder.test_cases)
    def test_scooter_order(self, order_page, home_page, test_data):

        # 1. Клик по кнопке
        getattr(order_page, f"start_order_from_{test_data['entry_method']}")()

        # 2. Заполнение формы и клик Далее
        order_page.fill_data (
            name=test_data ["name"],
            surname=test_data["surname"],
            address=test_data["address"],
            metro=test_data["metro"],
            phone=test_data["phone"])
        order_page.click_button_further()

        # 3. Заполнение формы Про аренду и клик Заказать
        order_page.input_date(date=test_data["date"])
        getattr(order_page, f"input_orger_{test_data['period_locator']}")()
        order_page.click_button_order()

        # 4. Проверка подтверждения заказа
        assert order_page.is_order_confirmed(), "Нет подтверждения заказа"
        order_page.click_button_yes()

        assert order_page.order_has_been_placed(), "Нет баннера об успешном оформлении"
        order_page.click_button_status()

        # 5. Проверка перехода на главную
        home_page.click_scooter_logo()
        assert home_page.is_main_page(), "Не вернулись на главную"

        # 6. Проверка перехода в Дзен
        home_page.check_yandex_redirect()
