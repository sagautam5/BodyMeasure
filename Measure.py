import numpy as np
import cv2
'''
All Measurement are in pixel of an two dimensional 
image in RGB color space which is converted to Gray 
Scale and then face is detected after that using 
Golden ratio(1.618) other parts are measured
'''
golden_ratio = 1.61803399

shoulder_left = []
shoulder_right = []
shoulder_width = 0

face_top = []
face_but = []
face_height = 0
face_width = 0

head_top = []
head_but = []
head_height = 0
head_width = 0

waist_left = []
waist_right = []
waist_width = 0
waist_joint = []

head_top = []
head_but = []
head_height = 0
head_width = 0

neck_joint = []
neck_width = 0
neck_left = []
neck_right = []

height = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
shoulder_cascade = cv2.CascadeClassifier('HS.xml')

Image = cv2.imread('wrestler.jpg')
gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
shoulders = shoulder_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in faces:
	cv2.rectangle(Image,(x,y),(x+w,y+h),(0,0,255),1)
	face_top.append(x+w/2)
	face_top.append(y)
	face_but.append(x+w/2)
	face_but.append(y+h)
	face_height = h
	face_width = w
	head_but.append(x+w/2)
	head_but.append(y+h)

for(x,y,w,h) in shoulders:
	cv2.rectangle(Image,(x,y),(x+w,y+h),(0,255,0),1)
	shoulder_left.append(x)
	shoulder_left.append(y+h)
	shoulder_right.append(x+w)
	shoulder_right.append(y+h)
	head_top.append(x+w/2)
	head_top.append(y)

shoulder_width = shoulder_right[0]-shoulder_left[0]
height = (int)(shoulder_width*4)

head_height = head_but[1]-head_top[1]
head_width = (int)(head_height* golden_ratio)

waist_x = (head_top[0])
waist_y = head_top[1]+(int)(height*0.618/1.618)
waist_joint.append(waist_x)
waist_joint.append(waist_y)
waist_width =(int)(shoulder_width / golden_ratio)

neck_x = (head_top[0]+shoulder_left[0]+shoulder_right[0])/3
neck_y = (head_top[1]+shoulder_left[1]+shoulder_right[1])/3

neck_joint.append(neck_x)
neck_joint.append(neck_y)
neck_width = waist_width/2
neck_left.append(neck_joint[0]-neck_width/2)
neck_left.append(neck_joint[1])
neck_right.append(neck_joint[0]+neck_width/2)
neck_right.append(neck_joint[1])

waist_left.append(waist_joint[0]-waist_width/2)
waist_left.append(waist_joint[1])
waist_right.append(waist_joint[0]+waist_width/2)
waist_right.append(waist_joint[1])

print 'All Measurements are in pixels'
print 'Left Shoulder : '+ str(shoulder_right)
print 'Right Shoulder : '+ str(shoulder_left)
print 'Shoulde Size : '+str(shoulder_width)
print 'Face Top : '+str(face_top)
print 'Face Buttom : '+str(face_but)
print 'Face Height : '+str(face_height)
print 'Face Width : '+str(face_width)
print 'Head Top : '+str(head_top)
print 'Head Buttom : '+str(head_but)
print 'Head Height : '+str(head_height)
print 'Head width : '+str(head_width)
print 'Height : '+str(height)
print 'Waist width : '+str(waist_width)
print 'Neck Joint : '+str(neck_joint)
print 'Neck Width : '+str(neck_width)
print 'Neck Left : '+str(neck_left)
print 'Neck Right : '+str(neck_right)
# Draw Lines over width of body parts in image

cv2.rectangle(Image,(neck_left[0],neck_left[1]),(neck_right[0],neck_right[1]),(255,255,0),3)
cv2.rectangle(Image,(shoulder_left[0],shoulder_left[1]),(shoulder_right[0],shoulder_right[1]),(0,255,255),3)
cv2.rectangle(Image,(waist_left[0],waist_left[1]),(waist_right[0],waist_right[1]),(0,0,0),3)

cv2.imwrite('Result.jpg',Image)
cv2.imshow('Result',Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
