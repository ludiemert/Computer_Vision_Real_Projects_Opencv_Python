# melhorar as imagens de numeros – transformacao morfologia
import cv2

#variaveis
img = cv2.imread('piramide.jpg') #carregar img = parametro
img = cv2.resize(img,(500, 300)) #altera o tamanho da img
imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #altera a cor da img p cinza
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0)    #aplicar a morfologia GaussianBlur = borrar a img
# (imgCinza(7,7))  matriz, linhas que vao sofrer a alteracao
imgCanny = cv2.Canny(img,50,100)   #destacar os contornos dentro da imagem
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=5) #dilatar a imagem de contornos (iterations=5) essa eh a dilatacao
#matriz que sofrera alteracao na imagem = linhas e colunas (5,5)
imgErode = cv2.erode(imgCanny ,(5,5),iterations=2) # Erode  = ele eh ao contrario da dilatacao, ele  cria uma erosao na imagem ele desfragmenta o obj
imgOpening = cv2.morphologyEx(imgCanny,cv2.MORPH_OPEN,(5,5)) # processo de Opening = erosao seguido da dilatação =  abertura da img = útil para tirar ruídos da img =
# limpa e deixa a imagem limpa ela eh a img central
imgClosing = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(5,5)) # processo de Closing  = MORPH_CLOSE  = ao contrario eh o processo de dilatação seguido de erosão =
# ele tentar limpar o objeto que esta na imagem = ele tenta fechar o objeto ele tira o ruído do objeto e não da imagem como um todo


#imshow para visualizar
#cv2.imshow('Img Original',img) #visualizar img
#cv2.imshow('Img Cinza',imgCinza)
#cv2.imshow('Img Bluer',imgBlur)
cv2.imshow('Img Canny',imgCanny)
#cv2.imshow('Img Dilat',imgDilat)
#cv2.imshow('Img Erode',imgErode)
cv2.imshow('Img Open',imgOpening)
cv2.imshow('Img Close',imgClosing)
cv2.waitKey(0)




#extrair a imagem da camera do celular
#import cv2

#video = cv2.VideoCapture()
#ip = "https://10.32.57.66:8080/video"   #variavel, end IP que eh mostrado no celular(end https)
#endereco completo para extrair a imagem

#video.open(ip) #exibir image

#while True: #looping
#    check,img = video.read() #leitura do video criar 2 variaveis
#   cv2.imshow("img", img)#mostrar a imagem
#   cv2.waitKey(1)#dar continuidade na imagem


#salvar img cv2 e
#recortar a img e ja ser salva
#cut an img

#import cv2
#img = cv2.imread('farol.jpg')
#dim = cv2.selectROI("Selecione a area de recorte",img,False)
#cv2.destroyWindow('Selecione a area de recorte')
#v1 = int(dim[0])
#v2 = int(dim[1])
#v3 = int(dim[2])
#v4 = int(dim[3])
#recorte = img[v2:v2+v4, v1:v1+v3]
#caminho = 'recortes/'
#nome_arquivo = input('Digite o nome do arquivo')
#cv2.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte)
#print('Imagem salva com sucesso🥳🥰')#print do prompt
#cv2.waitKey(0)



#com comentarios
#import cv2
#img = cv2.imread('farol.jpg')  #img variable

# open_cv will find the value in the img, func that gives the position in px of the img
#dim = cv2.selectROI("Selecione a area de recorte",img,False)
#cv2.destroyWindow('Selecione a area de recorte') #fechar a janela

#print with size
#print(dim)  #valuable saves the size of the cutout

#recorte = img[310:520, 120:420]
#fazer recorte com o mesmo tamanho do paint => (188, 309, 217, 206) um array
#v1 = int(dim[0])
#v2 = int(dim[1])
#v3 = int(dim[2])
#v4 = int(dim[3])

#fuc calculo
#recorte = img[v2:v2+v4, v1:v1+v3] #variavel

#funcao que salva a nova img
#diretorio = 'recortes/img01.jpg' #variavel
#caminho = 'recortes/'
#nome_arquivo = input('Digite o nome do arquivo')

#funcao concatenada
#cv2.imwrite(diretorio, recorte)
#cv2.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte)
#print('Imagem salva com sucesso🥳🥰')#print do prompt


#cv2.imshow('Imagem', img)
#cv2.imshow('Recorte', recorte)

#cv2.waitKey(0) ##nao fecha a img


#recortar uma img utilizando paint do windows
#import cv2
#img = cv2.imread('farol.jpg') #variavel da img
#print(img.shape)
#cv2.imshow('Imagem', img) #abre a img (640Y, 960X, 3Color)

#y-270-500
#x-170-400
# para extrair somente essa parte da img
#recorte = img[310:520, 120:420]
#print com o tamanho
#print(recorte.shape)
#cv2.imshow('Imagem', img)
#cv2.imshow('Recorte', recorte)

#cv2.waitKey(0) ##nao fecha a img



#como utilizar a img da webcam
#import  cv2

#camera = cv2.VideoCapture(0) #0 eh qdo a camera esta integrada no not

#setar config p melhorar img da webcan
#camera.set(3,640) #largura
#camera.set(4, 420) #altura
#camera.set(10,50) #brilho/luminosidade

#while True:
#    check, img = camera.read()

#    cv2.imshow('Web can', img)
#    if cv2.waitKey(1) & 0xFF ==ord('q'):
#        break  #assim que precionar o 'q' encerra o loop



#reprofuzir  um video
#import  cv2
#video = cv2.VideoCapture('runners.mp4')

#para ver o video precisa criar um loop infinito
#cada enter um frame (frame eh uma (1) img)
#
#while True:
#check,img = video.read()
#print(img.shape)    #ver tamanho desse video em px (resolucao), (0)pega somente 1 frame
#(1080, 1920, 3) img full-HD e colorida
#cv2.imshow('video', img)
#cv2.waitKey(0)   #waitKey(1) video roda rapido em 1miliseg(rapido)


#  imgRedim = cv2.resize(img,(640,420))   #redimencionar uma img (dx menor - resize)
# cv2.imshow('video', imgRedim)   #exibir a img redimencionada
#  cv2.waitKey(10)



#abrimos uma img
#import cv2
#img = cv2.imread('farol.jpg') #variavel da img
#imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # var  = comand que convert escala de img collor

#print(img.shape) #mostra a escala de PX
#print(imgGray.shape)
#print(imgGray) #px de como o computer le as cores

#cv2.imshow('Imagem', img) #abre a img
#cv2.imshow('Imagem Gray', imgGray)
#cv2.waitKey(0) ##nao fecha a img
