""" stacked data of matches season number of matches"""
import matplotlib.pyplot as plt
from main import matches,color_codes

def number_of_matches_played_per_year_by_team():
    """ stacked data of matches season number of matches"""
    matches_played = {}
    for row in matches:
        season = row['season']
        team1 , team2 = row['team1'] , row['team2']
        if season in matches_played:
            if team1 in matches_played[season]:
                matches_played[season][team1] +=1
            else:
                matches_played[season][team1] = 1
            if team2 in matches_played[season]:
                matches_played[season][team2] +=1
            else:
                matches_played[season][team2] = 1
        else:
            matches_played[season] = {team1 : 1 , team2: 1}
    #sorting the dict based on season
    sorted_matches_played = dict(sorted(matches_played.items(),key=lambda x : x[0]))
    #list of all teams to be plotted
    list_teams = []
    for season_data in sorted_matches_played.values():
        for team in season_data.keys():
            if team not in list_teams:
                list_teams.append(team)
    team_wins = {
        team : [ year_data.get(team, 0) for year_data in sorted_matches_played.values()]
        for team in list_teams
    }
    values = list(team_wins.values())
    positions = [range(2008,2018)]
    plt.figure(figsize=(10, 5))
    bottom = [0]*len(positions)
    for key, in enumerate(list_teams):
        plt.bar(positions,values[key],color=color_codes,label=list_teams[key],bottom=bottom)
        bottom = [bottom[j] + values[key][j] for j in range(len(positions))]
    plt.legend()
    plt.show()

number_of_matches_played_per_year_by_team()
