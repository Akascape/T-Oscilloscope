#################--------T-Oscilloscope--------#################
# Developer: Akash Bora (Akascape)
# License: MIT

import turtle
import tkinter
import customtkinter
import math
import threading
import sys
from widgets.volume_control import VolumeControl
from widgets.spinbox import CTkSpinbox
from widgets.tooltip import ToolTip

try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(0)
except:
    pass

customtkinter.set_appearance_mode("System") # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")

if customtkinter.get_appearance_mode()=="Dark":
    o = 1
else:
    o = 0
    
HEIGHT = 430
WIDTH = 840

Omega1 = 1
Omega2 = 1
onLoop = True

def description():
    tools = {Label_1: "This is the window refreshed rate, this can lead to quality "+
             "render but slower drawing time, or a short drawing time but sharp renders",
             Label_2: "It effectively makes the electron travel faster, making the image brighter",
             Label_3: "Move the plates in relation to each other in an angle from 0 to 180 degrees",
             Label_4: "Choose between some plate frequency relations optimized for Lissajous curves",
             custom: "Manually enter the frequency relation",
             color_bt: "Change the electron beam color",
             reset_bt: "Clear the canvas",
             checkbox: "Lock-Mode"}
    
    for i in tools:
        ToolTip(i, msg=tools[i], delay=1, follow=True, bg=customtkinter.ThemeManager.theme["color"]["frame_high"][o],
                fg=customtkinter.ThemeManager.theme["color"]["text"][o])
        
def changeOmega():
    global Omega1,Omega2
    if custom.get()==1:
        Omega1 = int(spinbox_1.get())
        Omega2 = int(spinbox_2.get())
    else:    
        list = var.get().split(",")
        Omega1 = int(list[0])
        Omega2 = int(list[1])
        
def lockmode():
    global Omega1, Omega2
    if checkbox.get()==1:
        Omega1 = 0
        Omega2 = 0     
    else:
        Omega1 = 1
        Omega2 = 1
        
def frequency_mode():
    spinbox_1.place_forget()
    spinbox_2.place_forget()
    radiobutton_1.place_forget()
    radiobutton_2.place_forget()
    radiobutton_3.place_forget()
    radiobutton_4.place_forget()
    
    if custom.get()==1:
        spinbox_1.place(x=20, y=345)
        spinbox_2.place(x=155, y=345)
        changeOmega()
    else:
        radiobutton_1.place(x=25, y=350)
        radiobutton_2.place(x=85, y=350)
        radiobutton_3.place(x=145, y=350)
        radiobutton_4.place(x=205, y=350)
        changeOmega()
        
cbt={}   
def color():
    
    def changecolor(i=7):
        if i==7:
            color_bt.configure(fg_color="white", state="normal")
        else:
            color_bt.configure(fg_color=cbt[i].fg_color, state="normal")
        win2.destroy()
        
    color_bt.configure(state="disabled")
    colors = ["red","chartreuse","blue", "aqua", "yellow", "magenta"]
    win2 = customtkinter.CTkToplevel()
    win2.maxsize(180,75)
    win2.minsize(180,75)
    win2.title("")
    win2.protocol("WM_DELETE_WINDOW", changecolor)
    
    x=0
    for i in range(6):
        cbt[x] = customtkinter.CTkButton(master=win2, width=50, hover=False, text="", fg_color=colors[x], command=lambda i=i: changecolor(i))
        if i<3:
            cbt[x].grid(row=0, column=i, padx=5, pady=(5,0))
        else:
            cbt[x].grid(row=1, column=5-i, padx=5, pady=5)
        x+=1
        
def x(t):
    return (slider_h.get()/100) * math.cos((Omega1*t))

def y(t):
    return (slider_v.get()/100) * math.cos((Omega2*t)+degreeToRad(slider.get()))

def degreeToRad(a):
    return (a * math.pi / 180)
    
def draw(time):
    try:
        x_axis = x(time*0.1*(int(knob1.value)/50))
        y_axis = y(time*0.1*(int(knob1.value)/50))

        x_value.goto(x_axis*100,-300)
        y_value.goto(300,+y_axis*100)
        screen_value.goto(x_axis*215,y_axis*150)
        
        if color_bt.fg_color=="red":
            screen_value.pencolor(int(knob2.value),0,0)
        elif color_bt.fg_color=="chartreuse":
            screen_value.pencolor(0,int(knob2.value),0)
        elif color_bt.fg_color=="blue":
            screen_value.pencolor(0,0,int(knob2.value))
        elif color_bt.fg_color=="aqua":
            screen_value.pencolor(0,int(knob2.value),int(knob2.value))
        elif color_bt.fg_color=="magenta":
            screen_value.pencolor(int(knob2.value),0,int(knob2.value))
        elif color_bt.fg_color=="yellow":
            screen_value.pencolor(int(knob2.value),int(knob2.value),0)
        elif color_bt.fg_color=="white":
            screen_value.pencolor(int(knob2.value),int(knob2.value),int(knob2.value))
        
        screen_value.pendown()
        y_value.pendown()
        x_value.pendown()
    except:
        pass
        
def reset():
    x_value.clear()
    y_value.clear()
    screen_value.clear()
           
def stop():   
    global onLoop
    onLoop = False
    des = tkinter.messagebox.askquestion("Exit","Do you want to exit?")
    if des=="yes":
        print("Please ignore error messages!")
        app.after(1000,app.destroy())
        sys.exit()
    else:
        onLoop = True
        main()
        
def main():
    time = 0
    while onLoop:
        draw(time)
        time += 1
        
### App ###
        
