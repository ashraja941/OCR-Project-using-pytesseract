from PIL import Image, ImageGrab, ImageEnhance, ImageOps
import cv2
import pytesseract
import numpy as np
import time
import keyboard
import json
import socket

s=socket.socket()
host = socket.gethostname()
ip=socket.gethostbyname(host)
print(host,"(",ip,")\n")
port = 1234
s.bind((host,port))
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn,addr=s.accept()
print("Received connection from ", addr[0],"(",addr[1],")\n")

boostStorage = {
    "boost" : 100
}

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#initialisations
i=0
boost = '100'

while True:    
    ### Image processsing
    im1 = ImageGrab.grab(bbox=(1638,860,1820,930))
    im1 = im1.resize((220,190))
    img = np.array(im1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    lower = np.array([90,140,90])
    upper = np.array([255,255,255])
    img = cv2.inRange(img,lower,upper)

    pts1 = np.float32([[0,0],[0,190],[190,20],[190,190]])
    pts2 = np.float32([[0,0],[0,190],[190,0],[190,160]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    img = cv2.warpPerspective(img,M,(200,190))
    img = cv2.bitwise_not(img)

    kernel = np.ones((3, 3), np.uint8) 
    dddimg = cv2.erode(img, kernel)
    img = cv2.fastNlMeansDenoising(img,None)
    
    img = cv2.medianBlur(img,1)

    ### OCR
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    txt = pytesseract.image_to_string(img,lang = "rl",config=custom_config)

    ### manage boost
    newBoost = ''.join(filter(lambda x: x.isdigit(), txt))
    if boost != newBoost:
        boost = newBoost
        if not boost == '' and int(boost) <= 100:
            print(boost)
            conn.send(boost.encode())
    
    ### quit program
    if keyboard.is_pressed('q'):
        print("Program quit")
        break

    time.sleep(0.1)
    i+=1
    if i == 6000:
        break

    
