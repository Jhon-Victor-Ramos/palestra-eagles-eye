import cv2

cv2.namedWindow("Imagem cinza", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Imagem cinza", 600, 600)

img_cinza = cv2.imread("./images/foto_carro.jpg")

img_cinza = cv2.cvtColor(img_cinza, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem cinza", img_cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()