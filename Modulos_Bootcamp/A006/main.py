import selenium
from selenium import webdriver


driver = webdriver.Chrome('A006/src/chromedriver')


# driver.get('https://howedu.com.br/')
# driver.find_element(by='xpath', value='//*[@id="bootcamps"]/div/div/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div/div[1]/div/div').click()
# driver.find_element(by='xpath', value='//*[@id="post-16997"]/div/div/section[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/section/div/div/div/section[1]/div/div').click()



# ----------- Busca CEP Correios -----------
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
elem_cep = driver.find_element(by='name', value='endereco')
elem_cep.clear()
cep_to_find = input('Digite o seu CEP: ')
elem_cep.send_keys(cep_to_find)

elem_combo_box = driver.find_element(by='name', value='tipoCEP')
elem_combo_box.click()
combo_box_options = driver.find_element(by='xpath', value='//*[@id="tipoCEP"]/optgroup/option[6]')
combo_box_options.click()

botao_buscar = driver.find_element(by='name', value='btn_pesquisar')
botao_buscar.click()

logradouro = driver.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
bairro = driver.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
localidade = driver.find_element('xpath', '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
