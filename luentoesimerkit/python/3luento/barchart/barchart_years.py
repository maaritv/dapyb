import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def create_bar_chart(categories, values, colors, title, xlabel, ylabel, filename):
    # Luo pylväsdiagrammi
    plt.figure(figsize=(10, 6))
    fig, ax = plt.subplots()
    plt.bar(categories, values, color=colors)

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.xticks(fontsize=14)  # X-akselin fonttikoko
    plt.yticks(fontsize=14)  # Y-akselin fonttikoko
    plt.savefig(filename) 

data = pd.read_csv('rakennuksetyears.csv', delimiter=",")
#categories = ['Omakotitalot', 'Rivitalot', 'Luhtitalot', 'Kerrostalot']
#values = [53, 24, 10, 6]  # Rakennusten lukumäärä samassa järjestyksessä
categories = data['Category']
values = data['Value']
colors = ['blue', 'orange', 'green', 'purple']
title='Firma Oy:n rakennusmäärien kasvu'
xlabel='Talotyyppi'
ylabel='Rakennettujen talojen määrä (kpl)'
filename="houses_per_years.pdf"
create_bar_chart(categories, values, colors, title, xlabel, ylabel, filename)
