import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import csv
from datetime import datetime
import winsound
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)  
cap.set(4, 480)  

detector = FaceMeshDetector(maxFaces=1)

breakcount_s = 0
counter_s = 0
state_s = False

def alert(img):
    cv2.rectangle(img, (360, 20), (590, 80), (0, 0, 0), cv2.FILLED)  
    cv2.putText(img, "DIKKAT!!!", (380, 60),  
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
    color = (0, 0, 255)
    intensity = int(128 * (1 + 0.5 * (1 - abs(time.time() * 2 % 2 - 1))))
    color = (intensity, 0, 0)
    winsound.Beep(1000, 1000)

def recordData(condition):
    file = open("database.csv", "a", newline="")
    now = datetime.now()
    dtString = now.strftime("%d-%m-%Y %H:%M:%S")
    writer = csv.writer(file)
    writer.writerow([dtString, condition])
    file.close()

while True:
    success, img = cap.read()

    img = cv2.flip(img, 1)

    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        eyeLeft = [27, 23, 130, 243]
        eyeRight = [257, 253, 463, 359]
        faceId = [27, 23, 130, 243, 257, 253, 463, 359]

        eyeLeft_ver, _ = detector.findDistance(face[eyeLeft[0]], face[eyeLeft[1]])
        eyeLeft_hor, _ = detector.findDistance(face[eyeLeft[2]], face[eyeLeft[3]])
        eyeLeft_ratio = int((eyeLeft_ver/eyeLeft_hor)*100)

        eyeRight_ver, _ = detector.findDistance(face[eyeRight[0]], face[eyeRight[1]])
        eyeRight_hor, _ = detector.findDistance(face[eyeRight[2]], face[eyeRight[3]])
        eyeRight_ratio = int((eyeRight_ver / eyeRight_hor) * 100)

        cv2.rectangle(img, (30,20), (200,90), (255,255,255), cv2.FILLED)  
        cv2.putText(img, f'Sol Goz Ratio: {eyeLeft_ratio}', (30, 50),
            cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 1)
        cv2.putText(img, f'Sag Goz Ratio: {eyeRight_ratio}', (30, 80),
            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)


        cv2.putText(img, f'UYUKLAMA: {counter_s}', (370, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

        #------------------------Eye-----------------------------
        if eyeLeft_ratio <= 50 and eyeRight_ratio <= 50:
            breakcount_s += 1
            if breakcount_s >= 30:
                alert(img)
                if not state_s:
                    counter_s += 1
                    recordData("Sleep")
                    state_s = not state_s
        else:
            breakcount_s = 0
            if state_s:
                state_s = not state_s

        for id in faceId:
            cv2.circle(img, face[id], 3, (0,0,255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27: 
        break

cap.release()
cv2.destroyAllWindows()
