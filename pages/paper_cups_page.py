import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PaperCupsPage(Base):
    """ Class containing locators and methods for the paper cup page """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    volume_filter = "(//span[@class='smart-filter-parameters-box-title-text'])[2]"
    volume_checkbox = "//label[@for='arrFilter_1447_2901814253']" # выбираем объем 300(430)
    color_filter = "(//span[@class='smart-filter-parameters-box-title-text'])[3]"
    color_checkbox = "//label[@for='arrFilter_1454_1210935977']" # выбираем фиолетовый цвет
    show_button = "//input[@id='set_filter']"
    add_paper_cup_to_cart = "//*[@id='korob-tab-pane-1890']/div[2]/div[2]/a"

    name_paper_cup_product = "//a[@href='/catalog/bumazhnye-stakany/iem90-430-0480-stakan-bumazhnyy-riflenyy-dvukhsloynyy-300-ml-miks/']"
    price_paper_cup_product = "//*[@id='korob-tab-pane-1890']/div[2]/div[1]/div[2]/span"

    # Getters

    def get_volume_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.volume_filter)))


    def get_volume_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.volume_checkbox)))


    def get_color_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_filter)))


    def get_color_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.color_checkbox)))


    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))


    def get_add_paper_cup_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_paper_cup_to_cart)))


    def get_name_cup_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_paper_cup_product)))


    def get_price_cup_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_paper_cup_product)))


    # Actions

    def click_volume_filter(self):
        self.get_volume_filter().click()
        print('Click volume filter')


    def click_volume_checkbox(self):
        self.get_volume_checkbox().click()
        print('Click volume checkbox')


    def click_color_filter(self):
        self.get_color_filter().click()
        print('Click color filter')


    def click_color_checkbox(self):
        self.get_color_checkbox().click()
        print('Click color checkbox')


    def click_show_button(self):
        self.get_show_button().click()
        print('Click show button')


    def click_add_paper_cup_to_cart(self):
        self.get_add_paper_cup_to_cart().click()
        print('Click add_paper_cup_to_cart')


    # Methods(steps)

    def add_paper_cups_to_cart(self):
        with allure.step('Add paper cups to cart'):
            self.get_current_url()
            self.click_volume_filter()
            self.click_volume_checkbox()
            self.click_color_filter()
            self.click_color_checkbox()
            self.click_show_button()
            self.click_add_paper_cup_to_cart()


    def get_info_name_paper_cup_product(self):
        with allure.step('Info name paper cup'):
            return self.get_name_cup_product()


    def get_info_price_paper_cup_product(self):
        with allure.step('Info price paper cup'):
            return self.get_price_cup_product()




