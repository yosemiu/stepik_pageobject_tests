from .base_page import BasePage
from .locators import LoginPageLocators


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

# добавьте в LoginPage метод register_new_user(email, password), который принимает две строки и регистрирует пользователя
    def register_new_user(self, email, password):
        reg_meil = self.browser.find_element(*LoginPageLocators.REGISTER_MEIL)
        reg_meil.send_keys(email)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)  
        reg_pass.send_keys(password) 
        pass_rep = self.browser.find_element(*LoginPageLocators.PASSWORD_REPIT) 
        pass_rep.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
    


