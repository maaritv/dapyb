import numpy as np
import matplotlib.pyplot as plt

categories = ['Omakotitalot', 'Rivitalot', 'Luhtitalot', 'Kerrostalot']
values = [53, 24, 10, 6]  # Rakennusten lukumäärä samassa järjestyksessä

# Luo pylväsdiagrammi
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'orange', 'green', 'purple'])

plt.title('Firma Oy:n rakentamat talot talotyypeittäin vuonna 2024', fontsize=16)
plt.xlabel('Talotyyppi', fontsize=14)
plt.ylabel('Rakennettujen talojen määrä (kpl)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(fontsize=14)  # X-akselin fonttikoko
plt.yticks(fontsize=14)  # Y-akselin fonttikoko

plt.savefig("houses.pdf") 

# Show the bar chart
plt.show()
