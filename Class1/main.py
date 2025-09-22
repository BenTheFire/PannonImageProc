import cv2

img = cv2.imread('cat.png')

cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cat2.png', img)

for i in range(5):
    cv2.imshow(winname=f'Cat {i}', mat=img)

cv2.waitKey(0)
cv2.destroyAllWindows()
