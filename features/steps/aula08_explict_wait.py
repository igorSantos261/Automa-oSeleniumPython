from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, title_contains
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8080
referencia: http://localhost:8080/html/login.html
"""


class LoginIn:

    def __init__(self, driver):
        self.driver = driver
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR, "div.w3-border")

    def find(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(invisibility_of_element_located(*locator))
    
    def title_contains(self, *locator, timeout=30):
        return WebDriverWait(driver, timeout).until(title_contains(*locator))
    
    def login(self, user, password):

        self.find(self.NOME).send_keys(user)

        self.find(self.PASS).send_keys(password)

        self.find(self.SUBMIT).click()

    def validar(self, value01, value02 ):

        self.find_not(self.SUBMIT)
        
        assert self.title_contains(value01) 

        elem = self.find(self.RESULT)

        assert value02 in elem.text


driver = webdriver.Chrome()
driver.get("http://localhost:8080/html/login.html")
test = LoginIn(driver)
test.login("Reinaldo", "12345")
test.validar("Forms action page","uname=Reinaldo&psw=12345")
driver.quit()
