import cv2

cv2.namedWindow("Imagem colorida", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Imagem colorida", 500, 500)

img = cv2.imread("./images/foto_carro.jpg")

cv2.imshow("Imagem colorida", img)

print("Pressione qualquer tecla para fechar!")

cv2.waitKey(0)
cv2.destroyAllWindows()