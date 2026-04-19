import cv2

cap = cv2.VideoCapture(0)
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mask = background_subtractor.apply(frame)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Foreground Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
