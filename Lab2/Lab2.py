import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DS8.txt', delim_whitespace=True, header=None, names=['x', 'y'])

fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=100)

ax.scatter(data['x'], data['y'], c='blue')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Lab№2 result image')

plt.savefig('scatter_plot.png', dpi=100)
plt.show()