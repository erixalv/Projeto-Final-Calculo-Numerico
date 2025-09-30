import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

# === CONFIGURAÇÕES ===
img = imread("Screen06.png")      
num_fatias = 10               
x_min, x_max = 451, 934       
escala = 0.025                 

# === GERAR LINHAS VERTICAIS ===
xs = np.linspace(x_min, x_max, num_fatias)

plt.imshow(img)
for x in xs:
    plt.axvline(x, color='red', linestyle='--')
plt.title("Clique na borda superior e inferior de cada linha")
pontos = plt.ginput(num_fatias*2) 
plt.close()

# === ORGANIZAR PONTOS ===
pontos = np.array(pontos)
x_vals = pontos[:,0]
y_vals = pontos[:,1]

y_sup = y_vals[0::2]
y_inf = y_vals[1::2]
f = y_sup - y_inf  

# === INTEGRAÇÃO NUMÉRICA ===
h = (x_max - x_min) / (num_fatias - 1)

# Trapézios
area_trap_px = (h/2) * (f[0] + 2*sum(f[1:-1]) + f[-1])

# Simpson (se número de intervalos for par)
if (num_fatias-1) % 2 == 0:
    area_simp_px = (h/3) * (f[0] + f[-1] + 4*sum(f[1:-1:2]) + 2*sum(f[2:-2:2]))
else:
    area_simp_px = None

# === CONVERSÃO PARA METROS² ===
area_trap_m2 = abs(area_trap_px) * (escala**2)
area_simp_m2 = abs(area_simp_px) * (escala**2) if area_simp_px else None

# === RESULTADOS ===
print("Área (Trapézios):", area_trap_px, "px² →", area_trap_m2, "m²")
if area_simp_m2:
    print("Área (Simpson):", area_simp_px, "px² →", area_simp_m2, "m²")
