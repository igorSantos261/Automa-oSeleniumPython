from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""


class LoginIn:

    def __init__(self, driver):
        self.driver = driver
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR, "div.w3-border")

    def find(self, *locator):
        element = WebDriverWait(driver, 30).until(visibility_of_element_located(*locator))
        return element

    def login(self, user, password):

        self.find(self.NOME).send_keys(user)

        self.find(self.PASS).send_keys(password)

        self.find(self.SUBMIT).click()

    def validar(self, value):

        elem = self.find(self.RESULT)

        assert value in elem.text


driver = webdriver.Chrome()
driver.get("C:/Users/IgorSantosAnselmodaS/eclipse-workspace/Selenium_Python/features/steps/html/login.html")
test = LoginIn(driver)
test.login("Reinaldo", "12345")
test.validar("uname=Reinaldo&psw=12345")
driver.quit()
