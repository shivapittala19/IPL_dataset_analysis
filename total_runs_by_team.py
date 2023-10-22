"""This Module is to find the total runs scored by team"""
import matplotlib.pyplot as plt
from main import deliveries

def total_runs_scored_by_team():
    """ runs scored by each team icombined all seasons """
    runs_scored = {}
    #creating a dictinary with key as a team and runs scored as it's value
    for bowl in deliveries:
        batting_team = bowl['batting_team']
        runs = int(bowl['total_runs'])
        if batting_team in runs_scored:
            runs_scored[batting_team] += runs
        else:
            runs_scored[batting_team] = runs
    team = list(runs_scored.keys())
    runs = list(runs_scored.values())
    plt.bar(team,runs,width=0.5)
    plt.xlabel("Team")
    plt.ylabel("Runs scored by team")
    plt.title("Runs scored by each team")
    plt.xticks(rotation = 90)
    for index,value in enumerate(runs):
        plt.text(team[index],value,str(value),ha='center',va='bottom')
    plt.show()

total_runs_scored_by_team()
