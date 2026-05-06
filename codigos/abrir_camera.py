import cv2

cv2.namedWindow("Vídeo colorido", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vídeo colorido", 600, 600)

camera = cv2.VideoCapture(0)
fps_desejado = 20
delay = int(1000 / fps_desejado)

print("Câmera ligada! Pressione 'f' para fechar a janela!")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Vídeo colorido", frame)

    if cv2.waitKey(delay) & 0xFF == ord('f'):
        break

camera.release()
cv2.destroyAllWindows()