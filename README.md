# Comparador de Imagens de Periféricos

Projeto desenvolvido em Python para comparar imagens utilizando matrizes de pixels.

## Objetivo

O objetivo do programa é identificar qual imagem é mais semelhante a uma imagem de teste, comparando-a com um conjunto de imagens base de periféricos.

## Como funciona

1. As imagens são carregadas pelo programa.
2. Cada imagem é convertida para **escala de cinza**.
3. As imagens são redimensionadas para o mesmo tamanho.
4. Cada imagem é transformada em uma **matriz de pixels**.
5. O algoritmo calcula a **distância euclidiana** entre a matriz da imagem de teste e as imagens base.
6. A imagem com menor distância é considerada a mais semelhante.

## Tecnologias utilizadas

- Python
- NumPy
- Pillow (PIL)
- Matplotlib

## Estrutura do projeto


comparador_perifericos
│
├ mouse.jpg
├ teclado.jpg
├ headset.jpg
├ controle.jpg
├ webcam.jpg
├ teste.jpg
└ program.py


## Como executar

1. Instalar as dependências:


pip install numpy pillow matplotlib


2. Executar o programa:


python program.py


## Resultado

O programa imprime no terminal qual imagem é mais semelhante à imagem de teste, com base na diferen
