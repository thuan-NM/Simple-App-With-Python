import tkinter as tk
from tkinter import ttk
from replace import ReplaceDialog


class Search(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        style = ttk.Style()
        self._input = ttk.Entry(self)
        self._input.insert(0, "3TSearch")
        self._input.configure(foreground="gray")
        # Create style Object
        
        style.configure('TButton', font =
                    ('calibri', 10, 'bold'),
                            borderwidth = '2')
        style.configure('TEntry', font =
                    ('calibri', 10, 'bold'),
                            borderwidth = '2')
        style.map('TButton', foreground = [('active', '!disabled', 'green')],
                            background = [('active', 'black')])
        # style.configure('TFrame',background='DarkSeaGreen')
        self._search_button = ttk.Button(self, text="Search")
        self._find_next = ttk.Button(self, text="Find next")
        self._replace = ttk.Button(self, text="Replace", command=self.open_replace_dialog)
        
        self._find_next.grid(row=0, column=1, padx=(25,5), pady=10, sticky="nsew")
        self._search_button.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
        self._replace.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")
        self._input.grid(row=0, column=4, padx=(20,25), pady=10, ipady=1, sticky="nsew")

        self.grid_columnconfigure(4, weight=1)
        
        self._input.bind("<FocusIn>", lambda event: self.handle_focus_in())
        self._input.bind("<FocusOut>", lambda event: self.handle_focus_out())
        self._input.bind('<Return>', self.on_enter_pressed)

    def on_enter_pressed(self, event):
        self._search_button.invoke()  # Invokes the search_button click event

    def handle_focus_in(self):
        if self.get_entry == "3TSearch":
            self._input.delete(0, tk.END)
        self._input.config(foreground='green')

    def handle_focus_out(self):
        if len(self.get_entry) <= 0:
            self._input.delete(0, tk.END)
            self._input.insert(0, "3TSearch")
            self._input.config(foreground='gray')

    def open_replace_dialog(self):
        dialog = ReplaceDialog(self)

    @property
    def get_entry(self):
        return self._input.get()

    @property
    def find_next(self):
        return self._find_next

    @property
    def search_button(self):
        return self._search_button


# if __name__ == '__main__':
#     root = tk.Tk()
#     Search(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()
