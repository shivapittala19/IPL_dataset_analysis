import matplotlib.pyplot as plt
from main import matches, color_codes

def number_of_wins_by_team_in_each_season():
    wins_by_team_and_season = {}
    
    # creating a dict as follows
    # {
    #     'season':{
    #         'team1':'number_of_wins' ,'team2': 'number_of_wins',
    #     },
    # }
    for row in matches:
        season = row['season']
        winner = row['winner']
        if season in wins_by_team_and_season:
            if winner in wins_by_team_and_season[season]:
                wins_by_team_and_season[season][winner] += 1
            else:
                wins_by_team_and_season[season][winner] = 1
        else:
            wins_by_team_and_season[season] = {winner : 1}
            
    sorted_wins_by_season = dict(sorted(wins_by_team_and_season.items(),key=lambda x : x[0]))
    
    #list of all teams
    list_teams = []
    for season_data in sorted_wins_by_season.values():
        for team in season_data.keys():
            if team not in list_teams:
                list_teams.append(team)
        
    
    #Data of wins by each team in each season
    #making a dict of list as key as team and values as a list ,value at each index represents the number of matches won in specific season
    # format
    # {
    #     'team1' : [0,13,15,16,14,0,0,13,13,],
    #     'team2' : [0,13,15,16,14,0,0,13,13]
    # }
    team_wins = {team: [year_data.get(team, 0) for year_data in sorted_wins_by_season.values()] for team in list_teams}
    values = list(team_wins.values())
    positions = [season for season in range(2008,2018)]

    plt.figure(figsize=(10, 5))
    bottom = [0]*len(positions)
    for i in range(len(list_teams)):
        plt.bar(positions,values[i],color = color_codes[i],label=list_teams[i],bottom=bottom)
        # bottom values represents in each index of plot we are passing the height of the stack
        bottom = [bottom[j] + values[i][j] for j in range(len(positions))]
  
    
    plt.legend()
    plt.show()
    
number_of_wins_by_team_in_each_season()