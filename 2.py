import cv2

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,600)
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()