import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found. Make sure sample.jpg exists.")
else:
    print("Image shape:", image.shape)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
