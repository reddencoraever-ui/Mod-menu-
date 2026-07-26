import tkinter as tk

root = tk.Tk()
root.title("Developer Menu")
root.geometry("500x350")

# ----- Create Pages -----
pages = {}

def show_page(name):
    for page in pages.values():
        page.pack_forget()
    pages[name].pack(fill="both", expand=True)

# Navigation Bar
nav = tk.Frame(root)
nav.pack(side="top", fill="x")

# Pages
for name in ["Player", "World", "Visual", "Settings"]:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Developer Menu")
root.geometry("500x350")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ---------- Pages ----------
player_page = ttk.Frame(notebook)
world_page = ttk.Frame(notebook)
settings_page = ttk.Frame(notebook)

notebook.add(player_page, text="Player")
notebook.add(world_page, text="World")
notebook.add(settings_page, text="Settings")
