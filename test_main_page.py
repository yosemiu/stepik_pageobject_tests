from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
 # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)  
 # открываем страницу
    page.open()                      
 # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()  

# создаем тест на корректность урла логина
def test_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()  
 
# создаем тесты на формы авторизации и регистрации
def test_login_n_refister_forms(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()  