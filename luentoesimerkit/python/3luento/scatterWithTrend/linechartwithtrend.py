import numpy as np
import matplotlib.pyplot as plt

# Data: yöunen pituus (tunnit) ja kahvin kulutus (kupit/päivä)
younen_pituus = [4, 5, 6, 7, 8, 9]
kahvin_kulutus = [5, 4, 3, 2, 1.5, 1]

# Luodaan hajontakaavio
plt.figure(figsize=(8, 6))
plt.scatter(younen_pituus, kahvin_kulutus, color='brown', s=100, alpha=0.8, edgecolors='black')

# Lisätään selitteet ja otsikko
plt.title("Yöunen pituuden ja kahvin kulutuksen välinen yhteys", fontsize=14)
plt.xlabel("Yöunen pituus (tuntia)", fontsize=12)
plt.ylabel("Kahvin kulutus (kupillista/päivä)", fontsize=12)

# Korostetaan negatiivista korrelaatiota trendiviivalla
z = np.polyfit(younen_pituus, kahvin_kulutus, 1)
p = np.poly1d(z)
plt.plot(younen_pituus, p(younen_pituus), color='darkred', linestyle='--', label='Trendiviiva')

plt.legend()
plt.grid(alpha=0.3)

plt.savefig("sleep_and_caffeine.png") 


