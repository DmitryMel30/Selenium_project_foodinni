import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.paper_cups_page import PaperCupsPage
from pages.cup_lids_page import CupLidsPage
from pages.cart_page import CartPage
from pages.payment_page import PaymentPage
from base.base_class import Base

@allure.epic('Test for buy two products')
def test_buy_product(set_up, set_group):
    """
    The product purchase test includes:
        authorization,
        product selection,
        adding product to cart,
        entering user data,
        verifying product data.
    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    print('Start test_buy_product')

    main_step = MainPage(driver)
    main_step.authorization()
    main_step.choice_paper_cup()

    pcp = PaperCupsPage(driver)
    pcp.add_paper_cups_to_cart()

    name_product_1 = pcp.get_info_name_paper_cup_product().text
    price_product_1 = pcp.get_info_price_paper_cup_product().text

    main_step.return_main_page()
    main_step.choice_cup_lids()

    clp = CupLidsPage(driver)
    clp.add_lids_to_cart()

    name_product_2 = clp.get_info_name_lid_product().text
    price_product_2 = clp.get_info_price_lid_product().text

    main_step.return_main_page()
    main_step.enter_cart()

    cp = CartPage(driver)
    cp.product_confirmation()

    pp = PaymentPage(driver)
    pp.payment()


    # Final check block

    b = Base(driver)
    total_price_of_two_products = round(float(price_product_1) + float(price_product_2),2)

    b.assert_data(name_product_1, pp.get_info_final_paper_cup_name())
    b.assert_data(price_product_1, pp.get_info_final_paper_cup_price())

    b.assert_data(name_product_2, pp.get_info_final_lids_name())
    b.assert_data(price_product_2, pp.get_info_final_lids_price())

    b.assert_final_price(total_price_of_two_products, float(pp.get_info_final_price()))


    print('Finish test_buy_product')
    driver.quit()






