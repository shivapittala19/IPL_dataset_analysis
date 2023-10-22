""" Total"""
import matplotlib.pyplot as plt
from main import matches

def number_of_matches_per_year():
    """number of matches played per year"""
    season_matces = {}
    for match in matches:
        season = match['season']
        if season in season_matces:
            season_matces[season] += 1
        else:
            season_matces[season] = 1
    sorted_season = dict(sorted(season_matces.items(),key=lambda x:x[0]))
    seasons = list(sorted_season.keys())
    matches_played = list(sorted_season.values())
    plt.bar(seasons,matches_played)
    plt.xlabel("season")
    plt.ylabel("Number of matches")
    plt.title("Number of matches played in each season")
    for index,value in enumerate(matches_played):
        plt.text(seasons[index],value,str(value),ha='center',va='bottom')
    plt.show()

number_of_matches_per_year()
