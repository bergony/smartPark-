import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

print(cap.get(3))
print(cap.get(4))

cap.set(3, 1600)
cap.set(4, 800)

vaga1 = False
vaga2 = False
vaga3 = False
vaga4 = False
vaga5 = False
vaga6 = False

print(cap.get(3))
print(cap.get(4))


while True:

    vaga1 = False
    vaga2 = False
    vaga3 = False
    vaga4 = False
    vaga5 = False
    vaga6 = False

    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    count = 0
    for obj in decodedObjects:
        count = count+1
        (x, y, w, h) = obj.rect
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

	barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type

        if x < 300 and y < 200:
            vaga1 = True
        elif x < 300 and y > 200:
            vaga4 = True
        elif x > 600 and y < 200:
            vaga3 = True
        elif x < 300 and y > 200:
            vaga4 = True
        elif (x > 300 and x < 600) and y < 200:
            vaga2 = True
        elif (x > 300 and x < 600) and y > 200:
            vaga5 = True
        elif x > 600 and  y > 200:
            vaga6 = True

        text = "{} ({})".format("Livre", barcodeType)
        cv2.putText(frame, text, (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#        print(barcodeData, count ," ", "x= ",x ," Y=",y, "W", w , "h", h)

    if vaga1 == True:
        print("Vaga1 livre")
    if vaga2 == True:
        print("Vaga2 livre")
    if vaga3 == True:
        print("Vaga3 livre")
    if vaga4 == True:
        print("Vaga4 livre")
    if vaga5 == True:
        print("Vaga5 livre")
    if vaga6 == True:
        print("Vaga6 livre")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
