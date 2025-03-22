import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CupLidsPage(Base):
    """  Class containing locators and methods for a page with cup lids """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    plastic_lids = "(//a[@href='/catalog/plastikovye-kryshki/'])[3]"
    add_lid_to_cart = "//*[@id='korob-tab-pane-24615']/div[2]/div[2]/a"

    name_lid_product = "//a[@href='/catalog/kryshki-dlya-stakanov/ich-90ub-k-kryshka-universalnaya-dlya-stakanov-d-90-mm-chernaya-flip-top/']"
    price_lid_product = "//*[@id='korob-tab-pane-24615']/div[2]/div[1]/div[2]/span"


    # Getters

    def get_plastic_lids(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plastic_lids)))


    def get_add_lid_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_lid_to_cart)))


    def get_name_lid_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_lid_product)))


    def get_price_lid_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_lid_product)))


    # Actions

    def click_plastic_lids(self):
        self.get_plastic_lids().click()
        print('Click plastic lids')


    def click_add_lid_to_cart(self):
        self.get_add_lid_to_cart().click()
        print('Click add lid to cart')


    # Methods(steps)

    def add_lids_to_cart(self):
        with allure.step('Add lids to cart'):
            self.get_current_url()
            self.click_plastic_lids()
            self.click_add_lid_to_cart()


    def get_info_name_lid_product(self):
        with allure.step('Info about name lids'):
            return self.get_name_lid_product()


    def get_info_price_lid_product(self):
        with allure.step('Info about price lids'):
            return self.get_price_lid_product()





