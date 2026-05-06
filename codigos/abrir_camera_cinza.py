import cv2


cv2.namedWindow("Vídeo suave - Gauss", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vídeo suave - Gauss", 600, 600)
cv2.namedWindow("Vídeo cinza", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vídeo cinza", 600, 600)
cv2.namedWindow("Vídeo colorido", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Vídeo colorido", 600, 600)


camera = cv2.VideoCapture(0)
fps_desejado = 20
delay = int(1000 / fps_desejado)

print("Câmera ligada! Pressione a tecla 'f' na janela do vídeo para fechar.")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(gray, (7, 7), 0)

    cv2.imshow("Vídeo colorido", frame)
    cv2.imshow("Vídeo cinza", gray)
    cv2.imshow("Vídeo suave - Gauss", suave)


    if cv2.waitKey(delay) & 0xFF == ord('f'):
        break

camera.release()
cv2.destroyAllWindows()