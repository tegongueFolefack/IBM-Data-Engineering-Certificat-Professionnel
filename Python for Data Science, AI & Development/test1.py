import pandas as pd
import matplotlib.pyplot as plt

data = [
    ['Mercury', 2440, 0], 
    ['Venus', 6052, 0], 
    ['Earth', 6371, 1],
    ['Mars', 3390, 2], 
    ['Jupiter', 69911, 80], 
    ['Saturn', 58232, 83],
    ['Uranus', 25362, 27], 
    ['Neptune', 24622, 14]
]

cols = ['Planet', 'radius_km', 'moons']
planets = pd.DataFrame(data, columns=cols)

# Afficher le DataFrame
print(planets)

# Pour visualiser les données, par exemple, avec un graphique
plt.bar(planets['Planet'], planets['radius_km'])
plt.xlabel('Planets')
plt.ylabel('Radius (km)')
plt.title('Radius of Planets')
plt.show()
