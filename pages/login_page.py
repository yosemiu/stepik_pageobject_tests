from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

# реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login url"

# реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

# реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"



#(*LoginPageLocators.LOGIN_FORM)
#(*LoginPageLocators.REGISTER_FORM)
#(*MainPageLocators.LOGIN_LINK)