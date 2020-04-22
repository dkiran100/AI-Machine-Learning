# Read a video stream from my web cam (Set of Frames) 
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	if ret == False:
		continue
	
	cv2.imshow("Video Frame", frame)
	
	# wait for the user input - q, then you will stop the loop 
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
