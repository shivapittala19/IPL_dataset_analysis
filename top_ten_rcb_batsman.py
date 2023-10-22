""" Find top rcb batsmans"""
import matplotlib.pyplot as plt
from main import deliveries

def top_ten_rcb_bastman():
    """ top 10 rcb batsmans """
    batsman_runs = {}
    for bowl in deliveries:
        batsman = bowl['batsman']
        runs = int(bowl['batsman_runs'])
        if bowl['batting_team'] == "Royal Challengers Bangalore":
            if  batsman in batsman_runs:
                batsman_runs[batsman] += runs
            else:
                batsman_runs[batsman] = runs
    sorted_batsman_runs = dict(
        list(sorted(batsman_runs.items(),key=lambda x:x[1],reverse=True))[:10]
    )
    batter = list(sorted_batsman_runs.keys())
    runs_by_batter = list(sorted_batsman_runs.values())
    plt.bar(batter,runs_by_batter)
    for index,value in enumerate(runs_by_batter):
        plt.text(batter[index],value ,str(value),ha='center', va='bottom')
    plt.show()

top_ten_rcb_bastman()
