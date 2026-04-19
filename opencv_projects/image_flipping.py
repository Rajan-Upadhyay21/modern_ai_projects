import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found. Make sure sample.jpg exists.")
else:
    horizontal = cv2.flip(image, 1)
    vertical = cv2.flip(image, 0)

    cv2.imshow("Horizontal Flip", horizontal)
    cv2.imshow("Vertical Flip", vertical)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
