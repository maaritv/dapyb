import pandas as pd
import matplotlib.pyplot as plt

def create_bar_chart(categories, values, colors, title, xlabel, ylabel, filename):
    # Luo pylväsdiagrammi
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=colors)

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.xticks(fontsize=14)  # X-akselin fonttikoko
    plt.yticks(fontsize=14)  # Y-akselin fonttikoko
    plt.savefig(filename) 

data = pd.read_csv('rakennukset.csv', delimiter=",")
#categories = ['Omakotitalot', 'Rivitalot', 'Luhtitalot', 'Kerrostalot']
#values = [53, 24, 10, 6]  # Rakennusten lukumäärä samassa järjestyksessä
categories = data['Category']
values = data['Value']
colors = ['blue', 'orange', 'green', 'purple']
title='Firma Oy:n rakentamat talot talotyypeittäin vuonna 2024'
xlabel='Talotyyppi'
ylabel='Rakennettujen talojen määrä (kpl)'
filename="houses.pdf"
create_bar_chart(categories, values, colors, title, xlabel, ylabel, filename)
