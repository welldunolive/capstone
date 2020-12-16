<img src = "img/steam.png" width="300"/>


# Table of Contents
- [Problem Statement](#Problem-Statement)
- [Data Collection](#Data-Collection)
- [Recommender System](#Recommender-System)
- [Demo](#Demo)
- [Conclusion and For Future](#Conclusion-and-For-Future)

# Problem Statement
There are thousands and thousands of games available. As a casual gamer, I take hours looking for right games worth my time and money.
Steam is a popular gaming platform that provides thousands upon thousands of games to its users. 

Gaming has become not just a hobby but also a source of income. The business has grown tremendously since the support for e-Sports has grown. Even the view on gaming has changed ever since. With more people staying home due to COVID-19, game industry has never been larger.

So how do we exactly find games we like? We can go through the path of personal recommendation but not everyone has the luxury of finding someone who enjoys the same exact games as you. To save time and money on games we do not like, many look outside of Steam to get recommendations on games based on what they have played. For this project, I have created a recommender system based on popular tags and the publisher of a game of user's decision.

## Data Collection
Two different datasets were collected for this project. one was from Kaggle created by Craig Kelly (https://github.com/CraigKelly/steam-data) and other was collected from Steamspy.com. SteamSpy is a consumer based website for Steam games that allows users to look for games in a more efficient way than what Steam UI provides for us. Data contains about 20,000 different games and softwares.

## Recommender System
There are a few different ways to build a recommender system; text based, collaborative filtering, and content based. My recommender system is content based, as mentioned above (tags and publisher). I personally noticed that once I enjoy a specific game, I tend to enjoy similar games from the same publisher. Using CountVectorizer on tags/genres to count the word frequency and TfidfVectorizer on the publishers to assign a score for each one.

To find the similarities on the vectorized features, I created a new dataset with cosine distance between each games. Cosine similarities show the distance between the two vectors using the angle in between them. The smaller the angle is, greater the similarities.

<img src = "img/cod.png">

Final dataset is available [here](https://drive.google.com/file/d/1-2fg5bSDyq6v7jbzu1adtjiQ5oYSjJ_N/view?usp=sharing)

## Demo
I used Flask to create a local app that will search for a specific game a user has input and spit out 12 different games that are most similar to each other.

<img src = "img/recommender.JPG">

## Conclusion and For Future
The recommender I created definitely works with great results. However, it only contains a page of information soley based on the two features and only the games available on Steam. My next step is to create a bigger dataset that contain games from different consoles and different filters in my app for the consumers to have more options in their search. For example, description of the game alone can make different results. By having different options for the users, my app will maximize its potential as well as help the consumers make a better choice.
