from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome('A006/src/chromedriver')
time.sleep(3)
driver.implicitly_wait(40)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
tabela = driver.find_element('xpath', '//*[@id="mw-content-text"]/div[1]/table[2]')
driver.close()
df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]

def tem_item(xpath, driver=driver):
    try:
        driver.find_element('xpath', xpath)
        return True
    except:
        return False
