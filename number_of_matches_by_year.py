""" Total"""
import matplotlib.pyplot as plt
from main import matches

def number_of_matches_per_year():
    """ Total number of matches played in each season"""
    match_dict = {}
    # creating a dict with keys-> season and value -> number of matches played in that season
    for row in matches:
        try:
            match_dict[row['season']] += 1
        except KeyError:
            match_dict[row['season']] = 1
    sorted_match_dict = dict(sorted(match_dict.items(),key=lambda x: x[0]))
    season = list(sorted_match_dict.keys())
    matches_per_season = list(sorted_match_dict.values())
    plt.bar(season,matches_per_season)
    plt.xlabel("season")
    plt.ylabel("Number of matches")
    plt.title("Number of matches played in each season")
    plt.show()

number_of_matches_per_year()
