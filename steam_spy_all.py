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

    all_data = []

    while True:
        choice = input("Deseja fazer o download de todas as informacoes disponiveis?"
        "Caso digite no, salvaremos apenas o appid e o nome do jogo. (yes/no): ")
        if choice.lower() in ["yes", "y"]:
            print("Baixando todas as informacoes...")
            choice = True
            break
        elif choice.lower() in ["no", "n"]:
            print("Baixando apenas nome e ID...")
            choice = False
            break
        else:
            print("Escolha invalida. Escolha yes/no.")


    while page < 100:
        data = request_api.request(url, params=params)

        # Concatena os dados obtidos com os dados anteriores
        all_data = pandas.concat([pandas.DataFrame.from_dict(data, orient='index'), pandas.DataFrame(all_data)], ignore_index=True)
        print(f"Foram encontrados {len(data)} appids na página {page}.")

        page += 1
        params = {"request": "all", "page": page}

        # Se a quantidade de appids for menor que 1000, interrompe o loop
        if len(data) < 1000:
            print("Menos de 1000 appids encontrados, finalizando a coleta.")
            break

        # Segue o loop
        time.sleep(1)  # Aguarda 1 segundo entre as requisições para não sobrecarregar o servidor
        print(f"Indo para a página {page}...")

    steam_spy_all = pandas.DataFrame(all_data)

    if choice:
        games = steam_spy_all.sort_values(by = 'appid').reset_index(drop=True)
        games.to_csv("data/steam_spy/all_data.csv")
        print("Todos os dados foram salvos em data/steam_spy/all_data.csv")
    else:
        games = steam_spy_all[["appid", "name"]].sort_values(by = 'appid').reset_index(drop=True)
        games.to_csv("data/steam_spy/all_data_id_name.csv")
        print("Todos os dados foram salvos em data/steam_spy/all_data_id_name.csv")


if __name__ == "__main__":
    main()