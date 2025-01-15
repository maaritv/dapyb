import matplotlib.pyplot as plt
import numpy as np

# Kuvitteelliset lämpötilat kesä- ja heinäkuussa
kesakuu = np.random.normal(20, 5, 30)  # Keskimäärin 20 °C, hajonta 5 °C
heinakuu = np.random.normal(22, 4, 31)  # Keskimäärin 22 °C, hajonta 4 °C

# Lisää poikkeamat
kesakuu[5] = 42  # Kesäkuussa yksi poikkeama
heinakuu[10] = 50  # Heinäkuussa yksi poikkeama

# Data for plotting
data = [kesakuu, heinakuu]

# Plotataan laatikko-janakaavio
plt.figure(figsize=(10, 6))
plt.boxplot(data, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'),
            whiskerprops=dict(color='blue'),
            flierprops=dict(marker='o', color='red', markersize=8),
            medianprops=dict(color='darkblue'))

# Asetetaan kaavion otsikot ja selitteet
plt.xticks([1, 2], ["Kesäkuu", "Heinäkuu"])
plt.ylabel("Lämpötila (°C)")
plt.title("Kesä- ja heinäkuun päivien lämpötilat\n(poikkeamat korostettuina)")

# Näytetään kaavio
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("temperatures.png") 

plt.show()

