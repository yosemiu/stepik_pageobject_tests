from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


# создаем структуру теста для метода add_product_to_basket
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(2)
    page.check_promo_name()
    page.check_promo_price()
    #time.sleep()

# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()     
    page.solve_quiz_and_get_code()
    #time.sleep(2)
    page.check_success_message_not_present()
    #time.sleep(2)

# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.check_success_message_not_present()
    time.sleep(2)

# Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = LoginPage(browser, link)
    page.open()
    page.add_product_to_basket()     
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_success_message_disappeared()
    time.sleep(2)

# Добавляем в файл c тестами test_product_page.py новые тесты: 
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.no_books_in_cart()
    page.empty_cart_text_is_here()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_books_in_cart()
    page.empty_cart_text_is_here()

# В файле test_product_page.py добавьте новый класс для тестов TestUserAddToBasketFromProductPage.
#Добавьте туда уже написанные тесты test_guest_cant_see_success_message и test_guest_can_add_product_to_basket и переименуйте, заменив guest на user. 

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Fp!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        time.sleep(2)
        page.check_promo_name()
        page.check_promo_price()
        time.sleep(2)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)
        page.check_success_message_not_present()
        time.sleep(2)
