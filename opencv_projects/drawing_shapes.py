import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(canvas, (50, 100), (200, 250), (0, 255, 0), 3)
cv2.circle(canvas, (350, 175), 75, (0, 0, 255), 3)
cv2.putText(canvas, "OpenCV", (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

cv2.imshow("Drawing Shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
