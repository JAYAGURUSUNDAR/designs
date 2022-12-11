import tkinter as tk
import time
import numpy as np

a=tk.Tk()
c=tk.Canvas(a,width=1000,height=2500,bg="black")
c.pack()


def animate(event):
        x=lambda x0,r0,t:500+r0*np.cos(x0*5*np.pi/2+i*t/5)
        y=lambda y0,r0,t:1100-r0*np.sin(y0*5*np.pi/2 +i*t/5)
        i=0
        r=50
        c1=["red","orange","brown","white","cyan","sky blue","green","light green","blue"]
        while True:
            c.delete("all")
            time.sleep(0.0001)
            for o in range(10,1,-1):
                c.create_polygon(
                x(0,o*r,o),y(0,o*r,o),
                x(1,o*r,o),y(1,o*r,o),
                x(2,o*r,o),y(2,o*r,o),
                x(3,o*r,o),y(3,o*r,o),
                x(0,o*r,o),y(0,o*r,o),fill=c1[10-o])
                for v in range(4):
                    c.create_oval(x(v,o*r,o)-10,y(v,o*r,o)-10,x(v,o*r,o)+10,y(v,o*r,o)+10,fill="yellow")
            c.update()
            i=i+0.001
            if i>=10*np.pi:i=0
        
a.bind("<Button-1>",animate)
a.mainloop()