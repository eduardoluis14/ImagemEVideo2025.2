# 1. Alteração de brilho. Um valor deve ser lido e passado por parâmetro para o procedimento de alteração de brilho da imagem.

import cv2
import numpy as np

def altera_o_brilho(imagem, alteracao):
    img_saida = np.copy(imagem)

    altura = img_saida.shape[0]
    largura = img_saida.shape[1]
    for i in range(0, altura):
        for j in range(0, largura):

            # Pegando cada banda de cor
            # Convertendo para int
            # Motivo, as matrizes do openCv são do tipo uint8 (inteiro de 8 bits sem sinal)
            # Por conta disso, se os valores forem menores que 0 ou maiores que 255, ele vai dar a volta e vai passar pelo teste sem ser percebido

            r = int(img_saida[i][j][2])
            g = int(img_saida[i][j][1])
            b = int(img_saida[i][j][0])
            
            # Alterando o brilho
            novo_r = alteracao + r
            novo_g = alteracao + g
            novo_b = alteracao + b

            # Limitando os valores entre 0 e 255
            if novo_r > 255: 
                novo_r = 255
            elif novo_r < 0: 
                novo_r = 0

            if novo_g > 255: 
                novo_g = 255
            elif novo_g < 0: 
                novo_g = 0

            if novo_b > 255: 
                novo_b = 255
            elif novo_b < 0: 
                novo_b = 0
            
            # Atualizando a imagem de saída
            img_saida[i][j][0] = novo_b
            img_saida[i][j][1] = novo_g
            img_saida[i][j][2] = novo_r
    return img_saida

# --- main ---
valor_brilho = -50

img = cv2.imread("../Imagens/natureza_1.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
    exit()

img2 = altera_o_brilho(img, valor_brilho)
cv2.imwrite("q1.jpg", img2)
