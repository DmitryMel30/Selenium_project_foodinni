import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):
    """ Class containing locators and methods for the shopping cart page """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_button = "//button[@class='btn btn-lg btn-primary text-center basket-btn-checkout']"


    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click check button')


    # Methods(steps)

    def product_confirmation(self):
        with allure.step('Product confirmation'):
            self.get_current_url()
            self.get_screenshot()
            self.click_checkout_button()


