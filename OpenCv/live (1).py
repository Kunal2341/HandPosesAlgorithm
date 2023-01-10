import cv2
import time
cap = cv2.VideoCapture(0)
pTime = 0
while(True):
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# Destroy all the windows
cv2.destroyAllWindows()