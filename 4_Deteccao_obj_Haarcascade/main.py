import  cv2

#Abrir a webcan

#variavel
camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_eye.xml')  #classificador #1 test q faz identificador dos olhos

while True:

    check, img = camera.read()

    cv2.imshow('Imagem', img) #img da camera
    cv2.waitKey(1)