import cv2

img = cv2.imread('Shapes.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('img', img)

for contour in contours:
    #aproximation for all contours # True means every shapes are closed
    aprox = cv2.approxPolyDP(contour , 0.01*cv2.arcLength(contour, True), True)
    #0 to get the maximum distance between the contours and the shapes
    cv2.drawContours(img, [aprox], 0,(0,0,0), 2)
    # To locate the text
    x = aprox.ravel()[0]
    y = aprox.ravel()[1]
    if len(aprox) == 3 :
        print(aprox)
        cv2.putText(img, 'Triangle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(aprox) == 4 :
        x1, y1, w , h = cv2.boundingRect(aprox)
        aspectRatio = float(w)/h
        
        if aspectRatio >= 0.95 and aspectRatio <= 1.05 :
            cv2.putText(img, 'Square', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else : 
            cv2.putText(img, 'Rectangle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(aprox) == 5 :
        cv2.putText(img, 'Pentagon', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(aprox) == 10 :
        cv2.putText(img, 'Star', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif  len(aprox) == 6 :
        cv2.putText(img, 'Hexagonal', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    else :
         cv2.putText(img, 'Circle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
         
         
         
cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()         
        
        
        
    
    