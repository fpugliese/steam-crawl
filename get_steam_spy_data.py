# Description: This code fetches game IDs from the Steam Spy API using the "request all"
# parameter, iterating through pages until no more data is available, 
# and saves them into a CSV file.
# Documentation: https://steamspy.com/api.php

import pandas
import time

import request_api

def main():

    # Defines Steam Spy's URL and the parameters for the requests
    url = "https://steamspy.com/api.php"
    page = 0
    params = {"request": "all", "page": page}

    all_data = []

    while True:
        choice = input("Do you want all the info available on Steam Spy? \n" \
        "If you intend to use crawl.py, you should choose 'No', so only the Game Name and AppID will be saved. (yes/no): ")
        if choice.lower() in ["yes", "y"]:
            print("Downloading all information...")
            choice = True
            break
        elif choice.lower() in ["no", "n"]:
            print("Saving only name and AppID...")
            choice = False
            break
        else:
            print("Invalid choice. Please choose between yes/no.")

    request_api.check_folder()

    while page < 100:
        data = request_api.request(url, params=params)

        all_data = pandas.concat([pandas.DataFrame.from_dict(data, orient='index'), pandas.DataFrame(all_data)], ignore_index=True)
        print(f"Found {len(data)} appids in page {page}.")

        page += 1
        params = {"request": "all", "page": page}

        # SteamSpy offers 1000 apps per all request, should it provide less than 1000, it means that we reached the end
        if len(data) < 1000:
            print("Less than 1000 appids found, wrapping up.")
            break

        time.sleep(1)  # 1 second delay so we don't overload the server
        print(f"Going to page {page}...")

    steam_spy_all = pandas.DataFrame(all_data)

    if choice:
        games = steam_spy_all.sort_values(by = 'appid').reset_index(drop=True)
        games.to_csv("data/steam_spy/all_data.csv")
        print("All data saved to data/steam_spy/all_data.csv")
    else:
        games = steam_spy_all[["appid", "name"]].sort_values(by = 'appid').reset_index(drop=True)
        games.to_csv("data/steam_spy/id_name.csv")
        print("All data saved to data/steam_spy/id_name.csv")


if __name__ == "__main__":
    main()