import tkinter as tk
import time
import numpy as np

a=tk.Tk()
c=tk.Canvas(a,width=1000,height=2200,bg="sky blue")
c.grid(row=1, column=1,columnspan=4,sticky="w")
cs=[c.create_oval(0,0,0,0) for i in range(700)]
cs1=[c.create_oval(0,0,0,0) for i in range(700)]
ls=[c.create_oval(0,0,0,0) for i in range(700)]

def wave(f1,a1,f2,a2,disy=800,s1=0,s=0):
    k=0
    color="red"
    for i in range(50):
        c.create_line(i*20,0,i*20,2200,fill="grey")
    for g in range(110):
        c.create_line(0,g*20,1000,g*20,fill="grey")
    c.create_line(500,0,500,2500,fill=color)
    c.create_line(0,1500,1000,1500,fill=color)
    c.create_line(0,800,1000,800,fill=color)
    c.create_text(700,200,text="amplitude="+str(a1/200)+"V\nfreq="+str(f1)+"kHz",fill="brown")
    c.create_text(700,400,text="amplitude="+str(a2/200)+"V\nfreq="+str(f2)+"kHz",fill="yellow")
    for e in range(1,700):
        ls[e]=c.create_oval(500+a1*np.sin(f1*(s1+k+e/100)),1500+a2*np.sin(f2*(s+k+e/100)),504+a1*np.sin(f1*(s1+k+e/100)),1504+a2*np.sin(f2*(s+k+e/100)),fill="yellow")
        cs[e]=c.create_oval(150+e,disy+a1*np.sin(f1*(s1+k+e/100)),150+e+4,disy+4+a1*np.sin(f1*(s1+k+e/100)),fill="red")
        cs1[e]=c.create_oval(150+e,disy+a2*np.sin(f2*(s+k+e/100)),150+e+4,disy+4+a2*np.sin(f2*(s+k+e/100)),fill="yellow")

i=0
ai=0
fi=0
wave(1,200,1,200,s=i)
re=False

def increase_amplitude():
    global ai,i,fi
    ai=ai+1
    c.delete("all")
    wave(1,200,1+fi,200+ai,s=i)
    c.update()


def increase_frequency():
    global ai,i,fi
    c.delete("all")
    wave(1,200,1+fi,200+ai,s=i)
    c.update()
    fi=fi+1

def reset():
    global ai,i,fi,re
    re=True
    ai,i,fi=0,0,0
    c.delete("all")
    wave(1,200,1,200+ai,s=i)
    c.update()

def create_wave():
    global i,ai,fi,re
    while not re:
        c.delete("all")
        time.sleep(0.01)
        wave(1,200,1+fi,200+ai,s=i)
        c.update()
        i=i+0.01
        if i>=2*np.pi:
            i=0


shiftb=tk.Button(a,text="shift",command=create_wave)
shiftb.grid(row=2,column=1)
amplitudeB=tk.Button(a,text="amplitude+",command=increase_amplitude)
amplitudeB.grid(row=2,column=2)
freqB=tk.Button(a,text="freq+",command=increase_frequency)
freqB.grid(row=2,column=3)
resetB=tk.Button(a,text="reset",command=reset)
resetB.grid(row=2,column=4)
a.mainloop()