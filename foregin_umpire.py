""" analysis of foreign umpires"""
import matplotlib.pyplot as plt
from main import matches,umpires

def foreign_umpire_analysis():
    """ analysis of foreign umpires"""
    umpires_list = [] #list of umpires
    for row in matches:
        if row['umpire1'] not in umpires_list:
            umpires_list.append(row['umpire1'])
        if row['umpire2'] not in umpires_list:
            umpires_list.append(row['umpire2'])
    new_data = {}
    for row in umpires:
        new_data[row['umpire']] = row[' country']
    final_data = {}
    for row in umpires_list:
        if row in new_data and new_data[row] != ' India':

            try:
                final_data[new_data[row]] += 1
            except KeyError:
                final_data[new_data[row]] = 1
    country = list(final_data.keys())
    values = list(final_data.values())
    plt.bar(country,values)
    plt.title("Foregin umpire analysis")
    plt.xlabel("Country")
    plt.ylabel("Number of umpires")
    plt.show()

foreign_umpire_analysis()
