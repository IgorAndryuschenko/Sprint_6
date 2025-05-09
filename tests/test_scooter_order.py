from pages.home_page import HomePageScooter
from pages.order_page import *
from tests.conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
import data



class TestScooterOrder:
    @allure.title("Проверка позитивного сценария заказа самоката")
    @pytest.mark.parametrize("data, entry_point", data.DataScooterOrder.test_cases)
    def test_scooter_order(self, driver, data, entry_point):

        test_flow = OrderPage(driver)
        # 1. Клик по кнопке
        if entry_point == "header":
            test_flow.click_bottom_order_header()
        else:
            test_flow.scroll_to_bottom_order_middle()
            test_flow.click_bottom_order_middle()

        # 2. Заполнение формы и клик Далее
        test_flow.fill_data (
            name=data ["name"], surname=data["surname"], address=data["address"], metro=data["metro"], phone=data["phone"])
        test_flow.click_button_further()
        # 3. Заполнение формы Про аренду и клик Заказать
        test_flow.input_date(date=data["date"])

        if entry_point == "header":
            test_flow.input_orger_period_1()
        else:
            test_flow.input_orger_period_2()

        test_flow.click_button_order()

        # 4. Проверка подтверждения заказа
        assert test_flow.is_order_confirmed(), "Нет подтверждения заказа"
        test_flow.click_button_yes()

        assert test_flow.order_has_been_placed(), "Нет баннера об успешном оформлении"
        test_flow.click_button_status()

        # 5. Проверка перехода на главную
        home_page = HomePageScooter(driver)
        home_page.click_scooter_logo()
        assert "/" in driver.current_url, "Не вернулись на главную"

        # 6. Проверка перехода в Дзен
        home_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
        assert "dzen.ru" in driver.current_url