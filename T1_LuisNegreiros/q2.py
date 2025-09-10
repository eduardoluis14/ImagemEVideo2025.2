# 2. Imagem negativa (inversão de cores).

import cv2
import numpy as np

def imagem_negativa(imagem):
    img_saida = np.copy(imagem)

    altura = img_saida.shape[0]
    largura = img_saida.shape[1]
    for i in range(0, altura):
        for j in range(0, largura):

            r = int(img_saida[i][j][2])
            g = int(img_saida[i][j][1])
            b = int(img_saida[i][j][0])

            
            # Atualizando a imagem de saída
            img_saida[i][j][0] = 255 - b
            img_saida[i][j][1] = 255 - g
            img_saida[i][j][2] = 255 - r
    return img_saida

# --- main ---
valor_brilho = -50

img = cv2.imread("../Imagens/natureza_1.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
    exit()

img2 = imagem_negativa(img)
cv2.imwrite("q2.jpg", img2)
