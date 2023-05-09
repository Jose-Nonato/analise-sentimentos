from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://twitter.com/i/flow/login")

### Quando estiver dando tudo certo ###
# username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
# username.send_keys("") # Email da Conta

# button_username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')))
# button_username.click()

# password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
# password.send_keys("") # Senha da Conta

# button_password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')))
# button_password.click()
### Quando estiver dando tudo certo ###

### Quando der problema e pedir segunda autenticação ###
username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
username.send_keys("") # Email da Conta

button_username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')))
button_username.click()

password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
password.send_keys("") # Senha da Conta

# button_password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div')))
# button_password.click()

# Obs.: Problema na hora de clicar no botão! Botões a partir do 1° são div's !!!
### Quando der problema e pedir segunda autenticação ###

time.sleep(5)

hashtag_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')))
hashtag_button.click()

trending_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a')))
trending_button.click()

top_one_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[3]/div/div/div')))
top_one_button.click()

# =-=-=-=-=-=--=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-=-=-=-=-=

time.sleep(4)

arrayTrends = []
while True:
    if len(arrayTrends) < 30:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)        
        trends_elements = browser.find_elements(By.CSS_SELECTOR, '.css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
        for i in trends_elements:
            print(i.text)
            arrayTrends.append(i.text)
    else:
        break

print(len(arrayTrends))