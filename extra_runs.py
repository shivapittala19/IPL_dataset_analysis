""" To find the extra runs conceded by each team """
import matplotlib.pyplot as plt
from main import deliveries, matches

def extra_runs_conceded_by_team():
    """extra runs conceeded in 2016 by each team"""
    season_id = []
    for match in matches:
        if match['season'] == '2016' and match['id'] not in season_id:
            season_id.append(match['id'])

    runs = {}
    for bowl in deliveries:
        if bowl['match_id'] in season_id:
            bowling_team = bowl['bowling_team']
            extra_runs = int(bowl['extra_runs'])
            if bowling_team in runs:
                runs[bowling_team] += extra_runs
            else:
                runs[bowling_team] = extra_runs

    team = list(runs.keys())
    extra_run_offered = list(runs.values())
    plt.bar(team,extra_run_offered)
    plt.xlabel("Team")
    plt.ylabel("Extra runs conceded")
    plt.title("Extra runs conceded by team ")
    for index,value in enumerate(extra_run_offered):
        plt.text(team[index],value,str(value),ha='center',va='bottom')
    plt.show()

extra_runs_conceded_by_team()
