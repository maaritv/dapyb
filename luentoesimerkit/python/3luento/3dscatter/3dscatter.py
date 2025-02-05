import pandas as pd
import matplotlib.pyplot as plt

## Mikäli muokkaat oman kuvaajasi tästä, tee toteutuksesta ensin 
## funktio! (kts. esimerkkinä barchart)

# Lue CSV-tiedosto pandasilla
# Korvaa 'data.csv' tiedostonimelläsi
data = pd.read_csv('customers.csv', delimiter=";")

# Oletetaan, että sarakkeiden nimet ovat 'x', 'y', 'z'
x = data['x']
y = data['y']
z = data['z']

# Värit tiheyden perusteella (esim. käytetään z-arvoja)
colors = z

# Piirretään 3D-hajontakuvio
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=50, edgecolor='k', alpha=0.8)
ax.set_title("3D-hajontakuvio CSV-datasta", fontsize=14)
ax.set_xlabel("X-akseli (etäisyys m)", fontsize=12)
ax.set_ylabel("Y-akseli (etäisyys m)", fontsize=12)
ax.set_zlabel("Z-akseli (viipymä min)", fontsize=12)

min_limit = min(x.min(), y.min())  # pienin arvo x- ja y-datasta
max_limit = max(x.max(), y.max())  # suurin arvo x- ja y-datasta
ax.set_xlim(min_limit, max_limit)  # Sama skaala x-akselille
ax.set_ylim(min_limit, max_limit)  # Sama skaala y-akselille

# Lisätään väripalkki
cbar = plt.colorbar(scatter, ax=ax, shrink=0.6, aspect=10)
cbar.set_label("Z-arvo (värikoodaus)", fontsize=12)

plt.savefig("asiakkaat.png") 
