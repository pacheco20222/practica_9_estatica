import matplotlib.pyplot as plt
import numpy as np

# Datos para Primera Configuración
fuerza_1 = np.array([0.000, 0.4905, 0.981, 1.4715, 1.962, 2.4525, 2.943, 3.4335, 3.924])
elongacion_1 = np.array([0.000, 0.032, 0.100, 0.171, 0.247, 0.298, 0.389, 0.465, 0.535])

# Datos para Segunda Configuración
fuerza_2 = np.array([0.000, 0.4905, 0.981, 1.4715, 1.962, 2.4525, 2.943, 3.4335, 3.924])
elongacion_2 = np.array([0.000, 0.000, 0.000, 0.002, 0.013, 0.028, 0.044, 0.060, 0.075])

# Regresiones lineales
m1, b1 = np.polyfit(elongacion_1, fuerza_1, 1)
m2, b2 = np.polyfit(elongacion_2, fuerza_2, 1)

# Gráfica de la Primera Configuración
plt.figure(figsize=(8, 5))
plt.scatter(elongacion_1, fuerza_1, color='blue', label='Datos experimentales')
plt.plot(elongacion_1, m1 * elongacion_1 + b1, color='red', label=f'Regresión lineal (k ≈ {m1:.2f} N/m)')
plt.title('Primera Configuración: Fuerza vs Elongación')
plt.xlabel('Elongación (m)')
plt.ylabel('Fuerza (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Gráfica de la Segunda Configuración
plt.figure(figsize=(8, 5))
plt.scatter(elongacion_2, fuerza_2, color='green', label='Datos experimentales')
plt.plot(elongacion_2, m2 * elongacion_2 + b2, color='orange', label=f'Regresión lineal (k ≈ {m2:.2f} N/m)')
plt.title('Segunda Configuración: Fuerza vs Elongación')
plt.xlabel('Elongación (m)')
plt.ylabel('Fuerza (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
