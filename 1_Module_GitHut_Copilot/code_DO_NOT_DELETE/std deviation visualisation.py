import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(loc=50, scale=10, size=100)

mean = np.mean(data)
std_dev = np.std(data)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, alpha=0.6, color='g', label='Data')

# Plot mean line
plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label='Mean')

# Shade ±1 std deviation
plt.axvspan(mean - std_dev, mean + std_dev, color='y', alpha=0.3, label='±1 Std Dev')

plt.title('Standard Deviation Visualization')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()
