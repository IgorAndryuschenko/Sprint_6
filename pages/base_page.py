import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Дождаться и переключиться на новую вкладку")
    def switch_to_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Дождаться URL в текущей вкладке")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: text in d.current_url
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

