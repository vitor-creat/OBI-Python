'''
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']

    print("Cotação do Dólar: R$", cotacao_dolar)
    print("Cotação do Euro: R$", cotacao_euro)

pegar_cotacoes()

'''


'''
# Repita os passos manuais, usando codigo
# 1 - Entrar no site - https://devaprender-play.netlify.app/
# 2 - Anotar o nome do primeiro produto
# 3 - Anotar o preço do primeiro produto
# 4 - Repetir para todos os produtos
# 5 - Guardar em um arquivo .csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1 - Entrar no site
driver = webdriver.Chrome()
driver.get('https://devaprender-play.netlify.app/')
sleep(5)

# 2 - Anotar o nome do primeiro produto
produtos = driver.find_elements(By.XPATH,"//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")

# 3 - Anotar o preço do primeiro produto
precos = driver.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

# 4 - Mostrar no console
# 5 - Guardar em um arquivo .csv 
for produto, preco in zip(produtos,precos):
    with open('produtos.csv', 'a', encoding='utf-8') as arquivo: 
        arquivo.write(f'{produto.text},{preco.text}\n')

driver.quit()


# XPATH(identificador do elemento)
# //tag[@atributo='valor']
'''