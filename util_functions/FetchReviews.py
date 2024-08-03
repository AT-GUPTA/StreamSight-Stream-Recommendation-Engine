import requests
import time
import csv
from urllib.parse import quote

def fetch_reviews(appid, api_key, num_reviews=5000):
    reviews = []
    cursor = '*'
    while True:
        encoded_cursor = quote(cursor)  # URL encode the cursor
        url = f"https://store.steampowered.com/appreviews/{appid}?json=1&filter=updated&language=english&cursor={encoded_cursor}&num_per_page=100&key={api_key}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch data for AppID {appid}: HTTP Status Code {response.status_code}")
            break

        data = response.json()
        if 'reviews' not in data or not data['reviews']:
            print(f"No more reviews available for AppID {appid}.")
            break

        reviews_batch = data['reviews']
        reviews.extend(reviews_batch)
        cursor = data['cursor']

        if len(reviews) >= num_reviews or not reviews_batch:
            break

        time.sleep(1)  # To avoid hitting the rate limit

    return reviews[:num_reviews]

def save_reviews_to_csv(appid, reviews, filename):
    full_filename = f"{appid}_{filename}"
    with open(full_filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for review in reviews:
            author = review['author']
            writer.writerow([
                appid,
                review.get('recommendationid', ''),
                author.get('steamid', ''),
                author.get('num_games_owned', ''),
                author.get('num_reviews', ''),
                author.get('playtime_forever', ''),
                author.get('playtime_last_two_weeks', ''),
                author.get('playtime_at_review', ''),
                author.get('last_played', ''),
                review.get('review', ''),
                review.get('timestamp_created', ''),
                review.get('timestamp_updated', ''),
                review.get('voted_up', ''),
                review.get('votes_up', ''),
                review.get('votes_funny', ''),
                review.get('weighted_vote_score', ''),
                review.get('comment_count', ''),
                review.get('steam_purchase', ''),
                review.get('received_for_free', ''),
                review.get('written_during_early_access', '')
            ])

api_key = 'KEY'  # Steam API key
appids = ['730', '570']  # List of AppIDs to fetch reviews for

filename = 'steam_reviews.csv'

for appid in appids:
    reviews = fetch_reviews(appid, api_key, 5000)
    if reviews:
        save_reviews_to_csv(appid, reviews, filename)
        print(f"Saved reviews for game AppID {appid} to {appid}_{filename}")
    else:
        print(f"No reviews fetched for game AppID {appid}")
