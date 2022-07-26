import cv2
from datetime import datetime

def record():
    cap = cv2.VideoCapture(0) # for webcam

    fourcc = cv2.VideoWriter_fourcc(*'XVID') # a four char string converted into interger form,( xvid to compress the video without loosing quality 
    out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc,20.0,(640,480)) # how the video is stored (path ,the storage format) 

    while True:
        _, frame = cap.read() #first frame captured

        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255,255,255), 2) # to show the date and time onscreen , font for displaying them

        out.write(frame) 
        

        cv2.imshow("esc. to stop", frame) #click esc 

        if cv2.waitKey(1) == 27: # value of esc
            cap.release()
            cv2.destroyAllWindows()
            break 
