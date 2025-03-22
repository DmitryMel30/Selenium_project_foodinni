import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    """ Class containing locators and methods for the main page """

    url = "https://www.foodinni.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    authorization_button = "//span[@class='item-text text-black fw-normal text-nowrap ']"
    login = "//input[@id='USER_LOGIN']"
    password = "//input[@id='USER_PASSWORD']"
    login_button = "//button[@type='submit']"
    paper_cup_button = "//div[@class='w-48 w-lg-30 w-xxl-12 card card-product category-card mb-']"
    cup_lids_button = "//div[@class='w-48 w-lg-30 w-xxl-12 card card-product category-card']"
    cart_button = "//span[@class='mobile-footer-text text-black fw-normal']"
    authorization_word = "/html/body/header/div[2]/div/div/div[4]/a[1]/span"
    main_label = "//div[@class='col-xxl-2 col-lg-2 pt-lg-2 d-none d-lg-block']"


    # Getters

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization_button)))


    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))


    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))


    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    def get_paper_cup_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.paper_cup_button)))


    def get_cup_lids_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cup_lids_button)))


    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


    def get_authorization_word(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Личный кабинет')]")))


    def get_main_label(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_label)))


    # Actions

    def input_login(self, user_name):
        self.get_login().send_keys(user_name)
        print('Input login')


    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')


    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')


    def click_authorization_button(self):
        self.get_authorization_button().click()
        print('Click authorization button')


    def click_paper_cup_button(self):
        self.get_paper_cup_button().click()
        print('Click paper cup button')


    def click_cup_lids_button(self):
        self.get_cup_lids_button().click()
        print('Click cup lids button')


    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click cart button')


    def click_main_label(self):
        self.get_main_label().click()
        print('Click main label')


    # Methods(steps)

    def authorization(self):
        with allure.step('Authorization'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_authorization_button()
            self.input_login('test_cup_1@example.ru')
            self.input_password('test_cup_user_1_2025')
            self.click_login_button()
            self.assert_data(self.get_authorization_word().text, 'Личный кабинет')


    def choice_paper_cup(self):
        with allure.step('Choice paper cup section'):
            self.click_paper_cup_button()
            self.assert_url('https://www.foodinni.ru/catalog/bumazhnye-stakany/')


    def choice_cup_lids(self):
        with allure.step('Choice cup lids section'):
            self.click_cup_lids_button()
            self.assert_url('https://www.foodinni.ru/catalog/kryshki-dlya-stakanov/')


    def return_main_page(self):
        with allure.step('Return main page'):
            self.click_main_label()
            self.assert_url('https://www.foodinni.ru/')


    def enter_cart(self):
        with allure.step('Enter cart'):
            self.click_cart_button()
            self.assert_url('https://www.foodinni.ru/personal/cart/')




