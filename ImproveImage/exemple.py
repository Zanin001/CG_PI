import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
imagem = cv2.imread('im01.jpg')

# Convertendo a imagem para escala de cinza (se necessário)
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Equalização de histograma para equilibrar as cores (pré-processamento)
imagem_eq = cv2.equalizeHist(imagem_gray)

# Filtro de suavização para remover ruídos
imagem_suavizada = cv2.GaussianBlur(imagem_eq, (5, 5), 0)

# Segmentação usando limiar adaptativo (se aplicável)
_, imagem_binaria = cv2.threshold(imagem_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Operações morfológicas para aprimorar a segmentação (se aplicável)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
imagem_morfo = cv2.morphologyEx(imagem_binaria, cv2.MORPH_CLOSE, elemento_estruturante)

# Criar a imagem final combinando todas as etapas
imagem_resultante = cv2.cvtColor(imagem.copy(), cv2.COLOR_BGR2RGB)
imagem_resultante[:,:,1] = cv2.bitwise_or(imagem_resultante[:,:,1], imagem_morfo)

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(2, 3, 2)
plt.imshow(imagem_eq, cmap='gray')
plt.title('Equalização de Histograma')

plt.subplot(2, 3, 3)
plt.imshow(imagem_suavizada, cmap='gray')
plt.title('Suavização')

plt.subplot(2, 3, 4)
plt.imshow(imagem_binaria, cmap='gray')
plt.title('Segmentação Binária')

plt.subplot(2, 3, 5)
plt.imshow(imagem_morfo, cmap='gray')
plt.title('Operações Morfológicas')

# Exibir a imagem resultante
plt.subplot(2, 3, 6)
plt.imshow(imagem_resultante)
plt.title('Imagem Resultante')

plt.show()
