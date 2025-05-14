# Import statements.
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Create a list.
my_list = [10, 'gold', 'dollars']

# Use the helper function to calculate F1 score used in the following graphics.
def f1_score(precision, recall):
    score = 2 * precision * recall / (precision + recall)
    score = np.nan_to_num(score)
    return score

# Generate a graph of F1 score for different precision and recall scores.
x = np.linspace(0, 1, 101)
y = np.linspace(0, 1, 101)
X, Y = np.meshgrid(x, y)
Z = f1_score(X, Y)

fig = plt.figure()
fig.set_size_inches(10, 10)
ax = fig.add_subplot(111, projection='3d')  # Use fig.add_subplot instead of plt.axes

# Plot the surface.
ax.plot_surface(X, Y, Z, rstride=2, cstride=3, cmap='plasma')

# Set the title and labels.
ax.set_title('$F_{1}$ of precision, recall', size=18)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_zlabel('F1 Score')
ax.view_init(35, -65)

# Show the plot.
plt.show()
