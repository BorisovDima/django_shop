from django.contrib.staticfiles.testing import StaticLiveServerTestCase


from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.core.files.base import ContentFile
from shop.apps.core.models import Product, Variant, Brand, Category
import time

TEST_IMAGE = '/home/borisov/Downloads/preview.jpeg'


class TestCartActions( StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.driver = WebDriver()
        brand = Brand.objects.create(name='Test brand')
        category = Category.objects.create(name='Test category')
        image = open(TEST_IMAGE, 'rb').read()
        image = ContentFile(image)
        product = Product.objects.create(category=category, brand=brand, name='test product', average_price=100)
        product.image.save('test_photo.jpg', image)
        Variant.objects.create(product=product, count=10, price=40, size='L')


    def wait(self, expr, error='Error'):
        try:
            WebDriverWait(self.driver, 10).until(expr)
        except TimeoutException:
            self.assertTrue(False, msg=expr)

    def test_add_in_cart(self):
        self.driver.get(self.live_server_url)

        self.wait(EC.element_to_be_clickable((By.XPATH,'.//a[@data-action="detail-product"]')))

        self.assertTrue(int(self.driver.find_element_by_id('cart-counter').text) == 0)

        self.driver.find_element_by_xpath('.//a[@data-action="detail-product"]').click()
        time.sleep(2)


        self.wait(EC.presence_of_element_located(
            (By.XPATH, './/div[@id="base-shop-modal"]//button[@data-action="order-product"]')))

        self.driver.find_element_by_xpath('.//div[@id="base-shop-modal"]//button[@data-action="order-product"]').click()

        time.sleep(2)

        self.wait(EC.element_to_be_clickable((By.XPATH, './/a[@id="my-cart"]')))


        self.wait((lambda _: self.driver.find_element_by_xpath(
            './/span[@id="cart-counter" and contains(text(), 1)]')))


        self.driver.find_element_by_id('my-cart').click()

        self.wait(EC.presence_of_element_located((By.XPATH,
                                                       './/div[@id="my-cart-modal"]//tr[@data-id="body-product-cart"]')))

        self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 1)]')))

        self.driver.find_element_by_xpath('.//div[@id="my-cart-modal"]'
                                          '//tr[@data-id="body-product-cart"]'
                                          '//button[@data-action="order-product"]').click()

        self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 2)]')))



    def tearDown(self):
        self.driver.close()