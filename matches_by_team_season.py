""" stacked data of matches season number of matches"""
import matplotlib.pyplot as plt
from main import matches,color_codes

def number_of_matches_played_per_year_by_team():
    """ number of matches in each season by each team"""
    matches_played = {}
    for match in matches:
        season = match['season']
        team1,team2 = match['team1'],match['team2']
        if season in matches_played:
            if team1 in matches_played[season]:
                matches_played[season][team1] += 1
            else:
                matches_played[season][team1] = 1
            if team2 in matches_played[season]:
                matches_played[season][team2] += 1
            else:
                matches_played[season][team2] = 1
        else:
            matches_played[season] = {team1:1,team2:1}

    teams = set()
    for season,season_matches in matches_played.items():
        for team in season_matches:
            teams.add(team)
    sorted_matches_played = dict(
        sorted(matches_played.items(),key=lambda x: x[0])
    )
    team_matches = {}
    for team in teams:
        number_of_matches = []
        for year in sorted_matches_played.values():
            number_of_matches.append(year.get(team,0))
        team_matches[team] = number_of_matches

    seasons = [year for year in range(2008,2018)]
    matches_played = list(team_matches.values())
    bottom = [0]*len(seasons)
    plt.figure(figsize=(10, 5))
    for index,team in enumerate(list(teams)):
        plt.bar(seasons,matches_played[index],color=color_codes[index],label=team,bottom=bottom)
        bottom = [bottom[j]+ matches_played[index][j] for j in range(len(seasons))]
    plt.legend()
    plt.show()

number_of_matches_played_per_year_by_team()
