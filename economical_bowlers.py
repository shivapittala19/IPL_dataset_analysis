"""to find the economical bowlers"""
import matplotlib.pyplot as plt
from main import deliveries, matches

def top_economical_bowlers():
    """top economical bowler of the season 2015"""
    season_id = []
    for match in matches:
        if match['season'] == '2015' and match['id'] not in season_id:
            season_id.append(match['id'])

    bowler_economy ={}
    for bowl in deliveries:
        if bowl['match_id'] in season_id:
            bowler = bowl['bowler']
            runs = int(bowl['total_runs'])
            if bowl['wide_runs'] == '0' or bowl['noball_runs'] == '0':
                if bowler in bowler_economy:
                    bowler_economy[bowler][0] += runs
                    bowler_economy[bowler][1] += 1
                else:
                    bowler_economy[bowler] = [runs,1]
            else:
                if bowler in bowler_economy:
                    bowler_economy[bowler][0] += runs
                else:
                    bowler_economy[bowler] = [runs,0]

    for bowler in bowler_economy:
        bowler_economy[bowler] = round(bowler_economy[bowler][0] / bowler_economy[bowler][1]*6,2)
    top_ten_bowlers = dict(
        sorted(bowler_economy.items(),key=lambda x: x[1])[:10]
    )
    bowler = list(top_ten_bowlers.keys())
    economy = list(top_ten_bowlers.values())
    plt.bar(bowler,economy)
    plt.xlabel("Bowler")
    plt.ylabel("Economy")
    plt.title("Top 10 economical bowlers of 2015")
    for index,economy_value in enumerate(economy):
        plt.text(bowler[index],economy_value,str(economy_value),ha='center',va='bottom')
    plt.show()

top_economical_bowlers()
