""" analysis of foreign umpires"""
import matplotlib.pyplot as plt
from main import matches,umpires

def foreign_umpire_analysis():
    """foreign umpire analysis"""
    foreign_umpire = set()
    for match in matches:
        foreign_umpire.add(match['umpire1'])
        foreign_umpire.add(match['umpire2'])
    umpire_country = {}
    for umpire in umpires:
        umpire_country[umpire['umpire']] = umpire[' country']
    country_data = {}
    for umpire in foreign_umpire:
        if umpire in umpire_country:
            country = umpire_country[umpire]
            if country != ' India':
                if country in country_data:
                    country_data[country] +=1
                else:
                    country_data[country] = 1
    countries = list(country_data.keys())
    umpires_count = list(country_data.values())
    plt.bar(countries,umpires_count)
    plt.title("Foregin umpire analysis")
    plt.xlabel("Country")
    plt.ylabel("Number of umpires")
    for index,value in enumerate(umpires_count):
        plt.text(countries[index],value,str(value))
    plt.show()

foreign_umpire_analysis()
