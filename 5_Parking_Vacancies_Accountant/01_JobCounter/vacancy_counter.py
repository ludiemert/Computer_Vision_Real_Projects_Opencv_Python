from distutils.command.check import check

import  cv2

#recuperar as inf que gravou no arquivo
import pickle

import numpy as np  #usar o kernel da biblioteca  numpy
from numpy.ma import count

#variavel vacancies array vazio
vacancies = []

#ler e abrir o arquivo salvo
with open('vacancies.pkl','rb') as archive: #rb => ler
    vacancies = pickle.load(archive)#carregar o arquivo (archive)

#verificar as coordenadas
print(vacancies)

#carrega  o video
video = cv2.VideoCapture('video.mp4')

while True:
    check,img = video.read()
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)    #thereshold adaptativo
    imgMedian = cv2.medianBlur(imgTh,5)   # Tirar mais ruídos da img (ficar mais limpa)

    kernel = np.ones((3,3),np.int8)  #3 linhas por 3 colunas
    imgDil = cv2.dilate(imgMedian,kernel)   #expandir mais os pixels, morfologia  da dilatacao, usar o kernel da biblioteca  (numpy import numpy as np)

#Criar uma contagem de quantas vagas disponíveis tem
    vacanciesOpen =  0 #variavel q recebe o valor de 0

#verificar se as coordenadas funcionara
    for x,y,w,h in vacancies:
        vacancy = imgDil[y:y+h,x:x+w]    #medir a intensidade de cada vaga - e recortar a img - aquela area - variavel
        count = cv2.countNonZero(vacancy) #valores baixos nao tem carros
        cv2.putText(img,str(count),(x,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #contagem dos pixls brancos

        #considerar acima de 900px tem carro abaixo nao tem carro
        if count <900:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  #retangulo verde quando tiver a vaga livre
            vacanciesOpen +=1 #vagas vazias acrescenta +1

        else: #caso contrario
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  #caso contrario retangulo vermelho
        #print(vacanciesOpen) #print variavel

        #colocar a informacao de vaga vazia dentro da img
        cv2.rectangle(img,(90,0),(415,60),(0,255,0),-1) #retangulo preenchido all com verde
        cv2.putText(img,f'FREE: {vacanciesOpen}/69', (95,45),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),5) #text com a ing de qtas vazias

    cv2.imshow('video color',img)
    #cv2.imshow('video TH',imgMedian)
    cv2.imshow('video TH', imgDil)

    cv2.waitKey(10)  #delay de 10ml seg para o video ficar mais lento
