import cv2
def picture():
    object=cv2.VideoCapture(0)
    result=True
    while(result):
        name,value=object.read()
        cv2.imwrite("picture.png",value)
        result=False
    object.release()
picture()