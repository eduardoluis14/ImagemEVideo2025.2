# 4. Histograma local. Defina um particionamento da imagem com no mínimo 3 partições. Concatenar os histogramas em um único vetor. Armazenar o resultado em um arquivo para facilitar a visualização do resultado

import cv2
import numpy as np 

# A funcao receba imagem que será analisada e o numero de particoes
# Se esse número for 3, você terá uma grade 3x3, totalizando 9 partições 
def gerar_histograma_local(imagem, num_particoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]
    
    altura_particao = altura // num_particoes
    largura_particao = largura // num_particoes
    
    todos_histogramas = {}
    vetor_concatenado = []
        
    for p in range(num_particoes):
        for q in range(num_particoes):
            inicio_altura = p * altura_particao
            inicio_largura = q * largura_particao
            
            if p == num_particoes - 1:
                fim_altura = altura
            else:
                fim_altura = (p + 1) * altura_particao
                
            if q == num_particoes - 1:
                fim_largura = largura
            else:   
                fim_largura = (q + 1) * largura_particao  
            
            hist_b = [0] * 256
            hist_g = [0] * 256
            hist_r = [0] * 256
            
            for i in range(inicio_altura, fim_altura):
                for j in range(inicio_largura, fim_largura):
                    r = imagem[i][j][2]
                    g = imagem[i][j][1]
                    b = imagem[i][j][0]
                    
                    hist_r[r] += 1
                    hist_g[g] += 1
                    hist_b[b] += 1
                    
            todos_histogramas[(p, q)] = (hist_b, hist_g, hist_r)
            vetor_concatenado.extend(hist_b + hist_g + hist_r)
            
    print("Cálculos concluídos. Total de histogramas em memória:", len(todos_histogramas))
    
    with open("histograma_local_final.txt", "w") as arquivo:
        
        # 2. Percorrendo os resultados que já estão guardados no dicionário
        # .items() nos dá acesso à chave e ao valor de cada item do dicionário
        for coordenadas, (h_b, h_g, h_r) in todos_histogramas.items():
            
            # 3. Escrevendo os dados de forma organizada
            arquivo.write(f"\n======================================================\n")
            arquivo.write(f"--- Histograma para a Partição nas coordenadas {coordenadas} ---\n")
            arquivo.write(f"======================================================\n")

            arquivo.write("\n--- Canal Azul (B) ---\n")
            for i, val in enumerate(h_b):
                arquivo.write(f"Intensidade {i}: {val}\n")
                
            arquivo.write("\n--- Canal Verde (G) ---\n")
            for i, val in enumerate(h_g):
                arquivo.write(f"Intensidade {i}: {val}\n")
                
            arquivo.write("\n--- Canal Vermelho (R) ---\n")
            for i, val in enumerate(h_r):
                arquivo.write(f"Intensidade {i}: {val}\n")

    print("Arquivo 'histograma_local_final.txt' foi salvo com sucesso!")
    return vetor_concatenado

# --- main ---
img = cv2.imread("../Imagens/natureza_1.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
else:
    num_particoes = 3
    histograma_local = gerar_histograma_local(img, num_particoes)
    print("\n--- Verificação Final ---")
    print(f"O tamanho total do vetor concatenado é: {len(histograma_local)}") # Para uma grade 3x3, o tamanho deve ser 3*3 * (256*3) = 9 * 768 = 6912
    print(f"Amostra dos 10 primeiros valores do vetor: {histograma_local[:10]}")
    print("Cálculo concluído com sucesso!")