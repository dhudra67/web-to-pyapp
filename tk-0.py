import tkinter as tk
from tkinter import ttk
import webview
root = tk.Tk()
root.title("Hd Today")
root.geometry('1400x900+50+50')
webview.create_window('HD SERIES' , 'https://hdtoday.tv/home')
webview.start()

