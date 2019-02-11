from django.contrib.staticfiles.testing import StaticLiveServerTestCase


from selenium.webdriver.firefox.webdriver import WebDriver, WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class TestCartActions( StaticLiveServerTestCase):
    fixtures = ['products_test.json']

    @classmethod
    def setUpClass(cls):
        super().setUp()
        cls.driver = WebDriver()

    def wait(self, expr, error='Error'):
        try:
            WebDriverWait(self.driver, 5).until(expr)
        except TimeoutException:
            self.assertTrue(False, msg=error)

    def test_add_in_cart(self):
        self.driver.get(self.live_server_url)

        self.assertTrue(int(self.driver.find_element_by_id('cart-counter').text) == 0)

        self.driver.find_element_by_xpath('/a[@data-action="detail-product"]').click()
        self.wait( EC.presence_of_all_elements_located(
            (By.XPATH, '/div[@id="base-shop-modal"]//button[@data-action="detail-product"]')))

        self.driver.find_element_by_xpath('/div[@id="base-shop-modal"]//button[@data-action="detail-product"]').click()

        self.wait(EC.element_to_be_clickable((By.XPATH, '/a[@id="my-cart"]')))

        self.assertTrue(int(self.driver.find_element_by_id('cart-counter').text) == 1)

        self.driver.find_element_by_id('my-cart').click()

        self.wait(EC.presence_of_all_elements_located((By.XPATH,
                                                       '/div[@id="my-cart-modal"]//[@data-id="body-product-cart"]')))

        self.assertTrue(int(self.driver.find_element_by_xpath(
            '/div[@id="my-cart-modal"]//[@data-id="cart-counter-product"]').text) == 1)

        self.driver.find_element_by_xpath('/div[@id="my-cart-modal"]'
                                          '//[@data-id="body-product-cart"]'
                                          '//button[@data-action="order-product"]').click()

        self.wait((lambda _: self.driver.find_element_by_xpath(
            '/div[@id="my-cart-modal"]'
            '//[@data-id="body-product-cart"]'
            '//[@data-id="cart-counter-product"][contains(text(), 2)]')))


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()