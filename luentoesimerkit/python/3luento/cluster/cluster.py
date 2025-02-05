import matplotlib.pyplot as plt

# Työntekijöiden klusterien data (yksinkertaistettu esimerkki)
# Istumatyöntekijät (matala aktiivisuus, korkea tasapainoisuus)
istumatyontekijat = {
    "aktiivisuus": [1, 2, 1.5, 2.2, 1.8],  # Matala aktiivisuus
    "tasapainoisuus": [8, 7.5, 8.2, 7.8, 8.1]  # Korkea tasapainoisuus
}

# Kenttäoperaattorit (korkea aktiivisuus, matala tasapainoisuus)
kenttaoperaattorit = {
    "aktiivisuus": [7, 8.5, 7.8, 8.2, 8],  # Korkea aktiivisuus
    "tasapainoisuus": [3, 2.5, 3.2, 2.8, 3.1]  # Matala tasapainoisuus
}

# Piirretään hajontakaavio
plt.figure(figsize=(8, 6))
plt.scatter(istumatyontekijat["aktiivisuus"], istumatyontekijat["tasapainoisuus"], 
            color="blue", label="Istumatyöntekijät", s=100)
plt.scatter(kenttaoperaattorit["aktiivisuus"], kenttaoperaattorit["tasapainoisuus"], 
            color="green", label="Kenttäoperaattorit", s=100)

# Asetetaan kaavion otsikot ja selitteet
plt.title("Työntekijäklusterit elintapojen perusteella")
plt.xlabel("Aktiivisuusaste")
plt.ylabel("Elintapojen tasapainoisuus")
plt.legend()
plt.grid(alpha=0.5)

plt.savefig("lifestyles.pdf") 
plt.savefig("lifestyles.svg") 

plt.show()

