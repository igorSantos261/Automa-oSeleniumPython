from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium_firefox import Firefox


#ff = Firefox()
#ff.get('https://www.google.com')

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\IgorSantosAnselmodaS\AppData\Local\Programs\Python\Python310\Scripts\geckodriver.exe', options=options)
driver.get('https://mgmt.vendas.qa1.vgn.internal.timbrasil.com.br/comissionamento-poseidon')



driver.close()

#driver = webdriver.Firefox()

#driver.get('https://mgmt.vendas.qa1.vgn.internal.timbrasil.com.br/comissionamento-poseidon')
