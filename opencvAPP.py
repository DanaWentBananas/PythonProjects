from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

root = Tk()


x=''

def turnToGrey():
    global x
    x = 'GRAY'

def turnToHsv():
    global x
    x = 'HSV'

def turnToCartoon():
    global x
    x = 'CARTOON'

def turnToSketch():
    global x
    x = 'SKETCH'

def blurAvg():
    global x
    x = 'AVG'

def blurGaussian():
    global x
    x = 'GAUSSIAN'

def blurMedian():
    global x
    x = 'MEDIAN'

def blurBilateral():
    global x
    x = 'BILATERAL'

mainFrame = Frame(root)
mainFrame.pack()

l = Label(mainFrame,bg='red')
l.pack(side=LEFT)

buttonsFrame = Frame(mainFrame)
buttonsFrame.pack(side=LEFT)

colorSpacesTitle = Label(buttonsFrame,text="COLOR SPACES")
colorSpacesTitle.pack()
colorSpaces = Frame(buttonsFrame)
colorSpaces.pack(side=BOTTOM)

blursTitle = Label(buttonsFrame,text="BLURS")
blursTitle.pack(side=BOTTOM)
blurs = Frame(buttonsFrame)
blurs.pack(side=BOTTOM)

effectsTitle = Label(buttonsFrame,text="EFFECTS")
effectsTitle.pack(side=BOTTOM)
effects = Frame(buttonsFrame)
effects.pack(side=BOTTOM)

#COLOR SPACES
gray = Button(colorSpaces,text='grey',command=turnToGrey)
gray.pack(side=LEFT)

hsv = Button(colorSpaces,text='hsv',command=turnToHsv)
hsv.pack(side=LEFT)

#BLURS
avg = Button(blurs,text='mean',command=blurAvg)
avg.pack(side=LEFT)

gaussian = Button(blurs,text='gaussian',command=blurGaussian)
gaussian.pack(side=LEFT)

median = Button(blurs,text='median',command=blurMedian)
median.pack(side=LEFT)

bilateral = Button(blurs,text='bilateral',command=blurBilateral)
bilateral.pack(side=LEFT)


#EFFECTS
cartoon = Button(effects,text='cartoon',command=turnToCartoon)
cartoon.pack(side=LEFT)

sketch = Button(effects,text='sketch',command=turnToSketch)
sketch.pack(side=LEFT)

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    if x=='GRAY':
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    elif x=='HSV':
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    elif x=='SKETCH':
        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.GaussianBlur(grayFrame, (21,21),0,0)
        sketch = cv2.divide(grayFrame,blurFrame,scale=256)
        frame = ImageTk.PhotoImage(Image.fromarray(sketch))
        l.config(image = frame)
    elif x=='CARTOON':
        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.medianBlur(grayFrame,5)
        edges = cv2.adaptiveThreshold(blurFrame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        filter = cv2.bilateralFilter(frame,9,333,333)
        cartoon = cv2.bitwise_and(filter,filter,mask=edges)
        frame = ImageTk.PhotoImage(Image.fromarray(cartoon))
        l.config(image = frame)
    elif x=='AVG':
        frame = cv2.blur(frame,(21,21))
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    elif x=='GAUSSIAN':
        frame = cv2.GaussianBlur(frame,(21,21),0)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    elif x=='MEDIAN':
        frame = cv2.medianBlur(frame,21)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    elif x=='BILATERAL':
        frame = cv2.bilateralFilter(frame,9,100,100)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)
    else:
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l.config(image = frame)

    root.update()

cap.release()
cv2.destroyAllWindows()

