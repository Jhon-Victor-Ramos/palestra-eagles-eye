import cv2

cv2.namedWindow("Rastreamento de Alvos", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rastreamento de Alvos", 600, 600)

camera = cv2.VideoCapture(0)

subtrator = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=False)

print("Rastreamento ativado! Pressione 'f' para fechar.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    mascara = subtrator.apply(frame)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_DILATE, kernel, iterations=2)

    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) > 3000:
            x, y, w, h = cv2.boundingRect(contorno)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "ALVO EM MOVIMENTO", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Mascara aplicada para detectar objetos em movimento", mascara)
    # cv2.imshow("Rastreamento de Alvos", frame)

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

camera.release()
cv2.destroyAllWindows()


