from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://192.168.15.1/cgi-bin/device-management-resets.cgi")
driver.maximize_window()

login = driver.find_element(By.ID, 'Loginuser')
login.send_keys('admin')

senha = driver.find_element(By.ID, 'LoginPassword')
senha.send_keys('SUA SENHA AQUI!')

entrar = driver.find_element(By.ID, 'acceptLogin')
entrar.click()

driver.switch_to.frame('basefrm')

reiniciar = driver.find_element(By.ID, 'btn-clicktocall')
reiniciar.click()

driver.switch_to.frame(0)

delay = WebDriverWait(driver, 10)

confirmar = delay.until(EC.element_to_be_clickable((By.ID, 'MLG_Pop_Reboot_Yes')))
confirmar.click()

driver.quit()