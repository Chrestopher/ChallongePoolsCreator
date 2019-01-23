import tkinter as tk
from src import pool_creator


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("CPC")
        self.iconbitmap()
        self.geometry("230x300")
        tk.Label(self, text="").grid(row=0, columnspan=3)
        tk.Label(self, text="Challonge Pools Creator").grid(row=1, columnspan=3)
        tk.Label(self, text="By ChresSSB <3").grid(row=2, columnspan=3)
        tk.Label(self, text="").grid(row=3, columnspan=3)
        tk.Label(self, text="Username").grid(row=4)
        self.username = tk.Entry(self)
        self.username.grid(row=4, column=1)
        tk.Label(self, text="Tournament URL").grid(row=5)
        self.turl = tk.Entry(self)
        self.turl.grid(row=5, column=1)
        tk.Label(self, text="Number of Pools").grid(row=6)
        self.pools = tk.Entry(self)
        self.pools.grid(row=6, column=1)
        tk.Label(self, text="").grid(row=7)
        tk.Label(self, text="").grid(row=8)
        self.done = tk.Label(self, text="").grid(row=9)
        self.gen = tk.Button(self, text="Generate Pools", command= self.on_gen).grid(row=10, columnspan=2)
        tk.Label(self, text="").grid(row=11)
        self.clear = tk.Button(self, text="Clear", command=self.on_clear).grid(row=12, columnspan=2)

    def on_gen(self):
        pool_creator.creator([self.username.get(), self.turl.get(), self.pools.get()])
        self.done = tk.Label(self, text="Done!").grid(row=9, columnspan=2)

    def on_clear(self):
        pool_creator.clear([self.username.get(), self.turl.get(), self.pools.get()])
        self.done = tk.Label(self, text="Done!").grid(row=9, columnspan=2)

