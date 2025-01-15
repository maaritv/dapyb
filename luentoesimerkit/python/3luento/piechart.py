import matplotlib.pyplot as plt

# Viipaleiden nimet
labels = ['Omenat', 'Päärynät', 'Appelsiinit', 'Muut hedelmät']
sizes = [25, 20, 40, 15]  # Viipaleiden osuudet samassa järjestyksessä
colors = ['red', 'green', 'yellow', 'gray']  # Värit
explode = (0.1, 0, 0, 0)  #Omenan viipale on visuaalisesti hieman erotettu

# Luodaan piirasdiagrammi
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)
plt.title('Hedelmäosaston myynnin jakauma')

plt.savefig("temperatures.png") 

plt.show()
