import cv2
import numpy as numpy
from matplotlib import pyplot as plt

def load_image(path):
    return cv2.imread(path)

def show_image(image, turn, title):
    plt.subplot(2, 3, turn)
    plt.imshow(image)
    plt.title(title) 
    plt.show(block=False)

def show_gray_image(image, turn, title):
    plt.subplot(2, 3, turn)
    plt.imshow(image, cmap='gray')
    plt.title(title) 
    plt.show(block=False)

def edges_gray(image):
    try:
        image_gray = image
        if len(image_gray.shape) != 2:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        result = cv2.Canny(image_gray, 100, 200)
        
        return result
    except:
        print("Erro ao aplicar segmentação")
        return None

def edges_rgb(image):
    print("Bordas RGB")

def segmentation_gray(image, blocksize, c):
    try:
        image_gray = image
        if len(image_gray.shape) != 2:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        result = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)

        return result
    except:
        print("Erro ao aplicar segmentação")
        return None

def segmentation_rgb(image, blocksize, c):
    try:
        channel_b, channel_g, channel_r = cv2.split(image)

        adaptive_threshold_blue = cv2.adaptiveThreshold(channel_b, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)
        adaptive_threshold_green = cv2.adaptiveThreshold(channel_g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)
        adaptive_threshold_red = cv2.adaptiveThreshold(channel_r, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize, c)

        result = cv2.merge([adaptive_threshold_blue, adaptive_threshold_green, adaptive_threshold_red])

        return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    except:
        print("Erro ao aplicar segmentação")
        return None

def smoothing_gray(image, kernel, detour):
    try:
        image_gray = image
        if len(image_gray.shape) != 2:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        result = cv2.GaussianBlur(image_gray, (kernel, kernel), detour)

        return result
    except:
        print("Erro ao suavizar")
        return None

def smoothing_rgb(image, kernel, detour):
    try:
        channel_b, channel_g, channel_r = cv2.split(image)

        channel_b_smooth = cv2.GaussianBlur(channel_b, (kernel, kernel), detour)
        channel_g_smooth = cv2.GaussianBlur(channel_g, (kernel, kernel), detour)
        channel_r_smooth = cv2.GaussianBlur(channel_r, (kernel, kernel), detour)

        result = cv2.merge([channel_b_smooth, channel_g_smooth, channel_r_smooth])

        return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    except:
        print("Erro ao suavizar")
        return None

def equalization_gray(image):
    try:
        image_gray = image
        if len(image_gray.shape) != 2:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        result = cv2.equalizeHist(image_gray)

        return result
    except:
        print("Erro ao aplicar equalização")
        return None

def equalization_rgb(image):
    try:
        channel_b, channel_g, channel_r = cv2.split(image)

        channel_b_eq = cv2.equalizeHist(channel_b)
        channel_g_eq = cv2.equalizeHist(channel_g)
        channel_r_eq = cv2.equalizeHist(channel_r)

        result = cv2.merge([channel_b_eq, channel_g_eq, channel_r_eq])

        return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    except:
        print("Erro ao aplicar equalização")
        return None

def get_odd_float_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if numero % 2 == 0:
                print("Número deve ser ímpar")
            elif numero % 2 != 0:
                return value
        except ValueError:
            print("Entrada inválida")

def get_float_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Entrada inválida")

def get_option():
    while True:
        try:
            option = float(input())
            if 1 <= option <= 9:
                return option
            else:
                print("Entrada Inválida")
        except:
            print("Entrada Inválida")

def do_process(image):
    finished = False

    turn = 1
    image_result = image
    show_image(cv2.cvtColor(image_result, cv2.COLOR_BGR2RGB), turn, "Original")

    while not finished:
        print("Qual processo deseja aplicar na imagem?")
        print("1 - Equalização (RGB)")
        print("2 - Equalização (GRAY)")
        print("3 - Suavização (RGB)")
        print("4 - Suavização (GRAY)")
        print("5 - Segmentação por Limiar (RGB)")
        print("6 - Segmentação por Limiar (GRAY)")
        print("9 - Bordas (GRAY)")
        option = get_option()

        turn = turn + 1

        if option == 1:
            result = equalization_rgb(image_result)
            if result is not None:
                image_result = result
                show_image(image_result, turn, "Equalização")

        if option == 2:
            result = equalization_gray(image_result)
            if result is not None:
                image_result = result
                show_gray_image(image_result, turn, "Equalização Cinza")

        if option == 3 or option == 4:
            kernel = get_float_input("Tamanho do Kernel (Quanto maior mais intensa a suavização. Recomendação: 5) : ")
            detour = get_float_input("Desvio Padrão (Quanto maior mais intensa a suavização. Recomendação: 0 (Calculada automática)) : ")
            if option == 3:
                result = smoothing_rgb(image_result, kernel, detour)
                if result is not None:
                    image_result = result
                    show_image(image_result, turn, "Suavização")
            if option == 4:
                result = smoothing_gray(image_result, kernel, detour)
                if result is not None:
                    image_result = result
                    show_gray_image(image_result, turn, "Suavização Cinza")

        if option == 5 or option == 6:
            blockSize = get_odd_float_input(f"Tamanho da Vizinhança (Recomendação: 11): ")
            c = get_float_input(f"Compensação (Recomendação: 2): ")
            if option == 5:
                result = segmentation_rgb(image_result, blockSize, c)
                if result is not None:
                    image_result = result
                    show_image(image_result, turn, "Segmentação")       
            if option == 6:
                result = segmentation_gray(image_result, blockSize, c)
                if result is not None:
                    image_result = result
                    show_gray_image(image_result, turn, "Segmentação Cinza")

        _continue = input("Deseja continuar? (S/N)")
        if _continue.upper() == 'S':
            finished = False
        
        if _continue.upper() == 'N':
            finished = True

def main():
    finished = False

    while not finished:
        path = input("Digite o caminho da imagem: ")

        print(f"\nProcessando image: {path}")
        image = load_image(path)

        if image is not None:
            do_process(image)

        if image is None:
            print("Erro ao carregar a imagem")

        response = input("Deseja tentar com outra imagem? (S/N)")
        if response.upper() == 'S':
            finished = False
        
        if response.upper() == 'N':
            finished = True


if __name__ == "__main__":
    main()

