import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

#Function to convert image to uint8
def toUint8(img):
    img = (img * 255).round().astype(np.uint8)
    return img

#Function to change the range of image
def imgMap(image, from_min, from_max, to_min, to_max):
    # map values from [from_min, from_max] to [to_min, to_max]
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled = np.array((image - from_min) / float(from_range), dtype=float)
    return to_min + (scaled * to_range)

#Function to check if image is in the correct range
def isInRange(img):
    for i in range(2,255):
        if i in img:
            return True
    return False

#Function to convert image to greyscale
def toGrey(img):
    rgb_weights = [0.2989, 0.5870, 0.1140]
    img = np.dot(img[...,:3], rgb_weights)
    return img

#Sum of Squared Differences
def SSD(img,template):
    x,y=0,0
    bingo=100000000000000000
    #For loop moving 3 pixels right and bottom until done
    for i in range(template.shape[0],img.shape[0],4):
        x=0
        for j in range(template.shape[1],img.shape[1],4):
            R = calculate_ssd(template,img[y:i,x:j])
            print(R)
            if R < bingo:
                bingo = R
                x_img = x
                y_img = y
            x+=4
        y+=4

    return x_img,y_img

def calculate_ssd(img1, img2):
    if img1.shape != img2.shape:
        print("Images don't have the same shape.")
        return
    return np.sum((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32))**2)
    
#Correlation Coefficient method
def CC(img,template):
    x,y=0,0
    bingo=0
    #For loop moving 3 pixels right and bottom until done
    for i in range(template.shape[0],img.shape[0],4):
        x=0
        for j in range(template.shape[1],img.shape[1],4):
            T = np.array(template, dtype=np.float32) - np.sum(np.array(template, dtype=np.float32)/(template.shape[0]*template.shape[1]))
            L = np.array(img[y:i,x:j], dtype=np.float32) - np.sum(np.array(img[y:i,x:j], dtype=np.float32)/(template.shape[0]*template.shape[1]))
            R = np.sum(T * L)
            print(R)
            if R > bingo:
                bingo = R
                x_img = x
                y_img = y
            x+=4
        y+=4

    return x_img,y_img

#Normalized Cross-Correlation method
def NCC(img,template):
        x,y=0,0
        bingo=0
        #For loop moving 3 pixels right and bottom until done
        for i in range(template.shape[0],img.shape[0],4):
            x=0
            for j in range(template.shape[1],img.shape[1],4):
                top = np.sum(np.array(img[y:i,x:j], dtype=np.float32)*np.array(template, dtype=np.float32))
                bottom = np.dot(np.sum(np.array(img[y:i,x:j], dtype=np.float32)**2),np.sum(np.array(template, dtype=np.float32)**2))
                bottom = np.sqrt(bottom)
                R = top/bottom
                print(R)
                if R > bingo:
                    bingo = R
                    x_img = x
                    y_img = y
                x+=4
            y+=4

        return x_img,y_img

