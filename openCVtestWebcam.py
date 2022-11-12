import cv2
import os
# define a video capture object
vid = cv2.VideoCapture(0)
"""
width = 1920
height = 1080

gst_str = ('nvarguscamerasrc ! ' + 'video/x-raw(memory:NVMM), ' +
          'width=(int)1920, height=(int)1080, ' +
          'format=(string)NV12, framerate=(fraction)30/1 ! ' + 
          'nvvidconv flip-method=2 ! ' + 
          'video/x-raw, width=(int){}, height=(int){}, ' + 
          'format=(string)BGRx ! ' +
          'videoconvert ! appsink').format(width, height)

vid = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER) 

"""
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


