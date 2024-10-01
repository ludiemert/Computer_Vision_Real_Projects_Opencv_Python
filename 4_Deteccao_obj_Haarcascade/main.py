import cv2
# Abrir a UM VIDEO  e fazer a leitura das pessoas - corpo inteiro


# Abrir o video
camera = cv2.VideoCapture('video.mp4') #aqui faz  a leitura do video

# Carregar o classificador de olhos
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_fullbody.xml') #se quiser outro resultado so trocar o aqruivo

while True:
    check, img = camera.read()  # Captura o frame da câmera

    # Redimensiona a imagem capturada
    img_resized_color = cv2.resize(img, (300, 300))  # Reduz a imagem colorida
    img_resized = cv2.resize(img, (300, 300))        # Outra redução de tamanho

    # Converte a imagem para escala de cinza
    imgGray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)


    #aplicar o classificador na img_cinza
    #variavel, ela detecta obj dentro da img e retornar as coordenadas de onde esse ob esta
    objetos = classificador.detectMultiScale(imgGray, minSize=(50,50),scaleFactor=1.5) #uma area 50px por 50px
    #objetos = classificador.detectMultiScale(imgGray)
    #scaleFactor => fator de escala do obj

    #print(objetos) #os numeros sao coordenadas em formato de px [[164 171  26  26]] que eh a estrutura da img

    for x,y,l,a in objetos: #estrutura for que percorre a variavel obj e extrai as coordenadas x,y,l,a
        cv2.rectangle(img_resized,(x,y),(x+l, y+a),(255,0,0),2)  #para fazer o retangulo

    # Exibe as imagens
    cv2.imshow('Imagem Colorida Redimensionada', img_resized)
    cv2.imshow('Imagem Cinza Redimensionada', imgGray)

    cv2.waitKey(10) #deixa o video mais lento





    # Abrir a webcam = IMG
#camera = cv2.VideoCapture(0)

# Carregar o classificador de olhos
#classificador = cv2.CascadeClassifier(r'cascades/haarcascade_smile.xml') #se quiser outro resultado so trocar o aqruivo

#while True:
    #    check, img = camera.read()  # Captura o frame da câmera

    # Se não for possível capturar a imagem da câmera
    #    if not check:
    #       print("Não foi possível capturar a imagem da câmera...")
    #break

    # Redimensiona a imagem capturada
    #   img_resized_color = cv2.resize(img, (300, 300))  # Reduz a imagem colorida
    #    img_resized = cv2.resize(img, (300, 300))        # Outra redução de tamanho

    # Converte a imagem para escala de cinza
    #   imgGray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)


    #aplicar o classificador na img_cinza
    #variavel, ela detecta obj dentro da img e retornar as coordenadas de onde esse ob esta
    #   objetos = classificador.detectMultiScale(imgGray, minSize=(50,50),scaleFactor=1.5) #uma area 50px por 50px
    #scaleFactor => fator de escala do obj

    #print(objetos) #os numeros sao coordenadas em formato de px [[164 171  26  26]] que eh a estrutura da img

    #  for x,y,l,a in objetos: #estrutura for que percorre a variavel obj e extrai as coordenadas x,y,l,a
    #       cv2.rectangle(img_resized,(x,y),(x+l, y+a),(255,0,0),2)  #para fazer o retangulo

    # Exibe as imagens
    #  cv2.imshow('Imagem Colorida Redimensionada', img_resized)
    #  cv2.imshow('Imagem Cinza Redimensionada', imgGray)

    # Verifica se a tecla 'q' foi pressionada para encerrar
    #  if cv2.waitKey(1) & 0xFF == ord('q'):
    #      break

    # Libera a câmera e fecha as janelas
    #camera.release()
    #cv2.destroyAllWindows()
