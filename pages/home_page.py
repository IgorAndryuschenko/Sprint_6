from locators.locators_home_page import *
from pages.base_page import *
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import *

class HomePageScooter(BasePage):
    @allure.step("Кликнуть на элемент аккордиона")
    def click_akkordion_price(self, number):
        self.click_on_element(HomePageLocators.accordion_number(number))

    @allure.step("Скролл до элемента аккордиона")
    def scroll_to_akkordion_price(self, number):
        self.scroll_to_element(HomePageLocators.accordion_number(number))

    @allure.step("Получить текст ответа при нажатии на аккордион")
    def get_text_accordion(self, number):
        self.wait_for_element(HomePageLocators.text_response(number))
        return self.get_text_on_element(HomePageLocators.text_response(number))

    @allure.step("Кликнуть на логотип Самокат")
    def click_scooter_logo(self):
        self.click_on_element(HomePageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_on_element(HomePageLocators.YANDEX_LOGO)

    @allure.step("Проверить переход в Дзен через логотип Яндекса")
    def check_yandex_redirect(self):
        self.click_yandex_logo()
        self.switch_to_new_window()
        self.wait_for_url_contains(site_dzen)
        assert site_dzen in self.get_current_url()

    @allure.step("Проверить что текущая страница - главная")
    def is_main_page(self):
        current_url = self.get_current_url()
        return current_url.endswith('/') or 'qa-scooter' in current_url