import numpy as np
import matplotlib.pyplot as plt

# Data: years and sales trends
years = np.arange(2017, 2024)
apple_sales = [2000, 2100, 1900, 2600, 2800, 2700, 3000]  # Npuseva trendi nähtävissä
pear_sales = [4000, 4100, 3800, 3100, 3000, 2500, 2400]   # Laskevaa trendiä

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(years, apple_sales, marker='o', label='Omenat (euroa)', color='red', linewidth=2)
plt.plot(years, pear_sales, marker='o', label='Päärynät (euroa)', color='green', linewidth=2)

# Add labels, title, and legend
plt.title('Omenien ja päärynöiden myynnin kehitys (2017-2024)', fontsize=14)
plt.xlabel('Vuosi', fontsize=12)
plt.ylabel('Myynti (euroa)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

##talletetaan kuva tiedostoon raporttiin liittämistä varten
plt.savefig("sales.png") 
plt.savefig("sales.pdf")
plt.savefig("sales.svg")


