import cv2
import matplotlib.pyplot as plt

# Carregando a imagem colorida
imagem_rgb = cv2.imread('img01.jpg')

# Convertendo a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2GRAY)

# Aplicando o filtro de Canny
bordas_canny = cv2.Canny(imagem_gray, 100, 200)  # Ajuste os valores de limiar conforme necessário

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2RGB))
plt.title('Original (RGB)')

plt.subplot(1, 3, 2)
plt.imshow(imagem_gray, cmap='gray')
plt.title('Escala de Cinza')

plt.subplot(1, 3, 3)
plt.imshow(bordas_canny, cmap='gray')
plt.title('Detecção de Bordas (Canny)')

plt.show()
