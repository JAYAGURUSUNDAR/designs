import tkinter as tk
import numpy as np


root=tk.Tk()
r=4

text_boxes=[]
for i in range(r):
    text_boxes.append([])
    for j in range(r):
        text_boxes[i].append(tk.Text(root,height=2,width=4,state="normal"))
        text_boxes[i][j].grid(row=i,column=j)

A=[]
def compute_deter():
      global A
      for i in range(r):
          A.append([])
          for j in range(r):
              input_value = text_boxes[i][j].get('1.0', tk.END)
              for line in input_value.split('\n'):
                  try:
                      number = float(line.strip())
                      A[i].append(number)
                  except ValueError:
                      pass
      label.config(text=str(round(np.linalg.det(np.array(A)),3)))
      A=[]
      
      
button=tk.Button(root,text="|A|",command=compute_deter)
button.grid(row=r+1,column=0,columnspan=r)
label=tk.Label(root,text="Enter the \nvalues")
label.grid(row=r+2,column=0,columnspan=r)
      
root.mainloop()