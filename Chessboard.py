import cv2 as cv
import numpy as np
#Color code for Dark Brown Color in (b,g,r) format.
(x,y,z)=(74,139,184)
#Color code for Light Brown Color in (b,g,r) format.
(p,q,r)=(111,193,227)
# Create a blank image of 640x640 dimension and with 3 rgb color format
blank=np.zeros((640,640,3),dtype='uint8')
i=0
# i-->Row
# j--> Column
while True:
    if(i>7):
        break
    else:   
        for j in [1,2,3,4,5,6,7,8]:
# For odd no. of columns 
            if(i%2==0):
                if(j%2!=0):
                    blank[((j-1)*80):(j*80),(i*80):((i+1)*80)]=(x,y,z)
                if(j%2==0):
                    blank[((j-1)*80):(j*80),(i*80):((i+1)*80)]=(p,q,r)
# For even no. of columns
            else:
                if(j%2!=0):
                    blank[((j-1)*80):(j*80),(i*80):((i+1)*80)]=(p,q,r)
                if(j%2==0):
                    blank[((j-1)*80):(j*80),(i*80):((i+1)*80)]=(x,y,z)
# Increment i by value of 1                    
    i+=1
# Display image with the titlebar name as Chess
cv.imshow('Chess',blank)
# Wait for any press of the keyboard
cv.waitKey(0)
