import cv2

cv2.namedWindow("Filtro Canny aplicado", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Filtro Canny aplicado", 600, 600)

camera = cv2.VideoCapture(0)
fps_desejado = 20
delay = int(1000 / fps_desejado)

print("Câmera ligada! Pressione a tecla 'f' na janela do vídeo para fechar.")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    suave = cv2.GaussianBlur(gray, (5, 5), 0)

    bordas = cv2.Canny(suave, 50, 150)

    cv2.imshow("Filtro Canny aplicado", bordas)

    if cv2.waitKey(delay) & 0xFF == ord('f'):
        break

camera.release()
cv2.destroyAllWindows()