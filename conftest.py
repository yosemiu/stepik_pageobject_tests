import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.

def pytest_addoption(parser):
    #parser.addoption('--language', action='store', default="en",
                     #help="Choose lang")
    parser.addoption('--language', action='store', default="none",
                     help="Choose lang")

# Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()