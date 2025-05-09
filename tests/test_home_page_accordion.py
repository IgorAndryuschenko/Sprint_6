from pages.home_page import *
from tests.conftest import *

import allure
import pytest
import data

class TestHomePageAccordion:
    @allure.title("Проверка текста ответов на Вопросы о важном")
    @pytest.mark.parametrize('number, expected_text', data.Data.card_names)
    def test_check_list_price (self, driver, number, expected_text):

        accordion_list= HomePageScooter (driver)
        accordion_list.scroll_to_akkordion_price(number)
        accordion_list.click_akkordion_price(number)
        actual_text = accordion_list.get_text_accordion(number)
        assert  actual_text == expected_text