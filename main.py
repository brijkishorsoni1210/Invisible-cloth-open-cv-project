import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened(): #getting the background image
    ret,background=cap.read()
    if ret:
        cv2.imshow("image",background)
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite("image.jpg",background) #save the background
            break
cap.release()
cv2.destroyAllWindows()

