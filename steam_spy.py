# Description: Esse código lê os IDs dos jogos da Steam a partir de requests
# da API do site Steam Spy e salva esses IDs em um arquivo CSV.
# Autor: Fernando Melo Pugliese
# Documentação: https://steamspy.com/api.php

import pandas
import request_api

def main():

    url = "https://steamspy.com/api.php"
    params = {"request": "all"}

    data = request_api(url, params=params)
    steam_spy_all = pandas.DataFrame.from_dict(data, orient='index')
    steam_spy_all.to_csv("data/steam_spy_all.csv", index_label="appid")
    print(f"Foram salvos {len(steam_spy_all)} appids no arquivo data/steam_spy_all.csv")

if __name__ == "__main__":
    main()