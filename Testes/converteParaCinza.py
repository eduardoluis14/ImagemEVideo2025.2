import cv2
import numpy as np

def transforma_para_cinza(imagem):

    altura = imagem.shape[0]
    largura = imagem.shape[1]
    for i in range(0, altura):
        for j in range(0, largura):
            r = imagem[i][j][2]
            g = imagem[i][j][1]
            b = imagem[i][j][0]
            imagem[i][j][0] = 0.299*r + 0.587*g + 0.114*b
            imagem[i][j][1] = 0.299*r + 0.587*g + 0.114*b
            imagem[i][j][2] = 0.299*r + 0.587*g + 0.114*b
    return imagem

# --- main ---
img = cv2.imread("../Imagens/natureza_1.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
    exit()

img2 = transforma_para_cinza(img)
cv2.imwrite("../Imagem_Saida/saida_cinza.jpg", img2)
