from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math 

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)

#  В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

# Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

# Метод для получения проверочного кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #WebDriverWait(self.browser, 10).until(
                #EC.alert_is_present())
        #try:
            #alert = self.browser.switch_to.alert
            #alert_text = alert.text
            #print(f"Your code: {alert_text}")
            #alert.accept()
       # except NoAlertPresentException:
            #print("No second alert presented")
      