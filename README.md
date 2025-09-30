# Steam Crawl

A Python-based project for crawling and extracting data from SteamSpy and the Steam platform.

**Heavily** inspired by Nik Davis' project, you can find his work on [github](https://github.com/nik-davis/steam-data-science-project) or well documented on his [blog](https://nik-davis.github.io/). He also has a dataset published on [Kaggle](https://www.kaggle.com/nikdavis/datasets).

You can find the dataset gathered with this code on [Kaggle](https://www.kaggle.com/datasets/fmpugliese/steam-all-games-data).

"get_steam_spy_data.py" will make requests using the "request:all" parameter to the SteamSpy API, you can find the API documentation [here](https://steamspy.com/api.php).

"crawl.py" relies on data previously captured by "get_steam_spy_data.py", it will make requests to the Steam API using the Steam appids collected from SteamSpy.

## Running the Project with `uv`

To run this project using [`uv`](https://github.com/astral-sh/uv), follow these steps:

1. **Clone Repo**:

    ```bash
    git clone https://github.com/fpugliese/steam-crawl
    ```

2. **Sync the environment with uv**

    ```bash
    uv sync
    ```

3. **Run the desired script with uv**

    ```bash
    uv run crawl.py
    ```
