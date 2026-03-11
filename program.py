from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def imagem_para_matriz(caminho, tamanho=(100,100)):
    img = Image.open(caminho).convert("L")   
    img = img.resize(tamanho)                
    matriz = np.array(img, dtype=np.float32)
    return matriz


def comparar(img1, img2):
    return np.linalg.norm(img1 - img2)


imagens_base = [
    "mouse.jpg",
    "teclado.jpg",
    "headset.jpg",
    "controle.jpg",
    "webcam.jpg"
]


imagem_teste = "teste3.jpg"


matriz_teste = imagem_para_matriz(imagem_teste)

resultados = []


for img in imagens_base:
    matriz_base = imagem_para_matriz(img)
    diferenca = comparar(matriz_teste, matriz_base)
    resultados.append((img, diferenca))


resultados.sort(key=lambda x: x[1])

print("Resultado da comparação:\n")

for nome, valor in resultados:
    print(nome, "-> diferença:", round(valor,2))

print("\nA máquina acha que a imagem mais parecida é:")
print(resultados[0][0])


plt.imshow(Image.open(imagem_teste))
plt.title("Imagem de teste")
plt.axis("off")
plt.show()