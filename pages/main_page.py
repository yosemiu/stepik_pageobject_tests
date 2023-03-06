from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators

#class MainPage(BasePage):
#    def go_to_login_page(self):
#        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        login_link.click()  
#        return LoginPage(browser=self.browser, url=self.browser.current_url) 


# заглушка класса
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


#создаем метод проверяющий наличие ссылки
#    def should_be_login_link(self):
#        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

