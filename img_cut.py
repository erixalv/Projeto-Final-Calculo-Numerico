import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread

# === CONFIGURAÇÕES ===
try:
    img = imread("Screen06.png")
except FileNotFoundError:
    print("Erro: A imagem 'Screen06.png' para cálculo de área não foi encontrada.")
    exit()
    
num_fatias = 10
x_min, x_max = 451, 934
escala = 0.025


# === GERAR LINHAS VERTICAIS E OBTER PONTOS DO USUÁRIO ===
xs = np.linspace(x_min, x_max, num_fatias)

plt.imshow(img)
for x in xs:
    plt.axvline(x, color='cyan', linestyle='--')
plt.title(f"Clique na borda SUPERIOR e INFERIOR de cada uma das {num_fatias} linhas")
pontos = plt.ginput(num_fatias * 2, timeout=0)
plt.close()

if len(pontos) < num_fatias * 2:
    print("Você não selecionou todos os pontos necessários. Encerrando o programa.")
    exit()

# === ORGANIZAR PONTOS E CALCULAR ALTURAS (f) ===
pontos = np.array(pontos)
y_vals = pontos[:, 1]
y_sup = y_vals[0::2]
y_inf = y_vals[1::2]
f = abs(y_sup - y_inf) # Altura de cada fatia em pixels


# === INTEGRAÇÃO NUMÉRICA ===
h = (x_max - x_min) / (num_fatias - 1)
num_intervalos = num_fatias - 1

# --- 1. Método dos Trapézios (Sempre calculado) ---
area_trap_px = (h / 2) * (f[0] + 2 * sum(f[1:-1]) + f[-1])

# --- 2. Método de Simpson (Adaptado para sempre calcular) ---
area_simp_px = 0
if num_intervalos % 2 == 0:
    print("\n(Info: Número de intervalos é par, Simpson 1/3 foi usado em toda a área.)")
    area_simp_px = (h / 3) * (f[0] + f[-1] + 4 * sum(f[1:-1:2]) + 2 * sum(f[2:-2:2]))
else:
    print("\n(Info: Número de intervalos é ímpar. Simpson foi combinado com Trapézio no último intervalo.)")
    if num_intervalos > 1:
        area_simp_px += (h / 3) * (f[0] + f[-2] + 4*sum(f[1:-2:2]) + 2*sum(f[2:-3:2]))
    area_simp_px += (h / 2) * (f[-2] + f[-1])


# === CONVERSÃO PARA METROS² ===
escala_area = escala**2
area_trap_m2 = area_trap_px * escala_area
area_simp_m2 = area_simp_px * escala_area

# ==============================================================================
# === RESULTADOS FINAIS (COM AJUSTE DE FATOR 10) ===
# ==============================================================================

# Fator de ajuste solicitado para multiplicar os resultados finais.
fator_ajuste = 10.0

# Aplica o fator de ajuste
area_final_trap = area_trap_m2 * fator_ajuste
area_final_simp = area_simp_m2 * fator_ajuste

print("\n" + "="*55)
print(" " * 19 + "RESULTADOS FINAIS")
print("="*55)

print("\n--- Método dos Trapézios ---")
print(f"Área em pixels ........: {area_trap_px:15,.2f} px²")
print(f"Área calculada .........: {area_final_trap:15,.4f} m² (Resultado x{fator_ajuste})")

print("\n--- Método de Simpson ---")
print(f"Área em pixels ........: {area_simp_px:15,.2f} px²")
print(f"Área calculada .........: {area_final_simp:15,.4f} m² (Resultado x{fator_ajuste})")

print("\n" + "="*55)