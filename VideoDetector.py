import cv2
import numpy as np 
import dlib
import imutils
import datetime

x = datetime.datetime.now()


# global var
x1 = int()
y1=int()
x2=int()
y2=int()
############
cap= cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#視頻編碼
fourcc = cv2.VideoWriter_fourcc(*"MPEG")

#存檔
nout = './image/'+str(x.date())+'%'+str(x.hour)
out = cv2.VideoWriter(nout+'.avi',fourcc,fps,size)
#(640,480)

# Dlib 人臉辨識
detector = dlib.get_frontal_face_detector()

while cap.isOpened():
    #開偵
    ret,frame =cap.read()
    
    #取時間
    x = str(datetime.datetime.now())
    
    #detect faceRequired 
    face_rects,scores,idx = detector.run(frame,0)
   
    #取出結果
    for i , d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        
    #用方框表示人臉 (框,座標,座標,顏色,粗度)
    cv2.rectangle(frame,(x1, y1), (x2, y2), (0, 255, 0), 4)
    
    #文字(框,文字變數,座標,字體,大小,顏色,粗度)
    cv2.putText(frame,x,(10,90),cv2.FONT_HERSHEY_DUPLEX,
                0.7,(255,0,0),0)
    
    if ret ==True:
        #frame = cv2.flip(frame,1) #翻轉frame
        
        #write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #按q退出
            break
    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()