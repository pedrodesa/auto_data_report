import requests

import pandas as pd


def get_api_ibge(link): 
    ''' Requisição dos dados do IBGE 
    referentes ao envelhecimento da população'''
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    
    return informacoes

url = "https://servicodados.ibge.gov.br/api/v3/agregados/9756/periodos/2022/variaveis/8845?localidades=N1[all]|N2[all]&classificacao=86[95251]"

data_ibge = get_api_ibge(url)
