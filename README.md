# Project Summary

## 1. Datasets

This project leverages two comprehensive datasets provided via the Steam APIs, encompassing both game metadata and user-generated content.

### - The *Steam App Info* dataset

URL: `http://store.steampowered.com/api/appdetails/` (2M)

This dataset includes fields such as `appid`, `title`, `developer`, `publisher`, `genres`, `languages`, `tags`, `release_date`, `price`, `old_userscore`, `is_free`, `detailed_description`, `about_the_game`, `short_description`, `pc_requirements`, and `content_descriptors`. These fields are instrumental in understanding the characteristics and diversity of games available on the platform.

### - The *Steam User Reviews* dataset

URL: `https://store.steampowered.com/appreviews/{appid}?json=1&filter=updated&language=english&cursor={encoded_cursor}&num_per_page=100&key={api_key}` (50k)

This dataset captures user interactions and opinions, detailed by attributes like `recommendationid`, `steamid`, `num_games_owned`, `num_reviews`, `playtime_forever`, `playtime_last_two_weeks`, `playtime_at_review`, `last_played`, `language`, `review`, `timestamp_created`, `timestamp_updated`, `voted_up`, `votes_up`, `votes_funny`, `weighted_vote_score`, `comment_count`, `steam_purchase`, `received_for_free`, `written_during_early_access`, and `developer_response`. These datasets encompass both quantitative and qualitative data, providing a rich foundation for analyzing user preferences and behaviors towards gaming content.

## 2. Research Question

The core objective of this study is to explore the feasibility of developing a recommender system that can suggest games to users based on their historical review sentiments and playtime metrics. This question probes the intersection of user-generated content analysis and predictive modeling to enhance personalization and user experience on digital platforms.

## 3. Model Design

The analytical framework of this project is structured around the application of machine learning models and algorithms tailored to interpret the complex dataset characteristics. The project employs a dual approach, integrating Sentiment Analysis, Collaborative Filtering, and Content-Based Filtering.

### 3.1 Sentiment Analysis and Collaborative Filtering

#### 3.1.1 Sentiment Analysis

For sentiment analysis, the project leverages the advanced capabilities of the [TweetNLP tool](https://github.com/cardiffnlp/tweetnlp#:~:text=%3DFalse%29-,Sentiment%20Analysis,-%3A%20The%20sentiment%20analysis), selected for its proficiency in processing informal language, including slang often found in game reviews. This model has been trained on a vast corpus of social media text data, allowing for effective sentiment classification across reviews. 
The sentiment analysis process is enhanced by utilizing NLP techniques such as tokenization, stemming, and stop word removal to preprocess review texts, improving the model's ability to focus on relevant sentiment indicators.

#### 3.1.2 Collaborative Filtering

The collaborative filtering component employs the Top-K Nearest Neighbors algorithm, a variant of the K-Nearest Neighbors (KNN) algorithm, optimized for large datasets and designed to identify similarities among users based on a vector space model. User vectors are constructed from features such as playtime metrics (total playtime, playtime in the last two weeks, playtime at the time of review), sentiment scores derived from reviews, and engagement metrics (votes up, votes funny, number of games owned, review count).

This algorithm calculates similarity scores using a cosine similarity measure, identifying the top-K users most similar to a given user. Recommendations are then generated based on the gaming preferences of these similar users, weighted by their similarity scores. This approach not only leverages shared experiences within the user community but also incorporates sentiment analysis results to provide a nuanced understanding of user preferences, significantly enhancing the personalized recommendation system.

### 3.2 Content-Based Filtering

For content-based filtering, the methodological approach focuses on the application of cosine similarity to compare user profiles with game characteristics. This is achieved by constructing feature vectors from concatenated attributes from both the Steam App Info and Steam User Reviews datasets.

From the Steam App Info dataset, the "tags" vector includes attributes such as `developer`, `publisher`, `genres`, `languages`, `tags`, `release_date`, `price`, `old_userscore`, `is_free`, and `detailed_description`, `about_the_game`, `short_description`, `pc_requirements`, and `content_descriptors`. From the Steam User Reviews dataset, the feature vector incorporates metrics like `total_playtime_forever`, `total_playtime_last_two_weeks`, and a textual analysis of the 50 most common words across all reviews for a game. 
These attributes provide a comprehensive view of each game, reflecting its thematic elements, gameplay mechanics, and overall content, which are essential for aligning games with user preferences.

The cosine similarity calculation is then applied to these feature vectors, identifying games with the highest similarity scores to a user's games profile, based on their past interactions and sentiment towards a game. This approach facilitates highly personalized game recommendations, ensuring users are introduced to titles that closely match their interests and gameplay preferences.
