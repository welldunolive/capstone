from flask import Flask, Response, request, render_template
import numpy as np
import pandas as pd
import requests
import re

#import data
steam = pd.read_csv('Data/final_df2.csv')
recommender = pd.read_csv('Data/genre_rating_based2.csv')
recommender.set_index('name', inplace = True)

app = Flask('SteamGameRecommender')

#Home
@app.route('/')
def home():
    return render_template('form.html')

@app.route("/Submit", methods = ['GET', 'POST'])
def submit():
    
    user_input = request.form['game_name']
    
    names = steam[steam['name'].str.contains(user_input, flags = re.IGNORECASE)].reset_index()
    games = [names['name'][i] for i in range(names.shape[0])]

    return render_template('form2.html', games = games)

@app.route("/recommendations")
def recommend():

    selected = request.args['game_name']

    steam['rating'] = steam['all_reviews'].replace({0: 'N/A', 1: 'Overwhelmingly Negative', 2: 'Very Negative',
                                                    3: 'Mostly Negative', 4: 'Negative', 5: 'Mixed',
                                                    6: 'Positive', 7: 'Mostly Positive', 8: 'Very Positive', 9: 'Overwhelmingly Positive'}).copy()
    steam_t = steam.set_index('name').T
    
    recommendations = recommender[selected].sort_values()[1:13]
    a = list(recommendations.index)
    df = steam_t[a]

    return render_template('recommendations.html', games = df, names_list = a, selected = selected)


if __name__ == '__main__':
    app.run(debug = True)
    