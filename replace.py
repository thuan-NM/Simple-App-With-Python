import tkinter as tk
from tkinter import simpledialog

class ReplaceDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Find:").grid(row=0)
        tk.Label(master, text="Replace:").grid(row=1)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)

        self.e1.config(width=30,background="White")
        self.e2.config(width=30,background="White")
        self.config(pady=20,padx=20)

        self.e1.grid(row=0, column=1,pady=10)
        self.e2.grid(row=1, column=1,pady=10)
        return self.e1  # initial focus

    def apply(self):
        self.find_text = self.e1.get()
        self.replace_text = self.e2.get()


# root = tk.Tk()
# d = ReplaceDialog(root)
# d.title("3TSearch - A simple text editor")
# d.minsize(400, 300)
# d.iconbitmap(None)
# print("Find:", d.find_text)
# print("Replace:", d.replace_text)
