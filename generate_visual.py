import matplotlib.pyplot as plt
import numpy as np

# Create synthetic 0.5-degree grid data for Pakistan region
# Coordinates roughly: Lat 24-37, Lon 61-75
data = np.random.randn(26, 28) 

plt.figure(figsize=(10, 6))
plt.imshow(data, cmap='RdBu_r', extent=[61, 75, 24, 37])
plt.colorbar(label='Temperature Anomaly (Standard Deviations)')
plt.title('Synthetic NASA-Bartik Climate Shock Map: South Asia Grid')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save the visual
plt.savefig('visuals/climate_shock_sample.png')
print("Visual generated and saved to visuals/folder.")
