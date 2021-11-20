import cv2
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE )
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if( area > 50):
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            perim = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, 0.02 * perim, True)
            print(len(vertices))
            x, y, w, h = cv2.boundingRect(vertices)

            if len(vertices) == 2:
                Tipo = "Reta"
            elif len(vertices) == 3:
                Tipo = "Triangulo"
            elif len(vertices) == 4:
                Tipo = "Retangulo"
            elif len(vertices) > 4:
                Tipo = "Circulo"
            else:
                Tipo = "Nenhum"

            cv2.putText(imgContour, Tipo, (int(x + (w / 2) - 10), int(y + (h / 2) - 10)), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0))


cap = cv2.VideoCapture("C:/Users/caios/PycharmProjects/pythonOpenCV1/teste2.mp4")

while cap.isOpened():
    (retorno, img) = cap.read() #lista com uma variável de sucesso e com cada frame do video
    img = cv2.resize(img, (480,360)) #redimensiona para acelerar o processamento

    imgCanny = cv2.Canny(img, 50, 50)
    imgContour = img.copy()
    getContours(imgCanny)

    cv2.imshow("formas", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
"""""
img = cv2.imread('formas.png', 1)

canny = cv2.Canny(img, 50, 50)

imgContour = img.copy()
getContours(canny)
cv2.imshow("normal", img)
cv2.imshow("Canny",canny)
cv2.imshow("contornos", imgContour)

cv2.waitKey()
cv2.destroyAllWindows()
"""""