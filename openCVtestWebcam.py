import cv2
import os
# define a video capture object
#vid = cv2.VideoCapture(0)

print(os.path.exists(os.path.join(os.path.dirname(os.getcwd()), "random_images")))

#print(vid)
"""
while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    print(frame)
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
cv2.destroyAllWindows()"""


