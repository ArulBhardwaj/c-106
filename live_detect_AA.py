import cv2

face_fascade=cv2.CascadesClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadesClassifier('C:Users/arubha/Local/Programs/Python39/Lib/site-packages/cv2/data/haarcascade_eye.xml')

vid=cv2.VideoCapture(0)

while(True):

    ret,frame=vid.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GGRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5)

    eyes=eye_cascade.detectMultiScale(gray,1.1,5)

    