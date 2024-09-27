import cv2

# Carregar o vídeo
video = cv2.VideoCapture('video.mp4')

# Loop para rodar o vídeo
while True:
    # Ler o frame do vídeo
    check, img = video.read()

    # Se o vídeo acabar, sair do loop
    if not check:
        break

    # Desenhar formas
    cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 5)
    cv2.circle(img, (120, 120), 50, (0, 0, 255), 5)
    cv2.line(img, (30, 40), (100, 100), (0, 255, 0), 2)

    # Adicionar texto
    texto = 'Exemplo OpenCV'
    cv2.putText(img, texto, (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Exibir o frame
    cv2.imshow('Video com Formas e Texto', img)

    # Sair do loop ao pressionar 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar as janelas
video.release()
cv2.destroyAllWindows()

#FORMAS GEOMETRICAS EM VIDEOS
#from tabnanny import check

import cv2

# Carregar o vídeo
video = cv2.VideoCapture('runners.mp4')

# Definir o novo tamanho (largura, altura)
largura = 640
altura = 480

# Loop para rodar o vídeo
while True:
    # Ler o frame do vídeo
    check, img = video.read()  # variáveis

    # Se o vídeo acabar, sair do loop
    if not check:
        break

    # Redimensionar o frame para as dimensões desejadas
    frame_redimensionado = cv2.resize(img, (largura, altura))

    # Desenhar formas e adicionar texto
    cv2.rectangle(frame_redimensionado, (50, 50), (200, 200), (255, 0, 0), 5)
    cv2.circle(frame_redimensionado, (120, 120), 50, (0, 0, 255), 5)
    cv2.line(frame_redimensionado, (30, 40), (100, 100), (0, 255, 0), 2)
    texto = 'Piramide do Egito'
    cv2.putText(frame_redimensionado, texto, (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Exibir o frame redimensionado com as formas e o texto
    cv2.imshow('Imagem', frame_redimensionado)

    # Sair do loop ao pressionar a tecla 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
       break
    #cv2.waitKey(10)

# Liberar o vídeo e fechar as janelas
video.release()
cv2.destroyAllWindows()



#FORMAS GEOMETRICAS EM FIGURAS
#import cv2

#img = cv2.imread('piramide.jpg')

#retangulo na imagem
#cv2.rectangle(img,(50,50),(200,200),(255,0,0),5)
#retangulo na imagem (nao precisa de variavel so usar o formato)
#ponto inicial em px (50,50) 50 no eixo y e 50 no eixo x
# e o 3 parametro eh o ponto final do retangulo eixos(200y e 200x)
#em seguida a cor que coloca em RGB (0,0,0) dar peso e formar outra cor(255,0,0)
# expessura da imagem 5


#para um retangulo pintado
#cv2.rectangle(img,(50,50),(200,200),(255,0,0),-1)


#curculo na imagem
#cv2.circle(img,(300,300),(50),(0,0,255),5)
#inicio do circulo = centro = (200,200)
# e o raio "tamanho do circulo" (,)
# e a cor = vermelho (0,0,255)
# expessura da imagem 5

# expessura da imagem 1 - a cor ocupa toda a img
#cv2.circle(img,(300,300),(50),(0,0,255),-1)

#colocar linha na img
#colocar ponto inicial e ponto final
#cv2.line(img,(300,400),(500,300),(0,255,0),2)


#inserir texto dentro da img
#texto = 'Piramide do Egito'
#cv2.putText(img, texto,(200,200), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)

#coloca onde o texto se inicia(posicao) (200,200)
#prox fonte (FONT_HER_SEMP)
#tamanho da font e a cor


#cv2.imshow('Imagem', img)
#cv2.waitKey(0)