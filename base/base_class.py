from pathlib import Path
from datetime import datetime, timezone

import allure


class Base:
    """ Base class, containing universal methods """

    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        """Method get current url"""

        get_url = self.driver.current_url
        print("current url " + get_url)


    def assert_data(self, data, result):
        """Method assert data"""

        with allure.step("Check data"):
            assert data == result, 'Bad value data'
            print('Good value data')


    def assert_final_price(self, price, result):
        """Method assert price"""

        with allure.step("Check final price"):
            assert price == result, 'Bad value final price'
            print('Good value final price')


    def assert_url(self, result):
        """Method assert url"""

        with allure.step("Check url"):
            get_url = self.driver.current_url
            assert get_url == result, 'Bad value url'
            print('Good value url')


    def get_screenshot(self):
        """Method for make screenshot in tests"""

        with allure.step("Screenshot saved"):
            folder = "screen"
            now_date = datetime.now(timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
            save_dir = Path(folder)
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir / f'screenshot_{now_date}.png'
            self.driver.save_screenshot(str(save_path))
            print(f'Screenshot saved')




