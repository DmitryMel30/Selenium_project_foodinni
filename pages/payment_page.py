import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PaymentPage(Base):
    """ Class containing locators and methods for the payment page """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    continue_button_1 = "//*[@id='bx-soa-basket']/div[2]/div[2]/div/button"
    continue_button_2 = "//*[@id='bx-soa-region']/div[2]/div[3]/div/button[2]"
    continue_button_3 = "//*[@id='bx-soa-delivery']/div[2]/div[3]/div/button[2]"
    continue_button_4 = "//*[@id='bx-soa-paysystem']/div[2]/div[3]/div/button[2]"
    city_field = "(//input[@value='84'])[2]"
    payment_field = "//input[@id='ID_PAY_SYSTEM_ID_3']"
    phone_field = "//input[@autocomplete='tel']"
    status_city = "//span[text()='Санкт-Петербург']"
    loading_status = "//div[@id='loading_screen']"

    final_price = "//*[@id='bx-soa-total']/div[2]/div[4]/span[2]"
    final_paper_cup_price = "//*[@id='bx-soa-basket']/div[2]/div/div/div/div[1]/div[3]/div[2]/strong"
    final_lids_price = "//*[@id='bx-soa-basket']/div[2]/div/div/div/div[2]/div[3]/div[2]/strong"
    final_paper_cup_name = "//a[@href='/catalog/bumazhnye-stakany/iem90-430-0480-stakan-bumazhnyy-riflenyy-dvukhsloynyy-300-ml-miks/']"
    final_lids_name = "//a[@href='/catalog/kryshki-dlya-stakanov/ich-90ub-k-kryshka-universalnaya-dlya-stakanov-d-90-mm-chernaya-flip-top/']"


    # Getters

    def get_continue_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_1)))


    def get_continue_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_2)))


    def get_continue_button_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_3)))


    def get_continue_button_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_4)))


    def get_status_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.status_city)))


    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.city_field)))


    def get_payment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_field)))


    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))


    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))


    def get_final_paper_cup_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_paper_cup_price)))


    def get_final_lids_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_lids_price)))


    def get_final_paper_cup_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_paper_cup_name)))


    def get_final_lids_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_lids_name)))


    def get_loading_status(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located((By.XPATH, self.loading_status)))


    # Actions

    def click_continue_button_1(self):
        self.get_continue_button_1().click()
        print('Click continue basket button')


    def click_continue_button_2(self):
        self.driver.execute_script("arguments[0].click();", self.get_continue_button_2()) # принудительный click
        print('Click continue region button')


    def click_continue_button_3(self):
        self.driver.execute_script("arguments[0].click();", self.get_continue_button_3())
        print('Click continue delivery button')


    def click_continue_button_4(self):
        self.driver.execute_script("arguments[0].click();", self.get_continue_button_4())
        print('Click continue paysystem button')


    def click_city_field(self):
        self.get_city_field().click()
        print('Click city field')


    def click_payment_field(self):
        self.get_loading_status()
        self.get_payment_field().click()
        print('Click payment field')


    def click_phone_field(self):
        self.get_loading_status()
        self.get_phone_field().click()
        print('Click phone field')


    def input_city_field(self, city_info):
        self.get_city_field().send_keys(Keys.CONTROL + 'a')
        self.get_city_field().clear()
        self.get_city_field().send_keys(city_info)
        self.get_status_city()
        self.get_city_field().send_keys(Keys.RETURN)
        print('Input city info')


    def input_phone_field(self, phone_number):
        self.get_phone_field().click()
        self.get_phone_field().send_keys(phone_number)
        print('Input phone number')


    # Methods(steps)

    def get_info_final_price(self):
        with allure.step('Info final price'):
            return self.get_final_price().text[:-5].replace(' ', '')


    def get_info_final_paper_cup_price(self):
        with allure.step('Info final paper cup price'):
            return self.get_final_paper_cup_price().text[:-5].replace(' ', '')


    def get_info_final_lids_price(self):
        with allure.step('Info final lids price'):
            return self.get_final_lids_price().text[:-5].replace(' ', '')


    def get_info_final_paper_cup_name(self):
        with allure.step('Info final paper cup name'):
            return self.get_final_paper_cup_name().text


    def get_info_final_lids_name(self):
        with allure.step('Info final lids name'):
            return self.get_final_lids_name().text


    def payment(self):
        with allure.step('Steps for payment page'):
            self.get_current_url()
            self.click_continue_button_1()
            self.click_city_field()
            self.input_city_field('Санкт-Петербург')
            self.click_continue_button_2()
            self.click_continue_button_3()
            self.click_payment_field()
            self.click_continue_button_4()
            self.get_loading_status()
            self.click_phone_field()
            self.input_phone_field('+79991111111')
            self.get_screenshot()

