import matplotlib.pyplot as plt
import pandas as pd

def createBoxAndWhiskerPlot(data, title, ylabel, file_name):
    # Plotataan laatikko-janakaavio
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, vert=True, patch_artist=True, 
                boxprops=dict(facecolor='lightblue', color='blue'),
                whiskerprops=dict(color='blue'),
                flierprops=dict(marker='o', color='red', markersize=8),
                medianprops=dict(color='darkblue'))

    # Asetetaan kaavion otsikot ja selitteet
    columns=list(data.columns) ##columns arvoksi lista ['june', 'july']
    column_indices = []  # Alustetaan tyhjä lista
    for i in range(0, len(data.columns)):
        column_indices.append(i + 1)  # Lisätään listaan numeroita 1,2, jne

    print(column_indices)  #column_indices sisaältö  lista [1,2]
    ##plt.xticks([1,2], ["june", "july"])  ## for-simukka luo [1,2] tietorakenteen
    ## indeksi 0 tarkoittaisi, että laatikko tulee Y-akselin päälle. siksi kohdat 1 ja 2
    plt.xticks(column_indices, columns)
    plt.ylabel(ylabel)
    plt.title(title)

    # Talletetaan kuvaaja
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(file_name) 


## Koodin suoritus alkaa tästä.

data = pd.read_csv('temperaturesb.csv', delimiter=";")
title="Kesä- ja heinäkuun päivien lämpötilat\n(poikkeamat korostettuina)"
ylabel="Lämpötila (°C)"
file_name="temperatures.png"
createBoxAndWhiskerPlot(data, title, ylabel, file_name)