app = customtkinter.CTk()
app.title("T-Oscilloscope")
app.geometry((f"{WIDTH}x{HEIGHT}"))
                
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.protocol("WM_DELETE_WINDOW", stop)
app.resizable(width=False, height=False)
app.bind("<1>", lambda event: event.widget.focus_set())

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(padx=20, pady=20, sticky="nswe")

customtkinter.FontManager.load_font("widgets//Orbitron-Bold.ttf") #Google Fonts: https://fonts.google.com/specimen/Orbitron

Label = customtkinter.CTkLabel(master=frame_1, text="T-Oscilloscope", text_font="orbitron 25")
Label.grid(row=0, padx=10, pady=10, sticky="w")

bar = customtkinter.CTkProgressBar(master=frame_1, width=280, height=5, corner_radius=10,
                                   progress_color=customtkinter.ThemeManager.theme["color"]["slider"][o])
bar.place(x=10, y=55)
bar.set(0)
        
var = tkinter.StringVar()

Label_1 = customtkinter.CTkLabel(master=frame_1, text="Latency")
Label_1.grid(row=1, padx=5, pady=10, sticky="w")

canvas = tkinter.Canvas(master=frame_1, bg=customtkinter.ThemeManager.theme["color"]["frame_low"][o],
                        relief="flat", highlightthickness=0, width=150, height=150)
canvas.place(x=20, y=100)

knob1 = VolumeControl(
    master=canvas,
    x=30,
    y=30,
    start=1,
    end=100,
    radius=50,
    distance=40,
    length=9,
    width=4,
    needle_color="grey",
    unit_color= "grey",
    text_color=customtkinter.ThemeManager.theme["color"]["text"][o],
    color_gradient={"from": "green", "to": "cyan"})

Label_2 = customtkinter.CTkLabel(master=frame_1, text="Voltage")
Label_2.grid(row=1, padx=140, pady=5, sticky="w")

canvas2 = tkinter.Canvas(master=frame_1, bg=customtkinter.ThemeManager.theme["color"]["frame_low"][o],
                        relief="flat", highlightthickness=0, width=150, height=150)
canvas2.place(x=152, y=100)

knob2 = VolumeControl(
    master=canvas2,
    x=30,
    y=30,
    start=255,
    end=0,
    radius=50,
    distance=40,
    length=9,
    width=4,
    text_title="V: ",
    needle_color="grey",
    unit_color= "grey",
    integer=True,
    text_color=customtkinter.ThemeManager.theme["color"]["text"][o],
    color_gradient={"from": "pink", "to": "blue"})

Label_3 = customtkinter.CTkLabel(master=frame_1, text="Phase Shift: 0.0", anchor="w")
Label_3.place(x=25, y=250)

slider = customtkinter.CTkSlider(master=frame_1, width=240, from_=0, to=180, number_of_steps=180, button_color="white",
                                 button_hover_color=None, command=lambda event: Label_3.configure(text="Phase Shift: "+str(slider.get())))
slider.place(x=20, y=285)
slider.set(0)

Label_4 = customtkinter.CTkLabel(master=frame_1, text="Frequency", anchor="w")
Label_4.place(x=25, y=310)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value="1,1", text="1:1", command=changeOmega)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value="1,2", text="1:2", command=changeOmega)

radiobutton_3 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value="1,3", text="1:3", command=changeOmega)

radiobutton_4 = customtkinter.CTkRadioButton(master=frame_1, variable=var, value="2,3", text="2:3", command=changeOmega)
radiobutton_1.select()

slider_h = customtkinter.CTkSlider(master=frame_1, from_=-100, to=100, number_of_steps=200, width=460, progress_color=None)
slider_h.place(x=295, y=350)

slider_v = customtkinter.CTkSlider(master=frame_1, from_=-100, to=100, number_of_steps=200, height=320, orient="vertical", progress_color=None)
slider_v.place(x=765, y=5)

checkbox = customtkinter.CTkCheckBox(master=frame_1, text="", command=lockmode)
checkbox.place(x=760, y=340)

color_bt = customtkinter.CTkButton(master=frame_1, width=30, hover=False, fg_color="aqua", text="", command=color)
color_bt.place(x=125, y=215)

custom = customtkinter.CTkSwitch(master=frame_1, width=30, text="custom", command=frequency_mode)
custom.place(x=170, y=315)

spinbox_1 = CTkSpinbox(master=frame_1, min_value=0, max_value=99, command=changeOmega)

spinbox_2 = CTkSpinbox(master=frame_1, min_value=0, max_value=99, command=changeOmega)

frequency_mode()

### Turtle Screen ###

canvas3 = tkinter.Canvas(master=frame_1, bg="black", relief="flat", highlightthickness=0, width=450, height=320)
canvas3.place(x=300, y=10)

screen = turtle.TurtleScreen(canvas3)
screen.bgcolor("black")
screen.colormode(255)

x_value = turtle.RawTurtle(screen)
y_value = turtle.RawTurtle(screen)
screen_value = turtle.RawTurtle(screen)

x_value.shape("circle")
y_value.shape("circle")
screen_value.shape("circle")

x_value.color(customtkinter.ThemeManager.theme["color"]["button"][o])
y_value.color(customtkinter.ThemeManager.theme["color"]["button"][o])

x_value.penup()
y_value.penup()
screen_value.penup()

screen_value.turtlesize(0.5)
screen_value.pensize(5)

reset_bt = customtkinter.CTkButton(master=frame_1, width=1, height=1,fg_color="black", bg_color="black",
                                   hover=False, command=reset, text="⟳", text_color="white")
reset_bt.place(x=720, y=10)

description()

if __name__ == "__main__":
    threading.Thread(target=main).start()
    app.mainloop()
