import cv2

cap = cv2.VideoCapture(0)
#設定畫面長寬
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

end=0
while(1):
    ret,frame = cap.read()
    #cv2.resizeWindow('cature',800,600)
    #show
    cv2.imshow('cature',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    else:
       end=end+1
       cv2.imwrite("./image/"+str(end)+'.jpeg',frame)
        
cap.release()
cv2.destroyAllWindows()