import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import functions as use
import time

#Prompt the user for the name of a color image and template files

#Enter the following for waldo:
#   waldo_image.jpeg
#   waldo_template.png

#Enter the following for the real life application
#   street.jpg
#   stop_sign.png

while True:
    colorImg = input("Enter file name of colored img")
    template = input("Enter file name of template")
    try:
        colored = mpimg.imread(colorImg)
        img = mpimg.imread(colorImg)
        template = mpimg.imread(template)
    except:
        print("File not found, try again")
    else:
        break

#Check data type and range and convert if not correct

#Convert to uint8
if img.dtype != "uint8":
    img = use.toUint8(img)
    colored = use.toUint8(img)

if template.dtype != "uint8":
    template = use.toUint8(template)

#Convert to correct range if not
if not use.isInRange(img):
    img = use.imgMap(img, 0.0,1.0,0,255)

if not use.isInRange(template):
    img = use.imgMap(template, 0.0,1.0,0,255)

#Convert to grayscale
img = use.toGrey(img)
template = use.toGrey(template)

#Promt the user for the type of template matching method
while True:
    print("SSD: Sum of Squared Differences")
    print("CC: Correlation Coefficient")
    print("NCC: Normalized Cross-Correlation")
    method = input("What method do you want to use? (SSD,CC,NCC)")

    if method.upper()=="SSD":
        chosenMethod = "Sum of Squared Differences"
        start = time.time()
        x,y = use.SSD(img,template)
        end = time.time()
        break
    elif method.upper()=="CC":
        chosenMethod = "Correlation Coefficient"
        start = time.time()
        x,y = use.CC(img,template)
        end = time.time()
        break
    elif method.upper()=="NCC":
        chosenMethod = "Normalized Cross-Correlation"
        start = time.time()
        x,y = use.NCC(img,template)
        end = time.time()
        break
    else:
        "Wrong input, enter again"


#Location to crop detected image
x1,y1 = x-5,y-5
x2 = x1+template.shape[1]+5
y2 = y1+template.shape[0]+5
cropped = colored[y1:y2,x1:x2]


#SHOW INFO
info1 = "Chosen method: "+chosenMethod
execTime = end - start
info2 = "Execution time: " + str(execTime) + " seconds"
info3 = "Location of image: X: " + str(x) +", Y: " + str(y)
info = info1+"\n"+info2+"\n"+info3


#SHOW original image with a bounding box highlighting the template
#SHOW a cropped image of detected image with bounding box
fig = plt.figure()
ax2 = fig.add_subplot(2,2,1)
#Bounding box on image
ax2.imshow(colored)
rect = patches.Rectangle((x, y), template.shape[1], template.shape[0], linewidth=1, edgecolor='r', facecolor='none')
ax2.add_patch(rect)
ax2.set_title("Bounding box")
#Cropped image
ax3 = fig.add_subplot(2,2,2)
ax3.imshow(cropped)
rect2 = patches.Rectangle((5, 5), cropped.shape[1]-10, cropped.shape[0]-10, linewidth=1, edgecolor='r', facecolor='none')
ax3.add_patch(rect2)
ax3.set_title("Cropped")
ax4 = fig.add_subplot(2,2,3)
#show information and removing border and axes for clear viewing
ax4.axis([0,10,0,10])
ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['bottom'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.text(2, 6, info , fontsize=15)
plt.show()





