import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem colorida
imagem_rgb = cv2.imread('im01.jpg')

# Convertendo a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2GRAY)

# Aplicando o filtro Sobel
sobel_x = cv2.Sobel(imagem_gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem_gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculando a magnitude do gradiente
magnitude_gradiente = np.sqrt(sobel_x**2 + sobel_y**2)

# Normalizando os valores para o intervalo de 0 a 255
magnitude_gradiente = cv2.normalize(magnitude_gradiente, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2RGB))
plt.title('Original (RGB)')

plt.subplot(1, 3, 2)
plt.imshow(imagem_gray, cmap='gray')
plt.title('Escala de Cinza')

plt.subplot(1, 3, 3)
plt.imshow(magnitude_gradiente, cmap='gray')
plt.title('Detecção de Bordas (Sobel)')

plt.show()
