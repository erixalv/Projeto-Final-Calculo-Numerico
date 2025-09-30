import matplotlib.pyplot as plt
from matplotlib.image import imread

# === CONFIGURAÇÕES ===
img = imread("Screen07.png")   # imagem do campeão dentro do jogo
altura_real_m = 1.95           # altura oficial do campeão em metros (troque pela da lore)

# === MOSTRAR IMAGEM ===
plt.imshow(img)
plt.title("Clique no topo da cabeça e nos pés do campeão")
pontos = plt.ginput(2)  # clique 1 = topo, clique 2 = pés
plt.close()

# === CALCULAR ALTURA EM PIXELS ===
(y_topo, y_pes) = (pontos[0][1], pontos[1][1])
altura_px = abs(y_pes - y_topo)

# === CALCULAR ESCALA ===
escala = altura_real_m / altura_px  # metros por pixel

print("Altura medida em pixels:", altura_px)
print("Altura real:", altura_real_m, "m")
print("Escala:", escala, "metros/pixel")
print("Escala ao quadrado:", escala**2, "m²/pixel² (para converter áreas)")
