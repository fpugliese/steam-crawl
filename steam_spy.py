# Description: Esse código lê os IDs dos jogos da Steam a partir de requests
# da API do site Steam Spy e salva esses IDs em um arquivo CSV.
# Autor: Fernando Melo Pugliese
# Documentação: https://steamspy.com/api.php

import pandas
import time

import request_api

def main():

    # Define a URL da API do Steam Spy e os parâmetros para a requisição
    url = "https://steamspy.com/api.php"
    page = 0
    params = {"request": "all", "page": page}

    while page < 100:
        data = request_api.request(url, params=params)
        steam_spy_all = pandas.DataFrame.from_dict(data, orient='index')
        steam_spy_all.to_csv(f"data/steam_spy_all_page{page}.csv", index_label="appid")
        print(f"Foram salvos {len(steam_spy_all)} appids no arquivo data/steam_spy_all_page{page}.csv")
        page += 1
        params = {"request": "all", "page": page}

        # Se a quantidade de appids for menor que 1000, interrompe o loop
        if len(steam_spy_all) < 1000:
            print("Menos de 1000 appids encontrados, finalizando a coleta.")
            break

        # Segue o loop
        time.sleep(1)  # Aguarda 1 segundo entre as requisições para não sobrecarregar o servidor
        print(f"Indo para a página {page}...")
        
if __name__ == "__main__":
    main()