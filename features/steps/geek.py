from selenium import webdriver
from selenium.webdriver.common.by import By




# instancia e carrega a nossa pagina.
driver = webdriver.Chrome()
driver.get("https://automacaocombatista.herokuapp.com/users/new")

# funcao para deixar a tela cheia.
#driver.fullscreen_window()

# tempo maximo para ler os elementos da pagina, isso na leitura\abertura da pagina,
# nao eh timeout dos elementos.
driver.set_page_load_timeout(10)

# exemplos de elementos de busca de forma explicita.
#driver.find_element_by_id("user_name")
driver.find_element(By.NAME, "user_name")
#driver.find_element_by_class_name("new_user")
driver.find_element(by=By.CLASS_NAME, value="new_user")
#driver.find_element_by_css_selector("#user_lastname")
driver.find_element(by=By.CSS_SELECTOR, value="#user_lastname")
#driver.find_element_by_xpath("//*[@id=\"user_lastname\"]")
driver.find_element(by=By.XPATH, value="//*[@id=\"user_lastname\"]")
#driver.find_element_by_name("user[email]")
driver.find_element(by=By.NAME, value="user[email]")
#driver.find_element_by_link_text("Treinamento")
driver.find_element(by=By.LINK_TEXT, value="Treinamento")
#driver.find_element_by_partial_link_text("Busca de")
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Busca de")
print(driver.current_url)
#print(driver.page_source)
print(driver.title)
driver.quit()