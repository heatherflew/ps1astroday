import Tkinter as tk
import numpy as np
from PIL import Image, ImageTk, ImageDraw,ImageOps, ImageEnhance

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.Imagevar=tk.StringVar()
        self.Rvar=tk.StringVar()
        self.Gvar=tk.StringVar()
        self.Bvar=tk.StringVar()
        #self.Imagevar.set("m16")
        #self.Rvar.set("None")
        #self.Gvar.set("None")
        #self.Bvar.set("None")
        self.r=0.5
        self.g=0.5
        self.b=0.5

        #self.setFileNames()

        
        self.createWidgets()
        self.setFileNames()
    def createWidgets(self):
        self.master.title("PanSTARRS colorizer")

        ####### Subdivided into 4 frames: 
        ####### frame1: upper left, for selecting images
        ####### frame2: upper right, for mapping RGB to filters
        ####### frame3: lower left, for adjusting the sliders
        ####### frame4: lower right, seeing the results

        ####### frame 1 ############
        frame1 = tk.LabelFrame(self, border =1, text = "Step 1")
        frame1.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E,padx=5,pady=5)
        tk.Label(frame1, text="Select a set of images").grid(row=0,column=0)
        rb1=tk.Radiobutton(frame1, text="M16",
                           variable=self.Imagevar,value="m16",
                           command=self.selectImg
                           )
        rb1.grid(row=1,column=0,padx=15)
        rb1.select()
        
        #self.Imagevar.set("m16")
        rb2=tk.Radiobutton(frame1, text="Horsehead",
                           variable=self.Imagevar,
                           value="horse",
                           command=self.selectImg
                           ).grid(row=1,column=1,padx=15)
        tk.Radiobutton(frame1, text="M17",
                       variable=self.Imagevar,
                       value="m17",
                       command=self.selectImg
                       ).grid(row=1,column=2,padx=15)
        tk.Radiobutton(frame1, text="M19",
                       variable=self.Imagevar,
                       value="m19",
                       command=self.selectImg
                       ).grid(row=2,column=0,padx=15)
        tk.Radiobutton(frame1, text="M20",
                       variable=self.Imagevar,
                       value="m20",
                       command=self.selectImg
                       ).grid(row=2,column=1,padx=15)
        tk.Radiobutton(frame1, text="M21",
                       variable=self.Imagevar,
                       value="m21",
                       command=self.selectImg
                       ).grid(row=2,column=2,padx=15)
        
        ####### frame 2 ############
        self.Rvar.set("None")
        self.Gvar.set("None")
        self.Bvar.set("None")
        frame2 = tk.LabelFrame(self, text="Step 2")
        frame2.grid(row=0,column=1,stick=tk.S+tk.E+tk.W+tk.N,padx=5,pady=5)
        tk.Label(frame2, text="Select a filter(grizy) for each channel (RGB)").grid(row=0, column=0)
        tk.Label(frame2, text="Red   (R) = ").grid(row=1,column=0)
        tk.Label(frame2, text="Green (G) = ").grid(row=2,column=0)
        tk.Label(frame2, text="Blue  (B) = ").grid(row=3,column=0)
        tk.Radiobutton(frame2, text="g",value="g",variable=self.Rvar,command=self.selectR).grid(row=1,column=1, padx=15)
        tk.Radiobutton(frame2, text="r",value="r",variable=self.Rvar,command=self.selectR).grid(row=1,column=2, padx=15)
        tk.Radiobutton(frame2, text="i",value="i",variable=self.Rvar,command=self.selectR).grid(row=1,column=3, padx=15)
        tk.Radiobutton(frame2, text="z",value="z",variable=self.Rvar,command=self.selectR).grid(row=1,column=4, padx=15)
        tk.Radiobutton(frame2, text="y",value="y",variable=self.Rvar,command=self.selectR).grid(row=1,column=5, padx=15)
        tk.Radiobutton(frame2, text="None",value="None",variable=self.Rvar,command=self.selectR).grid(row=1,column=6, padx=15)
        tk.Radiobutton(frame2, text="g",value="g",variable=self.Gvar,command=self.selectG).grid(row=2,column=1)
        tk.Radiobutton(frame2, text="r",value="r",variable=self.Gvar,command=self.selectG).grid(row=2,column=2)
        tk.Radiobutton(frame2, text="i",value="i",variable=self.Gvar,command=self.selectG).grid(row=2,column=3)
        tk.Radiobutton(frame2, text="z",value="z",variable=self.Gvar,command=self.selectG).grid(row=2,column=4)
        tk.Radiobutton(frame2, text="y",value="y",variable=self.Gvar,command=self.selectG).grid(row=2,column=5)
        tk.Radiobutton(frame2, text="None",value="None",variable=self.Gvar,command=self.selectG).grid(row=2,column=6)
        tk.Radiobutton(frame2, text="g",value="g",variable=self.Bvar,command=self.selectB).grid(row=3,column=1)
        tk.Radiobutton(frame2, text="r",value="r",variable=self.Bvar,command=self.selectB).grid(row=3,column=2)
        tk.Radiobutton(frame2, text="i",value="i",variable=self.Bvar,command=self.selectB).grid(row=3,column=3)
        tk.Radiobutton(frame2, text="z",value="z",variable=self.Bvar,command=self.selectB).grid(row=3,column=4)
        tk.Radiobutton(frame2, text="y",value="y",variable=self.Bvar,command=self.selectB).grid(row=3,column=5)
        tk.Radiobutton(frame2, text="None",value="None",variable=self.Bvar,command=self.selectB).grid(row=3,column=6)


        ####### frame 3 ############
        
        self.frame3 = tk.LabelFrame(self, text="Step 3")
        self.frame3.grid(row=1,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)
        frame3R = tk.Label(self.frame3,text="Red")
        frame3R.grid(row=1,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)

        frame3R = tk.Label(self.frame3,text="---------------------------------------")
        frame3R.grid(row=2,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5, columnspan=2)
        frame3G = tk.Label(self.frame3,text="Green")
        frame3G.grid(row=3,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)

        frame3R = tk.Label(self.frame3,text="---------------------------------------")
        frame3R.grid(row=4,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5,columnspan=2)
        frame3B = tk.Label(self.frame3,text="Blue")
        frame3B.grid(row=5,column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)

        gim = tk.PhotoImage(file='m16_smallest_None.pgm')
        rim = tk.PhotoImage(file='m16_smallest_None.pgm')
        iim = tk.PhotoImage(file='m16_smallest_None.pgm')

        buttong=tk.Label(self.frame3,image=gim)
        buttong.img = gim
        buttong.grid(column=0,row=1)
        var= tk.IntVar()
        var2= tk.IntVar()
        var3= tk.IntVar()

        self.scale = tk.Scale(self.frame3, orient=tk.HORIZONTAL, length=100, label="Red scale", resolution = 0.1, to =2, showvalue=0, command=self.getr)
        self.scale.grid(column=1,row=1)
        self.scale.set(0.5)
        self.scale2 = tk.Scale(self.frame3, orient=tk.HORIZONTAL, length=100, label="Green scale", resolution=0.1, to=2, showvalue=0, command=self.getg )
        self.scale2.grid(column=1,row=3)
        self.scale2.set(0.5)
        self.scale3 = tk.Scale(self.frame3, orient=tk.HORIZONTAL, length=100, label="Blue scale", resolution=0.1, to=2, showvalue=0, command = self.getb)
        self.scale3.grid(column=1,row=5)
        self.scale3.set(0.5)
        buttonr=tk.Label(self.frame3,image=rim)
        buttonr.img = rim
        buttonr.grid(column=0,row=3)
        buttoni=tk.Label(self.frame3,image=iim)
        buttoni.img = iim
        buttoni.grid(column=0,row=5)
        
        
        ####### frame 4 ############
        
        self.frame4 = tk.LabelFrame(self, text="Result")
        self.frame4.grid(row=1,column=1, sticky=tk.N+tk.S+tk.E+tk.W,padx=5,pady=5)
        #tk.Label(frame4, text="result").grid(row=0,column=0)
        rgbbig = tk.PhotoImage(file="m16_smaller_None.pgm")
        self.buttonrgbbig = tk.Label(self.frame4, image=rgbbig)
        self.buttonrgbbig.img = rgbbig
        self.buttonrgbbig.grid(column=0,row=0)

    def selectImg(self):
        self.setFileNames()
        print self.Imagevar.get()
        self.redraw()
        Rim=tk.PhotoImage(file=self.Rthumb)
        buttonr = tk.Label(self.frame3,image=Rim)
        buttonr.img =Rim
        buttonr.grid(column=0,row=1)
        Gim=tk.PhotoImage(file=self.Gthumb)
        buttong = tk.Label(self.frame3,image=Gim)
        buttong.img =Gim
        buttong.grid(column=0,row=3)
        Bim=tk.PhotoImage(file=self.Bthumb)
        buttonb = tk.Label(self.frame3,image=Bim)
        buttonb.img =Bim
        buttonb.grid(column=0,row=5)
        
    def selectR(self):
        self.setFileNames()
        print self.Rvar.get()
        Rim=tk.PhotoImage(file=self.Rthumb)
        buttonr = tk.Label(self.frame3,image=Rim)
        buttonr.img =Rim
        buttonr.grid(column=0,row=1)
        
    def selectG(self):
        self.setFileNames()
        print self.Gvar.get()
        Gim=tk.PhotoImage(file=self.Gthumb)
        buttong = tk.Label(self.frame3,image=Gim)
        buttong.img =Gim
        buttong.grid(column=0,row=3)

    def selectB(self):
        self.setFileNames()
        print self.Bvar.get()
        Bim=tk.PhotoImage(file=self.Bthumb)
        buttonb = tk.Label(self.frame3,image=Bim)
        buttonb.img =Bim
        buttonb.grid(column=0,row=5)
        
    def setFileNames(self):
        self.Rthumb = self.Imagevar.get() +"_smallest_"+self.Rvar.get()+".pgm" 
        self.Gthumb = self.Imagevar.get() +"_smallest_"+self.Gvar.get()+".pgm" 
        self.Bthumb = self.Imagevar.get() +"_smallest_"+self.Bvar.get()+".pgm" 
        self.Rbig = self.Imagevar.get() +"_smaller_"+self.Rvar.get()+".pgm" 
        self.Gbig = self.Imagevar.get() +"_smaller_"+self.Gvar.get()+".pgm" 
        self.Bbig = self.Imagevar.get() +"_smaller_"+self.Bvar.get()+".pgm"  
        print "R files ",self.Rthumb,self.Rbig
        print "G files ",self.Gthumb,self.Gbig
        print "B files ",self.Bthumb,self.Bbig
        self.imgR=Image.open(self.Rbig)
        self.imgR=self.imgR.convert("RGB")
        arrayR=np.array(self.imgR)
        self.arrR=arrayR[:,:,1]
        self.imgG=Image.open(self.Gbig)
        self.imgG=self.imgG.convert("RGB")
        arrayG=np.array(self.imgG)
        self.arrG=arrayG[:,:,1]
        self.imgB=Image.open(self.Bbig)
        self.imgB=self.imgB.convert("RGB")
        arrayB=np.array(self.imgB)
        self.arrB=arrayB[:,:,1]
        self.redraw()
        print self.arrB

    def redraw(self):
        #print "redraws stuff"
        arrR2=self.arrR*float(self.r)
        arrG2=self.arrG*float(self.g)
        arrB2=self.arrB*float(self.b)
        arrR2[arrR2>253]=254
        arrG2[arrG2>253]=254
        arrB2[arrB2>253]=254
        arrR3=arrR2.astype('uint8')
        arrG3=arrG2.astype('uint8')
        arrB3=arrB2.astype('uint8')
        
        
        imr = Image.fromarray(arrR3)
        img =Image.fromarray(arrG3)
        imb =Image.fromarray(arrB3)
        imgRGB=Image.merge('RGB',(imr,img,imb))
        imgRGB2=ImageTk.PhotoImage(imgRGB)
        self.buttonrgb=tk.Label(self.frame4,image=imgRGB2)
        self.buttonrgb.img=imgRGB2
        self.buttonrgb.grid(column=0,row=0)
        
    def getr(self,r):
        self.r=r
        self.redraw()
    def getg(self,g):
        self.g=g
        self.redraw()
    def getb(self,b):
        self.b=b
        self.redraw()

        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
