import cv2
import numpy as np
#rasm matn va ashkal hendesi bar rooye tasvir:
pic = cv2.imread('image1.jpg')

#KHAT 
# cv2.line(Aks, (Noghte Shoru, Noghte Shoru), (Noghte Payan, Noghte Payan), Rang be surat BGR, Zekhamat)
cv2.line(pic, (0, 0), (200, 200), (255, 0, 0), 5)
cv2.imshow('image', pic)

#MOSTATLIL 
# cv2.rectangle(Name Aks, (Noghte Shoru, Noghte Shoru), (Noghte Payan, Noghte Payan), Rang be surat BGR, Zekhamat)
pic = cv2.rectangle(pic, (100, 50), (300, 200), (0, 255, 0), 3)
cv2.imshow('img', pic)

#DAYERE 
# cv2.circle(Esme Aks, (Markaz, Markaz), Sho'Ae, Rang, (dastoor -1, dayere ra too por mikonad))
pic = cv2.circle(pic, (280, 280), 50, (0, 0, 255))
cv2.imshow('pic', pic)

#BEYZI 
# cv2.ellipse(Esm, (Markaz, Markaz), (tool mehvar bozorg, tool mehvar kuchek), Zavie ba mehvar asli, zavie shoru kaman, zavie entehaye kaman)
pic = cv2.ellipse(pic, (100, 240), (80, 30), 0, 0, 360, (255, 0, 0), -1)
cv2.imshow('picture', pic)

#CHAND_VAJHI 
# cv2.polylines
pts = np.array([[10, 5], [20, 30], [20, 20], [50, 10]])
pic = cv2.polylines(pic, [pts], False, (0, 0, 0),)
cv2.imshow('imag', pic)

#Matn
# cv2.putText(Aks, 'Name Aks', (Makan neveshte, Makan neveshte), font(ye font tarif shode), size font, rang matn, zekhamat)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(pic, 'open cv', (10, 100), font, 2, (255, 0, 0), 2)
cv2.imshow('pic', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()