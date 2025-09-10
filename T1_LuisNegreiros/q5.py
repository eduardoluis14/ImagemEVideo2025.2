 #Quatro transformadas radiométricas: (1) Expansão de contraste linear, (2) Compressão e expansão, (3) Dente de serra e (4) Transformada do logaritmo.
import cv2
import numpy as np

# za é limte inferior
# zb é o limite superior
def expansao_contraste_linear(imagem, za, zb):
    z1 = 0 # novo mínimo
    zn = 255 # novo máximo
    
    img_saida = np.copy(imagem)
    
    if za >= zb:
        fator_de_expansao = 1
    else:
        fator_de_expansao = (zn - z1) / (zb - za)
        
    altura = img_saida.shape[0]
    largura = img_saida.shape[1]
    for i in range(0, altura):
        for j in range(0, largura):
            
            b_original = imagem[i][j][0]
            g_original = imagem[i][j][1]
            r_original = imagem[i][j][2]
        
            if b_original <= za:
                novo_b = z1
            elif b_original >= zb:
                novo_b = zn
            else:
                novo_b = int(round(fator_de_expansao * (b_original - za) + z1))
                
            if g_original <= za:
                novo_g = z1
            elif g_original >= zb:
                novo_g = zn
            else:
                novo_g = int(round(fator_de_expansao * (g_original - za) + z1))
                
            if r_original <= za:
                novo_r = z1
            elif r_original >= zb:
                novo_r = zn
            else:
                novo_r = int(round(fator_de_expansao * (r_original - za) + z1))
            
            img_saida[i][j][0] = novo_b
            img_saida[i][j][1] = novo_g
            img_saida[i][j][2] = novo_r
    
    return img_saida

def compreensao_e_expansao(imagem):
    min = 85
    maxi = 170
    
    img_saida = np.copy(imagem)
    
    altura = img_saida.shape[0]
    largura = img_saida.shape[1]
    for i in range(0, altura):
        for j in range(0, largura):
            b_original = imagem[i][j][0]
            g_original = imagem[i][j][1]
            r_original = imagem[i][j][2]
            
            if b_original <= min:
                novo_b = int(round(b_original/2))
            elif b_original > min and b_original < maxi:
                novo_b = int(round((2 * b_original) - 127))
            else:
                novo_b = int(round((b_original/2) + 128))
            
            if g_original <= min:
                novo_g = int(round(g_original/2))
            elif g_original > min and g_original < maxi:
                novo_g = int(round((2 * g_original) - 127))
            else:
                novo_g = int(round((g_original/2) + 128))
                
            if r_original <= min:
                novo_r = int(round(r_original/2))
            elif r_original > min and r_original < maxi:
                novo_r = int(round((2 * r_original) - 127))
            else:
                novo_r = int(round((r_original/2) + 128))
            
            novo_b = np.clip(novo_b, 0, 255)
            novo_g = np.clip(novo_g, 0, 255)
            novo_r = np.clip(novo_r, 0, 255)
            
            img_saida[i][j][0] = novo_b
            img_saida[i][j][1] = novo_g
            img_saida[i][j][2] = novo_r
    return img_saida

def dente_de_serra(imagem):
# --- main ---
img = cv2.imread("../Imagens/imagem_baixo_contraste.jpg")

if img is None:
    print("Erro: não foi possível carregar a imagem!")
else:
    img2 = expansao_contraste_linear(img, 48, 200)
    cv2.imwrite("q5_contraste_linear.jpg", img2)
    print("Imagem salva como 'q5_contraste_linear.jpg'")