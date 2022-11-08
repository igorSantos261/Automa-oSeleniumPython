from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def calculate_implicit_wait_time(driver, wait_value):

    # somente entre se tiver valor.
    if wait_value:
        driver.implicitly_wait(wait_value)

    # dou o clique no elemento.
    driver.find_element_by_id("bt01").click()

    # função para pegar o tempo em segundos.
    now = time.time()

    try:
        myelement = driver.find_element_by_id("meuId")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # mostrando que é preciso aplicar somente uma vez.
    # fazendo o teste com o outro botão.
    driver.find_element_by_id("bt02").click()

    try:
        myelement = driver.find_element_by_id("meuId2")

    # caso der erro vai entrar na exceção e imprimir o erro.
    except Exception as x:
        print(x)

    # imprime a media do tempo.
    print(str(int(time.time()-now))+'--Seconds')


driver = webdriver.Chrome()
driver.get("C:/Users/IgorSantosAnselmodaS/eclipse-workspace/Selenium_Python/features/steps/html_2/wait.html")
calculate_implicit_wait_time(driver, 5)
driver.quit()
