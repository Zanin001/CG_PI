import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem em escala de cinza
imagem_gray = cv2.imread('img02.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicando a segmentação por limiar adaptativo
limiar_adaptativo = cv2.adaptiveThreshold(
    imagem_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(imagem_gray, cmap='gray')
plt.title('Escala de Cinza (Original)')

plt.subplot(1, 2, 2)
plt.imshow(limiar_adaptativo, cmap='gray')
plt.title('Segmentação por Limiar Adaptativo')

plt.show()