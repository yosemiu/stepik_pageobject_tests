from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    BOOK_NAME_SMALL = (By.CSS_SELECTOR, "div:first-child>.alertinner>strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_PRICE_SMALL = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div:first-child>.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_CART = (By.CSS_SELECTOR, "span.btn-group>a.btn-default")
    
class BasketPageLocators():
    NO_EMPTY_CART_TEXT = (By.CSS_SELECTOR, "div.basket-title.hidden-xs>div.row>h2")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "div#content_inner>p")
    
    
