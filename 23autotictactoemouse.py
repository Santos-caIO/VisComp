import cv2
import numpy as np

#Desenhando jogo na folha
folha = np.empty([400,400,3],dtype=np.uint8)
folha.fill(255)
cv2.line(folha,(150,50),(150,350),(0,0,0),4)
cv2.line(folha,(250,50),(250,350),(0,0,0),4)
cv2.line(folha,(50,150),(350,150),(0,0,0),4)
cv2.line(folha,(50,250),(350,250),(0,0,0),4)

#Criando o X
X = np.empty([50,50,3], dtype=np.uint8)
X.fill(255)
cv2.line(X,(0,0),(50,50),(0,0,0),3)
cv2.line(X,(0,50),(50,0),(0,0,0),3)

vezX = True
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

cv2.imshow('Jogo da velha', folha)

def verifyWinner():
    for l in range(0,3):
        c=1
        if(matriz[l][c-1] == matriz[l][c] and matriz[l][c] == matriz[l][c+1] and matriz[l][c]!=0):
            return True
    for c in range(0,3):
        l=1
        if(matriz[l-1][c] == matriz[l][c] and matriz[l][c] == matriz[l+1][c] and matriz[l][c]!=0):
            return True
    if(matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2] and matriz[1][1]!=0):
        return True
    if (matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[1][1]!=0):
        return True

def click_event(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        global vezX
        if(x<150 ):
            x=100
        elif (x > 150 and x < 250):
            x = 200
        else:
            x = 300

        if (y < 150):
            y = 100
        elif (y > 150 and y < 250):
            y = 200
        else:
            y = 300

        if( vezX == True):
            centrox = int(x/100 - 1)
            centroy = int(y/100 - 1)
            folha[y-25:y+25, x-25:x+25] = X
            matriz[centrox][centroy] = 1
            vezX = False
        elif( vezX == False):
            centrox = int(x/100 - 1)
            centroy = int(y/100 - 1)
            cv2.circle(folha, (x,y),25,(0,0,0), 3)
            matriz[centrox][centroy] = 2
            vezX = True

        cv2.imshow('Jogo da velha', folha)

        if ( verifyWinner() ):
            if (vezX == False):
                print("O jogador que estava marcando o X ganhou.")
                simbolo = "xis"

            if (vezX == True):
                print("O jogador que estava marcando círculo ganhou")
                simbolo = "circulo"

            cv2.putText(folha, "O jogador que estava marcando ",(0, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7,(0,0,0))
            cv2.putText(folha, simbolo + " ganhou.", (0, 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0))
            cv2.imshow('Jogo da velha', folha)
            cv2.waitKey()
            cv2.destroyAllWindows()

cv2.setMouseCallback('Jogo da velha', click_event)
cv2.waitKey()
cv2.destroyAllWindows()