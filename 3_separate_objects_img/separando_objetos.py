import cv2

# Carregar a imagem
img = cv2.imread('objetos.jpg')
img = cv2.resize(img, (400, 500))  # Diminuir a resolução

# Converter para escala de cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Suavização para reduzir ruídos
imgBlur = cv2.GaussianBlur(imgCinza, (5, 5), 0)

# Detectar contornos usando Canny
imgCanny = cv2.Canny(imgBlur, 50, 150)  # Ajuste os valores de limiar conforme necessário

# Aplicar a morfologia para melhorar o fechamento dos contornos
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (5, 5))  # Ajustar o tamanho do kernel

# Encontrar contornos
contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Verificar se encontrou contornos
if len(contours) > 0:
    print(f"Encontrados {len(contours)} objetos.")

    numOb = 1  # Inicializar o número do objeto

    # Loop sobre os contornos
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Filtrar por área
        if area > 500:  # Ajuste o valor conforme o tamanho esperado dos objetos
            x, y, w, h = cv2.boundingRect(cnt)

            # Recortar a área do objeto
            objeto = img[y:y+h, x:x+w]

            # Salvar a imagem do objeto separadamente
            cv2.imwrite(f'C:/Users/user/Downloads/3_separar_objetos_img/objetos/objeto-{numOb}.jpg', objeto)

            # Desenhar o retângulo na imagem original
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

            numOb += 1  # Incrementar o número do objeto

# Exibir as imagens
cv2.imshow('Imagem Original com Contornos', img)
cv2.imshow('Imagem em Escala de Cinza', imgCinza)
cv2.imshow('Imagem com Canny (Contornos)', imgCanny)

# Esperar até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()
