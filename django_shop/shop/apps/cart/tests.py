from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.testcases import TestCase
from django.core.files.base import ContentFile

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


from shop.apps.core.models import Product, Variant, Brand, Category
from .utils import CartObj

import time

TEST_IMAGE = '/home/borisov/Downloads/preview.jpeg'


class TestCreateProduct:

    def create_product(self, n=1, count=10, price=40, a_p=40):
        brand = Brand.objects.create(name='Test brand %s' % n)
        category = Category.objects.create(name='Test category %s' % n)
        image = open(TEST_IMAGE, 'rb').read()
        image = ContentFile(image)
        product = Product.objects.create(category=category, brand=brand, name='test product% s' % n, average_price=a_p)
        product.image.save('test_photo.jpg', image)
        Variant.objects.create(product=product, count=count, price=price, size='L')



class TestCartActions(TestCreateProduct, StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.driver = WebDriver()
        self.create_product()


    def wait(self, expr):
        try:
            WebDriverWait(self.driver, 10).until(expr)
        except (NoSuchElementException, TimeoutException):
            return False
        else:
            return True

    def test_add_in_cart(self):
        self.driver.get(self.live_server_url)

        b = self.wait(EC.element_to_be_clickable((By.XPATH,'.//a[@data-action="detail-product"]')))

        self.assertTrue(b, msg='Error: product was not found')

        self.assertTrue(int(self.driver.find_element_by_id('cart-counter').text) == 0)

        #Открыл модальное окно с товаром
        self.driver.find_element_by_xpath('.//a[@data-action="detail-product"]').click()
        time.sleep(2)


        b = self.wait(EC.presence_of_element_located(
            (By.XPATH, './/div[@id="base-shop-modal"]//button[@data-action="order-product"]')))

        self.assertTrue(b, msg='Error: order error')

        # Добаил в корзину
        self.driver.find_element_by_xpath('.//div[@id="base-shop-modal"]//button[@data-action="order-product"]').click()

        time.sleep(2)

        b = self.wait(EC.element_to_be_clickable((By.XPATH, './/a[@id="my-cart"]')))

        self.assertTrue(b, msg='Error: cart was not found')


        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/span[@id="cart-counter" and contains(text(), 1)]')))

        self.assertTrue(b, msg='Error: cart counter dont increment')

        # Открыл корзину
        self.driver.find_element_by_id('my-cart').click()

        b = self.wait(EC.presence_of_element_located((By.XPATH,
                                                       './/div[@id="my-cart-modal"]//tr[@data-id="body-product-cart"]')))
        self.assertTrue(b, msg='Error: product not in cart')

        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 1)]')))

        self.assertTrue(b, msg='Error: wrong count in cart')

        # Добавил еще одну едницу товара
        self.driver.find_element_by_xpath('.//div[@id="my-cart-modal"]'
                                          '//tr[@data-id="body-product-cart"]'
                                          '//button[@data-action="order-product"]').click()

        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 2)]')))

        self.assertTrue(b, msg='Error: Counter dont increment')

        # Отнял одну едницу товара
        self.driver.find_element_by_xpath('.//div[@id="my-cart-modal"]'
                                          '//tr[@data-id="body-product-cart"]'
                                          '//button[@data-action="delete-cart-product"]').click()

        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 1)]')))

        self.assertTrue(b, msg='Error: Counter dont decrement')

        # Проверил, что кол-во единиц товара не может быть меньше одного
        self.driver.find_element_by_xpath('.//div[@id="my-cart-modal"]'
                                          '//tr[@data-id="body-product-cart"]'
                                          '//button[@data-action="delete-cart-product"]').click()

        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]'
            '//span[@data-id="cart-counter-product" and contains(text(), 1)]')))

        self.assertTrue(b, msg='Error: counter after operation delete == 0')

        # Удалил товар
        self.driver.find_element_by_xpath('.//div[@id="my-cart-modal"]'
                                          '//tr[@data-id="body-product-cart"]'
                                          '//a[@data-action="delete-cart-product-all"]').click()

        b = self.wait((lambda _: self.driver.find_element_by_xpath(
            './/div[@id="my-cart-modal"]'
            '//tr[@data-id="body-product-cart"]')))

        self.assertFalse(b, msg='Error: product was not delete after operation delete-all')


    def tearDown(self):
        self.driver.close()

class TestCart(TestCreateProduct, TestCase):

    def setUp(self):
        super().setUp()
        self.count_variants = 30
        for i in range(1, self.count_variants+1):
            self.create_product(n=i, count=i+1, price=i*4)


    def test_cart(self):
        cart = CartObj(self.client)
        for v in Variant.objects.all():
            for i in range(v.count):
                cart.action('add', v.id)

        # Количество товаров в корзине
        self.assertTrue(cart.count == sum(i+1 for i in range(1, self.count_variants+1)), 'cart count error')

        cart.action('add', v.id) # Добавили еще одну единицу последнего товара в корзину, но на складе нет такого кол-ва
        exceed = v.price * v.count

        """
        Сумма всех товаров в которую не входит сумма последнего товара
        кол-во которого превышает кол-во единиц товара на складе
        """
        cart_price, expected_price = cart.total_price, \
                                     sum((i*4)*(i+1) for i in range(1, self.count_variants+1))-exceed

        self.assertTrue(cart_price == expected_price, 'cart total price error: expected %s instead %s' %
                        (cart_price, expected_price))

        self.assertTrue(cart.count == sum(i + 1 for i in range(1, self.count_variants + 1))+1, 'add: cart count error')

        # удаление товара, который был exceed
        cart.action('delete', v.id)
        self.assertTrue(cart.count == sum(i+1 for i in range(1, self.count_variants+1)), 'delete: cart count error')

        #еще раз
        price_one_p = 1 * v.price
        cart.action('delete', v.id)
        cart_price, expected_price = cart.total_price, \
                                     sum((i*4)*(i+1) for i in range(1, self.count_variants+1))-price_one_p
        self.assertTrue(cart_price == expected_price, 'cart total price error: expected %s instead %s' %
                        (cart_price, expected_price))

        # Вернул обратно
        cart.action('add', v.id)
        # узнал сколько осталось ед. текущего товара и высчитал их полную стоимость и кол-во
        count = cart.count_order(v.id)
        all_price = v.price * count
        cart.action('delete_all', v.id)
        self.assertTrue(cart.count ==
                        sum(i + 1 for i in range(1, self.count_variants + 1))-count, 'delete_all: cart count error')

        cart_price, expected_price = \
            cart.total_price, sum((i * 4) * (i + 1) for i in range(1, self.count_variants + 1))-all_price

        self.assertTrue(cart_price == expected_price, 'cart total price error: expected %s instead %s' %
                        (cart_price, expected_price))

        # Полностью очистил корзину
        cart.action('clear', None)
        self.assertTrue(cart.count == 0, 'clear: count')
        self.assertTrue(cart.total_price == 0, 'clear: total')
        self.assertFalse(len(cart.orders), 'clear: len')





