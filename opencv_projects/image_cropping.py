import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found. Make sure sample.jpg exists.")
else:
    cropped = image[50:250, 50:250]
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
