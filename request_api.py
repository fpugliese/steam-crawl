# Description: Esse código lê os IDs dos jogos da Steam a partir de requests
# da API do site Steam Spy e salva esses IDs em um arquivo CSV.
# Autor: Fernando Melo Pugliese
# Documentação: https://steamspy.com/api.php
import requests
import time

def request(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
    except requests.exceptions.RequestException as e:
        # Caso ocorra algum erro na requisição, ele será capturado aqui
        print(f"Erro ao fazer a requisição: {e}")
        # Aguardamos 10 segundos antes de tentar novamente
        time.sleep(10)
        return request(url, params)
    
    if response.status_code == 200:
        # Se a resposta for bem-sucedida, retornamos o conteúdo JSON
        return response.json()
    elif response == None:
        # Se a resposta for None, provavelmente excedemos a quantidade de tentativas,
        # aguardamos 10 segundos e tentamos novamente
        print("Sem resposta, tentando novamente em 10 segundos...")
        time.sleep(10)
        return request(url, params)
    else:
        # Caso contrário, imprimimos o código de status da resposta
        print(f"Erro na resposta da API: {response.status_code} - Parametros: {params}")
        return None