import matplotlib.pyplot as plt
from main import matches,color_codes

def number_of_matches_played_per_year_by_team():
    matches_played = {}
    for row in matches:
        season = row['season']
        team1 , team2 = row['team1'] , row['team2']
        # creating a dict as follows
        # {
        #     'season1': {
        #         'team1' : 'matches_played','team2':'matches_played'
        #     },
        # } 
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
                
    #making a dict of list as key as team and values as a list ,value at each index represents the number of matches played in specific season
    # format
    # {
    #     'team1' : [0,13,15,16,14,0,0,13,13,],
    #     'team2' : [0,13,15,16,14,0,0,13,13]
    # }
    team_wins = {team: [year_data.get(team, 0) for year_data in sorted_matches_played.values()] for team in list_teams}
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
    
number_of_matches_played_per_year_by_team()