import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)
useCamera = True

while True:

    if useCamera:
        _, img = cap.read()

    # Change output from bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Use specific hsv range
    mask = cv2.inRange(hsv,(54, 124, 64), (104, 255, 200) )
    
    
   # find the contours
    le_contour = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    le_contour = imutils.grab_contours(le_contour)
    
    # Approximate and draw contours
    for cnt in le_contour:
        
        # calculate the area of the contour
        area = cv2.contourArea(cnt)
        
        x,y,w,h = cv2.boundingRect(cnt)
        
        # only draw the contour if it's area is greater than x
        if area > 100:
        
            #Approximate size of contour
            epsilon = 0.01*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            
            # Add text to show off
            cv2.putText(img,"Green",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,225)
            
            #Draw contour
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        
        
        
    # Display specific output
    cv2.imshow('img',img)

    # Stop when you press "Q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Removes the open window once you break out of the while loop
cap.release()
cv2.destroyAllWindows()