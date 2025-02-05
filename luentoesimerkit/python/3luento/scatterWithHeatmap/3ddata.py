import pandas as pd
import matplotlib.pyplot as plt

def createScatterPlotWithIntensity(x,y,z, title, xlabel, ylabel, zlabel, filename="scatter_heat.png"):
    # Värit tiheyden perusteella (esim. käytetään z-arvoja)
    plt.figure(figsize=(8, 6))
    colors = z
    s=20*z
    scatter=plt.scatter(x, y, c=colors, cmap='viridis', s=s, edgecolor='k', alpha=0.8)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    min_limit = min(x.min(), y.min())-5  # pienin arvo x- ja y-datasta
    max_limit = max(x.max(), y.max())+5  # suurin arvo x- ja y-datasta
    plt.xlim(min_limit, max_limit)  # Sama skaala x-akselille
    plt.ylim(min_limit, max_limit)  # Sama skaala y-akselille

    # Lisätään väripalkki
    cbar = plt.colorbar(scatter, shrink=0.6, aspect=10)
    cbar.ax.get_yaxis().labelpad = 20  ##palkin etäisyys selitetekstistä
    cbar.set_label(zlabel, rotation=270)
    plt.savefig(filename)
    return filename 


data = pd.read_csv('customers.csv', delimiter=";")

# Oletetaan, että sarakkeiden nimet ovat 'x', 'y', 'z'
x = data['x']
y = data['y']
z = data['z']

title="Asiakkaiden oleskelu kaupan eri osissa"
xlabel="X-akseli (etäisyys m)"
ylabel="Y-akseli (etäisyys m)"
zlabel="Z-arvo (viipymä minutteina)"

createScatterPlotWithIntensity(x,y,z,title, xlabel, ylabel, zlabel, "customers.png")

