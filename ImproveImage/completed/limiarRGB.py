import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem RGB
imagem_rgb = cv2.imread('img02.jpg')

# Separando os canais de cor
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_rgb)

# Aplicando a segmentação por limiar adaptativo a cada canal
limiar_adaptativo_azul = cv2.adaptiveThreshold(canal_azul, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
limiar_adaptativo_verde = cv2.adaptiveThreshold(canal_verde, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
limiar_adaptativo_vermelho = cv2.adaptiveThreshold(canal_vermelho, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Juntando os canais segmentados por limiar adaptativo
imagem_segmentada_rgb = cv2.merge([limiar_adaptativo_azul, limiar_adaptativo_verde, limiar_adaptativo_vermelho])

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2RGB))
plt.title('Original (RGB)')

plt.subplot(1, 2, 2)
plt.imshow(imagem_segmentada_rgb, cmap='gray')
plt.title('Segmentação por Limiar Adaptativo (RGB)')

plt.show()
