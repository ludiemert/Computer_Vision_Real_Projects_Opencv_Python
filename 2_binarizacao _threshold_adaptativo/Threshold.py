import cv2

#img = cv2.imread('img01.jpg')
img = cv2.imread('img02.jpg')
img = cv2.resize(img, (400,500)) # diminuir a resolucao

imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #para converter binalizacao primeiro converte para escala de cinza
imgCinza2 = cv2.resize(imgCinza,(400,500))


_,th1 = cv2.threshold(imgCinza2, 127,255,cv2.THRESH_BINARY) # _, representa a primeira variavel
#variavel que vai receber a img binarizada (img com 2 cores P e B) - THRESH_BINARY
# maior que 127 eh cor Branca e menor que 127 ele assue a cor preta


#corrigir sombra na img ( Threshold ADAPTIVE)
#block size 25 e 16 efeito sobre a img tem que ir fazendo testes
th2 = cv2.adaptiveThreshold(imgCinza2, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16)


#alterar o tipo de adaptacao = adapta o numero de Threshold  da img - ADAPTIVE_THRESH_MEAN_C
th3 = cv2.adaptiveThreshold(imgCinza2, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,16)



cv2.imshow('Original',img)
cv2.imshow('TH1 - img binarizada (img com 2 cores P e B) - THRESH_BINARY',th1) #127
cv2.imshow('TH2 - Corrigir sombra na img -Threshold ADAPTIVE',th2) #se adequa a necessidade da img
cv2.imshow('TH3 - Adapta o numero de Threshold da img - ADAPTIVE_THRESH_MEAN_C',th3)
cv2.waitKey(0)

