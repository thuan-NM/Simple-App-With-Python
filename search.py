import tkinter as tk
from tkinter import ttk


class Search(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        self._input = ttk.Entry(self)
        self._input.insert(0, "Regex")
        self._input.configure(foreground="gray")

        self._search_button = ttk.Button(self, text="Search")
        self._find_next = ttk.Button(self, text="Find next")

        self._input.grid(row=0, column=1, padx=55, pady=10, ipady=3, sticky="nsew")
        self._search_button.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
        self._find_next.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")

        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(4, weight=1)

        self._input.bind("<FocusIn>", lambda event: self.handle_focus_in())
        self._input.bind("<FocusOut>", lambda event: self.handle_focus_out())

    def handle_focus_in(self):
        if self.get_entry == "Regex":
            self._input.delete(0, tk.END)
        self._input.config(foreground='black')

    def handle_focus_out(self):
        if len(self.get_entry) <= 0:
            self._input.delete(0, tk.END)
            self._input.insert(0, "Regex")
            self._input.config(foreground='grey')

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
