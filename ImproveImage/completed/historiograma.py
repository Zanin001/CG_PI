import cv2
import matplotlib.pyplot as plt

# Carregando a imagem colorida
imagem_rgb = cv2.imread('im01.jpg')

# Separando os canais de cor
canal_b, canal_g, canal_r = cv2.split(imagem_rgb)

# Equalização de histograma para cada canal
canal_b_eq = cv2.equalizeHist(canal_b)
canal_g_eq = cv2.equalizeHist(canal_g)
canal_r_eq = cv2.equalizeHist(canal_r)

# Combinando os canais de volta em uma imagem RGB equalizada
imagem_rgb_equalizada = cv2.merge([canal_b_eq, canal_g_eq, canal_r_eq])

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2RGB))
plt.title('Original (RGB)')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagem_rgb_equalizada, cv2.COLOR_BGR2RGB))
plt.title('Equalizada (RGB)')

plt.show()
