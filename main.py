import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk


from controller import Controller


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        style = ttk.Style()
        self._parent = parent
        self._menubar = tk.Menu()
        self._parent.config(menu=self._menubar)

        self._sub_menu_file = tk.Menu(self._menubar, tearoff=False, background='AliceBlue', activebackground='CornflowerBlue')
        self._sub_menu_file.add_command(label="   Open   ", command=self.open_file)
        self._sub_menu_file.add_command(label="   Save As   ", command=self.save_file)
        self._sub_menu_file.add_command(label="   New file    ", command=self.new_file)
        self._sub_menu_file.add_separator()
        self._sub_menu_file.add_command(label="   Exit   ", command=self.exit_file)
        self._menubar.add_cascade(label="File", menu=self._sub_menu_file)

        self._controller = Controller(self)
        self._controller.pack(side="bottom", fill="both", expand=True)

        self._edit_menu = tk.Menu(self._menubar, tearoff=0, background='AliceBlue', activebackground='CornflowerBlue')
        self._menubar.add_cascade(label="    Edit    ", menu=self._edit_menu)
        self._edit_menu.add_command(label="    Undo    ", command=self.undo_text)
        self._edit_menu.add_command(label="    Redo    ", command=self.redo_text)
        self._edit_menu.add_separator()
        self._edit_menu.add_command(label="    Cut     ", command=self.cut_text)
        self._edit_menu.add_command(label="    Copy    ", command=self.copy_text)
        self._edit_menu.add_command(label="    Paste   ", command=self.paste_text)

        self._changes = []
        self._current_change = -1
        self._applying_changes = False
        self._typing = False
        self.add_change()

        # Trace changes to update undo and redo buttons
        self._controller.text_widget.text_area.bind("<KeyRelease>", self.on_key_press)

        self._parent.bind("<Control-n>", lambda event: self.new_file())
        self._parent.bind("<Control-s>", lambda event: self.save_file())
        self._parent.bind("<Control-o>", lambda event: self.open_file())

    def new_file(self):
        self._controller.text_widget.text_area.delete(1.0, tk.END)
        self.reset_changes()
        self.add_change()

    def open_file(self):
        file_path = fd.askopenfilename()
        if file_path:
            with open(file_path, 'r',encoding='utf-8') as file:
                self._controller.text_widget.text_area.delete(1.0, tk.END)
                self._controller.text_widget.text_area.insert(tk.END, file.read())
                self.reset_changes()
        self.add_change()

    def save_file(self):
        file_path = fd.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.")),
                                         defaultextension=".txt")
        if file_path:
            with open(file_path, 'w',encoding='utf-8') as file:
                file.write(self._controller.text_widget.text_area.get(1.0, tk.END))
                self.reset_changes()
        self.add_change()

    def exit_file(self):
        self._parent.destroy()

    def copy_text(self):
        self._parent.clipboard_clear()
        text = self._controller.text_widget.text_area.get("sel.first", "sel.last")
        self._parent.clipboard_append(text)
        self.add_change()

    def cut_text(self):
        self.copy_text()
        self._controller.text_widget.text_area.delete("sel.first", "sel.last")
        self.add_change()

    def paste_text(self):
        text = self._parent.clipboard_get()
        self._controller.text_widget.text_area.insert(tk.INSERT, text)
        self.add_change()

    def undo_text(self):
        if self._current_change > 0:
            self._applying_changes = True
            self._current_change -= 1
            self._controller.text_widget.text_area.delete(1.0, tk.END)
            self._controller.text_widget.text_area.insert(tk.END, self._changes[self._current_change])
            self._applying_changes = False

    def redo_text(self):
        if self._current_change < len(self._changes) - 1:
            self._applying_changes = True
            self._current_change += 1
            self._controller.text_widget.text_area.delete(1.0, tk.END)
            self._controller.text_widget.text_area.insert(tk.END, self._changes[self._current_change])
            self._applying_changes = False

    def on_key_press(self, event):

        if not self._typing:
            self._typing = True
            self.add_change()
        self._typing = False

    def add_change(self):
        content = self._controller.text_widget.text_area.get(1.0, tk.END)
        # Remove the changes after the current change index
        if not self._changes or content != self._changes[-1]:
            self._changes = self._changes[: self._current_change + 1]
            self._changes.append(content)
            self._current_change = len(self._changes) -1

            
    def reset_changes(self):
        self._changes = []
        self._current_change = -1


if __name__ == '__main__':
    root = tk.Tk()

    root.title("3TSearch - A simple text editor")
    root.minsize(400, 300)
    root.iconbitmap(r'.\3T.ico')

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
