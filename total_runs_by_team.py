"""
This Module is to find the total runs scored by team
"""
import matplotlib.pyplot as plt
from main import deliveries,color_codes

def total_runs_scored_by_team():
    """ runs scored by each team icombined all seasons """
    runs_dict = {}
    #creating a dictinary with key as a team and runs scored as it's value
    for row in deliveries:
        batting_team = row['batting_team']
        runs = int(row['total_runs'])
        if batting_team in runs_dict:
            runs_dict[batting_team] += runs
        else:
            runs_dict[batting_team] = runs
    x_values = list(runs_dict.keys())
    y_values = list(runs_dict.values())
    plt.bar(x_values,y_values,color = color_codes,label = x_values,width=0.5)
    plt.xlabel("Team")
    plt.ylabel("Runs scored by team")
    plt.title("Runs scored by each team")
    plt.legend()
    plt.xticks(rotation = 90)
    plt.show()

total_runs_scored_by_team()
