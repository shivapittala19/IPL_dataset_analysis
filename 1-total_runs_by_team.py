import matplotlib.pyplot as plt
from main import deliveries,color_codes

def total_runs_scored_by_team():
    runs_dict = {}
    for row in deliveries:
        batting_team = row['batting_team']
        runs = int(row['total_runs'])
        try:
            runs_dict[batting_team] += runs
        except:
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