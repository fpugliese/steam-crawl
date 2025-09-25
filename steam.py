import pandas as pd
import request_api

def parse_steam_request(appid, name):
    """Unique parser to handle data from Steam Store API.
    
    Returns : json formatted data (dict-like)
    """
    url = "http://store.steampowered.com/api/appdetails/"
    parameters = {"appids": appid}
    
    json_data = request_api.request(url, parameters=parameters)
    json_app_data = json_data[str(appid)]
    
    if json_app_data['success']:
        data = json_app_data['data']
    else:
        data = {'name': name, 'steam_appid': appid}
        
    return data

def main():
    # Set file parameters
    download_path = './data/steam_store/'
    steam_app_data = 'steam_app_data.csv'
    steam_index = './data/steam_index.txt'

    try:
        app_list = pd.read_csv('./data/steam_spy/all_data_id_name.csv')
    except FileNotFoundError:
        print("Arquivo 'all_data_id_name.csv' não encontrado. Execute o script 'steam_spy_name_id.py' primeiro.")
        return 
    except pd.errors.EmptyDataError:
        print("Arquivo 'all_data_id_name.csv' está vazio. Verifique o conteúdo do arquivo.")
        return

    steam_columns = [
        'type', 'name', 'steam_appid', 'required_age', 'is_free', 'controller_support',
        'dlc', 'detailed_description', 'about_the_game', 'short_description', 'fullgame',
        'supported_languages', 'header_image', 'website', 'pc_requirements', 'mac_requirements',
        'linux_requirements', 'legal_notice', 'drm_notice', 'ext_user_account_notice',
        'developers', 'publishers', 'demos', 'price_overview', 'packages', 'package_groups',
        'platforms', 'metacritic', 'reviews', 'categories', 'genres', 'screenshots',
        'movies', 'recommendations', 'achievements', 'release_date', 'support_info',
        'background', 'content_descriptors'
    ]

    # Overwrites last index for demonstration (would usually store highest index so can continue across sessions)
    request_api.reset_index(download_path, steam_index)

    # Retrieve last index downloaded from file
    index = request_api.get_index(download_path, steam_index)

    # Wipe or create data file and write headers if index is 0
    request_api.prepare_data_file(download_path, steam_app_data, index, steam_columns)

    # Set end and chunksize for demonstration - remove to run through entire app list
    request_api.process_batches(
        parser=parse_steam_request,
        app_list=app_list,
        download_path=download_path,
        data_filename=steam_app_data,
        index_filename=steam_index,
        columns=steam_columns,
        begin=index,
        end=10,
        batchsize=5
    )    

if __name__ == "__main__":
    main()