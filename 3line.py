import cv2

img = cv2.imread('lena.png',1)
cv2.imshow('normal',img)

#adicionar uma linha com o comando line
img_line_blue = cv2.line(img, (0,200), (225,200), (255,0,0), 2)
cv2.imshow('line blue',img_line_blue)


img_line_green = cv2.line(img, (50,0), (25,500), (0,255,0), 4)
cv2.imshow('line green',img_line_green)

img_line_red = cv2.line(img, (0,190), (225,190), (0,0,255), 2)
cv2.imshow('line red',img_line_red)

cv2.waitKey()
cv2.destroyAllWindows()