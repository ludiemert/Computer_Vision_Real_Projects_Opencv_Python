import  cv2

#abrir a camera
video = cv2.VideoCapture(0)

amostra = 1 #amostra (variavel) que vai iniciar com 1

while True:
    check,img = video.read()
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #converter para cinza

    if cv2.waitKey(1) & 0XFF ==ord('q'):  #capturar a img qdo pressionar o q dentro da pasta fotos p (positivas)
        imgR = cv2.resize(imgCinza,(220,220))  #alterar o tamanho da img 220 x 220
        cv2.imwrite(f'fotos/p/im{amostra}.jpg',imgR)     #para salvar, a cada amostra vai acrescentando um numero (vai acrescentar um num em cada img que salvarmos)
        amostra +=1   #cada vez que salvar uma img vai acrescentar o numer na img


    cv2.imshow('Captura img lampada', img)
    cv2.waitKey(1)