import requests
import pandas as pd
from bs4 import BeautifulSoup

def clean_html(raw_html):
    if raw_html is None:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

def truncate_string(s, length=50):
    if s is None:
        return ""
    return (s[:length] + '...') if len(s) > length else s

def get_steam_data(appids):
    url = "http://store.steampowered.com/api/appdetails/"
    app_data = []

    for appid in appids:
        params = {"appids": appid}
        response = requests.get(url, params=params)
        data = response.json()

        if data and str(appid) in data and data[str(appid)].get('success'):
            app_info = data[str(appid)]['data']
            record = {
                'appid': appid,
                'title': app_info.get('name', ''),
                'developer': ', '.join(app_info.get('developers', [''])),
                'publisher': ', '.join(app_info.get('publishers', [''])),
                'genres': ', '.join([genre['description'] for genre in app_info.get('genres', [])]) if app_info.get('genres') else '',
                'languages': app_info.get('supported_languages', '').replace('<strong>*</strong>', '').replace('<br>', ''),
                'tags': ', '.join([category['description'] for category in app_info.get('categories', [])]) if app_info.get('categories') else '',
                'release_date': app_info.get('release_date', {}).get('date', ''),
                'price': app_info.get('price_overview', {}).get('final_formatted', '') if app_info.get('price_overview') else '',
                'old_userscore': app_info.get('metacritic', {}).get('score', '') if app_info.get('metacritic') else '',
                'owners': app_info.get('owners', ''),
                'is_free': app_info.get('is_free', ''),
                'detailed_description': truncate_string(clean_html(app_info.get('detailed_description', ''))),
                'about_the_game': truncate_string(clean_html(app_info.get('about_the_game', ''))),
                'short_description': truncate_string(clean_html(app_info.get('short_description', ''))),
                'pc_requirements': truncate_string(clean_html(app_info.get('pc_requirements', {}).get('minimum', ''))) if app_info.get('pc_requirements') else '',
                'content_descriptors': truncate_string(clean_html(app_info.get('content_descriptors', {}).get('notes', ''))) if app_info.get('content_descriptors') else ''
            }
            app_data.append(record)
        else:
            print(f"Data for AppID {appid} not found or request failed.")
    return pd.DataFrame(app_data)

# app ids to be fetched
app_ids =['730', '570']
steam_data = get_steam_data(app_ids)

# display options for better DataFrame visualization
pd.set_option('display.max_colwidth', 50)
print(steam_data)

# save to a CSV file
steam_data.to_csv('steam_data.csv', index=False)
