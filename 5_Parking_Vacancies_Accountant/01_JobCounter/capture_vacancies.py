import cv2

#salva inf em um arquivo externo
import pickle #extensao .pkl

#abrir img
img = cv2.imread('estacionamento.png')

#variavel p salvar a inf  do array
vacancies = []


#criar um loop que vamos percorrer 69x(tem 69 vagas)
for x in  range(69):
    vacancy = cv2.selectROI('vacancies',img,False) #selecionar a img que corresponde a vaga e ir salvando em uma variavel
    cv2.destroyWindow('vacancies')#fechar a janela vacancies
    vacancies.append(vacancy) #salva nessa variavel

    #fazer um retangulo cada vez que gravarmos uma vaga(extrair as informaoes)
    for x,y,w,h in vacancies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


#cria um arquivo para salvar o array depois que selecionar todas a img, apos 69 vezes ele cria um archive vacancies(arquivo vagas)
#fazendo isso nao precisa fazer isso toda vez que iniciar o codigo
with open('vacancies.pkl','wb') as archive:   #escrever dentro do arquivo eh wb, estamos criando o wb e salvando dentro da variavel wb
    pickle.dump(vacancies,archive) # oque vamos salvar qual variavel (vacancies = vagas) e onde vamos archive(arquivo)