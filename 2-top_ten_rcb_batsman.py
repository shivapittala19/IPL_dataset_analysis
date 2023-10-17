import matplotlib.pyplot as plt
from main import deliveries

def top_ten_rcb_bastman():
    batsman_runs = {}
    for row in deliveries:
        if row['batting_team'] == 'Royal Challengers Bangalore':
            batter, runs = row['batsman'] , int(row['batsman_runs'])
            try:
                batsman_runs[batter] += runs
            except:
                batsman_runs[batter] = int(runs)
                
    sorting_order = dict(sorted(batsman_runs.items(),key=lambda x: x[1],reverse=True))
    
    batsman = list(sorting_order.keys())[:10]
    batsman_runs = list(sorting_order.values())[:10]
    
    plt.bar(batsman,batsman_runs)
    plt.xlabel("Batsman")
    plt.ylabel("Runs")
    plt.title("Top 10 RCB batsman")
    plt.show()

top_ten_rcb_bastman()