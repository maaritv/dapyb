import pandas as pd
import matplotlib.pyplot as plt

def createPieChart(title, labels, sizes, colors, explode, file_name="piechart.png"):
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)
    plt.title(title)
    plt.savefig(file_name) 


data = pd.read_csv('fruits.csv', delimiter=",")
#categories = ['Omakotitalot', 'Rivitalot', 'Luhtitalot', 'Kerrostalot']
#values = [53, 24, 10, 6]  # Rakennusten lukumäärä samassa järjestyksessä
categories = data['category']
values = data['value']
colors = data['color']  # Värit

title='Hedelmäosaston myynnin jakauma'
#categories = ['Omenat', 'Päärynät', 'Appelsiinit', 'Muut hedelmät']
#values = [25, 20, 40, 15]  # Viipaleiden %osuudet samassa järjestyksessä
explode = (0.1, 0, 0, 0)  #Omenan viipale on visuaalisesti hieman erotettu
createPieChart(title, categories, values, colors, explode, "fruits.png")
