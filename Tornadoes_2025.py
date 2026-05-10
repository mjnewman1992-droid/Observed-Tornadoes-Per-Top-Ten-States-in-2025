import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

states = ['Alabama', 'Colorado', 'Illinois', 'Iowa', 'Kansas', 'Mississippi', 'Missouri', 'Nebraska', 'Oklahoma', 'Texas']
count = [82, 71, 149, 142, 98, 76, 88, 105, 114, 192]
colors = ['darkorange', 'gold', 'firebrick', 'crimson', 'tomato', 'orange', 'coral', 'orangered', 'red', 'darkred']
bar = plt.bar(states, count, color=colors, width=0.5, edgecolor = 'black')
plt.bar_label(bar, padding=3, fontweight='bold')
plt.xlabel('States')
plt.xticks(rotation=45)
plt.ylabel('Number of Observed Tornadoes')
plt.title('Observed Tornadoes Per Top Ten States in 2025')
plt.tight_layout()
plt.show()