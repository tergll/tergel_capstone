import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

n = 50  # number of samples per class

def make_cluster(x_center, y_center, label):
    x = np.random.normal(x_center, 0.1, n)
    y = np.random.normal(y_center, 0.1, n)
    labels = [label] * n
    return np.column_stack((x, y)), labels

# Generate clusters
X_buuz, y_buuz = make_cluster(0.5, 0.2, "бууз")
X_khuushuur, y_khuushuur = make_cluster(0.8, 0.9, "хуушуур")
X_bansh, y_bansh = make_cluster(0.2, 0.1, "банш")

X = np.vstack([X_buuz, X_khuushuur, X_bansh])
y = np.array(y_buuz + y_khuushuur + y_bansh)

label_colors = {
    "бууз": "#7FB3D5",    
    "хуушуур": "#F5B041", 
    "банш": "#D5DBDB"     
}

# Create plot
plt.figure(figsize=(8, 6))

for label in np.unique(y):
    subset = X[y == label]
    plt.scatter(subset[:, 0], subset[:, 1],
                label=label,
                edgecolor='black',
                color=label_colors[label],
                s=70)

plt.xlabel("Хэмжээ (0 - 1 хооронд)", fontsize=12)
plt.ylabel("Шаргал хэмжээ (0 - 1 хооронд)", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
