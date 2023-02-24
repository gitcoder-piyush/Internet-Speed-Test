from tkinter import *
import tkinter as tk
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up =  str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test - Piyush")
sp.geometry("500x700")
logo = PhotoImage(file="—Pngtree—speed meter for automobile or_4103470.png")
sp.iconphoto(False, logo)
sp.config(bg="black")

lab = Label(sp,text = "Speed Test by Piyush", font = ("Time New Roman", 25, "bold"), bg="black", fg="cyan")
lab.place(x=60,y=40, height=50, width=380)

lab = Label(sp,text = "Downloading Speed", font = ("Time New Roman", 30, "bold"), bg="black", fg="deeppink")
lab.place(x=60,y=130, height=50, width=380)

lab_down = Label(sp,text = "00", font = ("Time New Roman", 30, "bold"), bg="black", fg="green")
lab_down.place(x=60,y=200, height=50, width=380)

lab = Label(sp,text = "Uploading Speed", font = ("Time New Roman", 30, "bold"), bg="black", fg="deeppink")
lab.place(x=60,y=290, height=50, width=380)

lab_up = Label(sp,text = "00", font = ("Time New Roman", 30, "bold"), bg="black", fg="green")
lab_up.place(x=60,y=360, height=50, width=380)




button = Button(sp, text="GO", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="black", fg="greenyellow", bd=0, command=speedcheck)
button.place(x=60,y=460, height=50, width=380)


sp.mainloop()
