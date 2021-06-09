import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print('width',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('height',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('fps',cap.get(cv2.CAP_PROP_FPS))

while cap.isOpened():
    ret,img = cap.read()

    if ret:
        cv2.imshow('video capture',img)

        key = cv2.waitKey(0)
        if key == 27:
            break

cap.release()   #cap 연결 닫기
cv2.destroyAllWindows()  #cv2 열려진 화면 닫기