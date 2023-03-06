from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()  
 
    def check_promo_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_small = self.browser.find_element(*ProductPageLocators.BOOK_NAME_SMALL)
        book_name_text = book_name.text
        book_name_small_text = book_name_small.text
        assert book_name_text == book_name_small_text, "not promo name"

    def check_promo_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_small = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_SMALL)
        book_price_text = book_price.text
        book_price_small_text = book_price_small.text
        assert book_price_text  == book_price_small_text, "not promo price"
  
    def check_success_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "success message is presented, but should not be"    

    def check_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "success message is not disappeared" 



