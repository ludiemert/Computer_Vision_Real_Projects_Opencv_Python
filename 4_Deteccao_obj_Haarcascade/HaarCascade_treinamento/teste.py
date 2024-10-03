import cv2

#arquivo que ele vai ler
classificador = cv2.CascadeClassifier('cascade.xml')

#abrir webcam
camera = cv2.VideoCapture(0)

#loop para rodar a img
while True:
    check, img = camera.read()

    #from captura import imgCinza
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # aplicar o classificador a img, 1 transf em cimza
    objetos = classificador.detectMultiScale(imgCinza,scaleFactor=1.2) #detecta objeto

    if len(objetos) ==0:   #se for igual a 0 nada vai acontecer, vai passar (pass)
        pass
    if len(objetos) !=0:  #se a variavel obj for diferente de 0 entao coloca o retangulo ao redor do obj
        for (x,y,l,a) in objetos:  #percorre o obj e extrai as dimensoes, dentro da variavel objet
            cv2.rectangle(img,(x,y),(x+l,y+a),(0,255,0),2)

    cv2.imshow('Camera',img)
    cv2.waitKey(1)

