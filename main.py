import cv2
import numpy as np


# пример работы с картинкой
# img = cv2.imread(r'C:\Users\sony4\Desktop\pp.jpg')

cap = cv2.VideoCapture('video/2022-04-17 11-15-58.mp4')

while True:
    success, new_img = cap.read()

    new_img = cv2.GaussianBlur(new_img, (9, 9), 0)

    new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    new_img = cv2.Canny(new_img, 200, 200)
    kernel = np.ones((5, 5), np.uint8)
    new_img = cv2.dilate(new_img, kernel, iterations=1)
    new_img = cv2.erode(new_img, kernel, iterations=1)
    cv2.imshow('Result',new_img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
         break

# new_img = cv2.resize(img,(2000,2000))
# new_img = cv2.resize(img,(img.shape[1]//2,img.shape[1]//2))
# # размытие Знаение - 3 - только нечетные
# new_img = cv2.GaussianBlur(new_img,(9,9),0)
# new_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
#
# new_img = cv2.Canny(new_img,200,200)
# kernel = np.ones((5,5),np.uint8)
# new_img = cv2.dilate(new_img,kernel,iterations=1)
#
# new_img =cv2.erode(new_img,kernel,iterations=1)

# cv2.imshow('1',img)
# cv2.imshow('1',new_img)


# print(img.shape)
# cv2.waitKey()


# # пример работы с видео
# # cap = cv2.VideoCapture('video/2022-04-17 11-15-58.mp4')
#
# cap = cv2.VideoCapture(0)
# # cap = cv2.VideoCapture(1)
#
# cap.set(3,500)
# cap.set(4,300)
#
#
# # 0  и  1  выбираем камеры
#
# while True:
#      success, img = cap.read()
#      cv2.imshow('Result',img)
#
#      if cv2.waitKey(1) & 0xFF ==ord('q'):
#          break