import cv2

img = cv2.imread('Defcon_Sticker.png')
mask = cv2.imread('mask.png',0)
res = cv2.bitwise_and(img,img,mask = mask)
print(img.shape)
print(mask.shape)
cv2.imshow("masked", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()