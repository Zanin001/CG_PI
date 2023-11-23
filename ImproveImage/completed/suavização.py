import cv2
import matplotlib.pyplot as plt

# Carregando a imagem colorida
imagem_rgb = cv2.imread('im01.jpg')

# Separando os canais de cor
canal_b, canal_g, canal_r = cv2.split(imagem_rgb)

# Aplicando a suavização Gaussiana em cada canal
canal_b_suavizado = cv2.GaussianBlur(canal_b, (7, 7), 0)
canal_g_suavizado = cv2.GaussianBlur(canal_g, (7, 7), 0)
canal_r_suavizado = cv2.GaussianBlur(canal_r, (7, 7), 0)

# Combinando os canais de volta em uma imagem RGB suavizada
imagem_rgb_suavizada = cv2.merge([canal_b_suavizado, canal_g_suavizado, canal_r_suavizado])

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2RGB))
plt.title('Original (RGB)')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagem_rgb_suavizada, cv2.COLOR_BGR2RGB))
plt.title('Suavizada (RGB)')

plt.show()
