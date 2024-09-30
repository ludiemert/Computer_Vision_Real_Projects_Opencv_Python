import cv2

# Abrir a webcam
camera = cv2.VideoCapture(0)

# Carregar o classificador de olhos
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_eye.xml')

while True:
    check, img = camera.read()  # Captura o frame da câmera

    # Se não for possível capturar a imagem da câmera
    if not check:
        print("Não foi possível capturar a imagem da câmera...")
        break

    # Redimensiona a imagem capturada
    img_resized_color = cv2.resize(img, (300, 300))  # Reduz a imagem colorida
    img_resized = cv2.resize(img, (300, 300))        # Outra redução de tamanho

    # Converte a imagem para escala de cinza
    imgGray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)


    #aplicar o classificador na img_cinza
    #variavel, ela detecta obj dentro da img e retornar as coordenadas de onde esse ob esta
    objetos = classificador.detectMultiScale(imgGray)
    print(objetos) #os numeros sao coordenadas em formato de px [[164 171  26  26]]
    #que eh a estrutura da img



    # Exibe as imagens
    cv2.imshow('Imagem Colorida Redimensionada', img_resized_color)
    #cv2.imshow('Imagem Cinza Redimensionada', imgGray)

    # Verifica se a tecla 'q' foi pressionada para encerrar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
camera.release()
cv2.destroyAllWindows()
