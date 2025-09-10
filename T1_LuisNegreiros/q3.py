# 3. Histograma global. Gerar um vetor para representar o histograma da imagem. Concatenar o histograma de cada banda RGB em um único vetor. Armazenar o resultado em um arquivo texto para facilitar a visualização do resultado.

import cv2
import numpy as np

def gerar_histograma_global(imagem):
    
    # Primeiramente vamos inicializar três listas para cada canal (R, G, B)
    # Cada lista terá 256 posições (0-255) para contar a frequência de cada intensidade
    hist_r = [0] * 256
    hist_g = [0] * 256
    hist_b = [0] * 256

    altura = imagem.shape[0]
    largura = imagem.shape[1]

    # Depois, basicamente percorremos cada pixel da imagem e incrementamos o valor correspondente na lista do canal apropriado
    for i in range(altura):
        for j in range(largura):
            r = imagem[i][j][2]  # Canal R
            g = imagem[i][j][1]  # Canal G
            b = imagem[i][j][0]  # Canal B

            # Incrementa o valor do histograma para cada canal
            hist_r[r] += 1
            hist_g[g] += 1
            hist_b[b] += 1

    # Finalmente, concatenamos os três histogramas em um único vetor
    histograma_global = hist_b + hist_g + hist_r

    # Salvamos o histograma em um arquivo texto
    print("Salvando resultado em 'histograma_global.txt'...")
    with open("histograma_global_img_ruim.txt", "w") as arquivo:
        arquivo.write("--- Histograma Canal Azul (B) ---\n")
        for i, val in enumerate(hist_b):
            arquivo.write(f"Intensidade {i}: {val}\n")
            
        arquivo.write("\n--- Histograma Canal Verde (G) ---\n")
        for i, val in enumerate(hist_g):
            arquivo.write(f"Intensidade {i}: {val}\n")
            
        arquivo.write("\n--- Histograma Canal Vermelho (R) ---\n")
        for i, val in enumerate(hist_r):
            arquivo.write(f"Intensidade {i}: {val}\n")
    
    print("Histograma salvo com sucesso!")
    return histograma_global

# --- main ---

img = cv2.imread("../Imagens/imagem_baixo_contraste.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
else:
    histograma = gerar_histograma_global(img)
    print(f"Tamanho do vetor concatenado: {len(histograma)}")
    print("\nAmostra do Histograma Global (primeiros 10 valores do azul):", histograma[:10])
