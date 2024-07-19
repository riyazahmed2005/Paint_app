# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:33:00 2024
         New paint app
         
@author: Riyaz
"""

import tkinter as tk
import PIL.ImageGrab as Image_grab
w=tk.Tk()

x1=0 
y1=0 


color_var="black"
width_val=2


dash_val=()
def window():
    
    w.title('freehand-drawing')
    w.geometry('1000x600+200+0')
    w.resizable(False,False)
    
def left_clicked(event):
    global x1,y1
    x1=event.x
    y1=event.y 
def motion(event):
    global color,width_val,dash_val
    global x1,y1
    x2=event.x 
    y2=event.y 
    canva.create_line(x1,y1,x2,y2,fill=color_var,width=width_val,dash=dash_val)
    x1=x2
    y1=y2
    
def colors(color):
    global color_var
    color_var=color
    
def width(width):
    global width_val
    width_val=width
    
def paint_style(dash):
    global dash_val
    dash_val=dash
    
def Pencil():
    global color_var
    color_var="black"
    canva.config(cursor="arrow")
    
def Eraser():
    global color_var,width_val
    my_color='gray'
    color_var=my_color
    width_val=2
    canva.config(cursor="circle")
    
def save(event):
    x=w.winfo_rootx()
    y=w.winfo_rooty()
    img=Image_grab.grab(bbox=(205,50,1000+x,600))
    img.show()

def design():
    global canva
    canva=tk.Canvas(w,width=1000,height=600,bg="gray")
    canva.place(x=0,y=0)
    
    menu_bar=tk.Menu(w)    # Top level menu bar attached to mainwindow
# =============================================================================
#                               Draw
# =============================================================================
    draw_menu=tk.Menu(menu_bar,tearoff=0)    #submenu attached to toplevel menu
    draw_menu.add_command(label="Pencil",command=Pencil)
    draw_menu.add_command(label="Eraser",command=Eraser)
    menu_bar.add_cascade(label="Draw",menu=draw_menu)
# =============================================================================
#                       Color menu 
# =============================================================================
    color_menu=tk.Menu(menu_bar,tearoff=0)    #submenu attached to toplevel menu
    color_menu.add_command(label="blue",command=lambda:colors("blue"))
    color_menu.add_command(label="red",command=lambda:colors("red"))
    color_menu.add_command(label="green",command=lambda:colors("green"))
    color_menu.add_command(label="yellow",command=lambda:colors("yellow"))
    color_menu.add_command(label="black",command=lambda:colors("black"))
    menu_bar.add_cascade(label="Colors",menu=color_menu)
    
# =============================================================================
#                       Width menu
# =============================================================================
    width_menu=tk.Menu(menu_bar,tearoff=0)
    width_menu.add_command(label="Line Width 1",command=lambda:width(2))
    width_menu.add_command(label="Line Width 2",command=lambda:width(3))
    width_menu.add_command(label="Line Width 3",command=lambda:width(4))
    width_menu.add_command(label="Line Width 4",command=lambda:width(5))
    width_menu.add_command(label="Line Width 5",command=lambda:width(6))
    menu_bar.add_cascade(label="Width",menu=width_menu)
# =============================================================================
#                       Style menu
# =============================================================================
    style=tk.Menu(menu_bar,tearoff=0)    
    style.add_command(label="Dash 1",command=lambda:paint_style((4,2)))
    style.add_command(label="Dash 2",command=lambda:paint_style((5,6)))
    style.add_command(label="Dash 3",command=lambda:paint_style((6,7)))
    style.add_command(label="No Dash",command=lambda:paint_style(()))
    menu_bar.add_cascade(label="Style",menu=style)
    
    canva.bind("<Button-1>",left_clicked)
    canva.bind("<B1-Motion>",motion)
    w.bind("<Control-s>",save)
    canva.bind("<Control-s>",save)
    
    w.config(menu=menu_bar)
    w.mainloop()
window()
design()
