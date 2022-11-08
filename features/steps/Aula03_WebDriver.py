from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

""""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.html
"""
#Classe Login
class LoginIN:
    
    #Constantes
    def __init__(self, driver):
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        selfRESULT = (By.CSS_SELECTOR, "div.w3-border")


        #driver.get("C:/Users/IgorSantosAnselmodaS/eclipse-workspace/Selenium_Python/features/steps/html/login.html")
    #Função Login
    def login(self, user, password):
        driver.find_element(*self.NOME).send_keys(user)

        driver.find_element(*self.PASS).send_keys(password)

        driver.find_element(*self.SUBMIT).click()

        

    def validar(self, value):

        elem = driver.find_element(*self.RESULT)
        assert value in elem.text


driver = webdriver.Chrome()
driver.get("C:/Users/IgorSantosAnselmodaS/eclipse-workspace/Selenium_Python/features/steps/html/login.html")
#driver.implicitly_wait(20)
#Chamando a Classe "LoginIN"
test = LoginIN(driver)
#chamada das Funções login e validar.
test.login("Reinaldo", "12345")
test.validar("uname=Reinaldo&psw=12345")
#metodo para fechar o navegador
driver.quit()
