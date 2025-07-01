#Study Planner App
from tkinter import *
import customtkinter as ctk
from CTkTable import *
from paes.searchPage import searchPage
from pages.addPage import addPage 



app = ctk.CTk()
app.Title("Study Planner")
app.geometry("1000x600")
# Configure app window grid
left_frame  =  Frame(app,  width=200,  height=  400,  bg='black')
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

right_frame  =  Frame(app,  width=650,  height=400,  bg='white')
right_frame.grid(row=0,  column=1,  padx=10,  pady=5)


    





app.mainloop