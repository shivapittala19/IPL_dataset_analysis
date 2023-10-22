""" To find the nuber of matches won by a team in each season"""
import matplotlib.pyplot as plt
from main import matches, color_codes

def number_of_wins_by_team_in_each_season():
    """matches won by year by team"""
    matches_won = {}
    for match in matches:
        season = match['season']
        team = match['winner']
        if season in matches_won:
            if team in matches_won[season]:
                matches_won[season][team] += 1
            else:
                matches_won[season][team] = 1
        else:
            matches_won[season] = {team:1}

    teams = []
    for season,season_matches in matches_won.items():
        for team in season_matches:
            if team not in teams:
                teams.append(team)
    sorted_matches_won = dict(
        sorted(matches_won.items(),key=lambda x: x[0])
    )
    team_wins = {}
    for team in teams:
        number_of_wins = []
        for year in sorted_matches_won.values():
            number_of_wins.append(year.get(team,0))
        team_wins[team] = number_of_wins

    seasons = [year for year in range(2008,2018)]
    matches_won = list(team_wins.values())
    bottom = [0]*len(seasons)
    plt.figure(figsize=(10, 5))
    for index,team in enumerate(list(teams)):
        plt.bar(seasons,matches_won[index],color=color_codes[index],label=team,bottom=bottom)
        bottom = [bottom[j]+ matches_won[index][j] for j in range(len(seasons))]
    plt.xlabel("season")
    plt.ylabel("Number of matches won")
    plt.title("Number of matches won by each team in each season")
    plt.legend()
    plt.show()

number_of_wins_by_team_in_each_season()
