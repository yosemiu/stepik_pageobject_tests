from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
# Ожидаем, что в корзине нет товаров
    def no_books_in_cart(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "div.basket-title.hidden-xs>div.row>h2"), "no empty cart"


# Ожидаем, что есть текст о том что корзина пуста 
    def empty_cart_text_is_here(self):
        assert self.is_element_present(By.CSS_SELECTOR, "div#content_inner"),  "not empty cart text"

