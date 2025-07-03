#Study Planner App
from tkinter import *
import customtkinter as ctk
from CTkTable import *
from pages.searchPage import searchPage
from pages.addPage import addPage 



app = ctk.CTk()
app.Title("Study Planner")
app.geometry("1000x600")
# Configure app window grid
app.grid_columnconfigure(0, weight=1)       #Left Column
app.grid_columnconfigure(1, weight=4)       #Right Column 
app.grid_rowconfigure(0, weight=1)      # Title 
app.grid_rowconfigure(1, weight=1)      # slogan  
app.grid_rowconfigure(2, weight=1)      # Home 
app.grid_rowconfigure(3, weight=1)      # Tasks
app.grid_rowconfigure(4, weight=1)      # Calendar

#─── Left Frame ────────────────────────────────────────────
leftFrame = ctk.CTkFrame(app, border_width=2) 



    





app.mainloop