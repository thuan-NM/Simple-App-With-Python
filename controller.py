import tkinter as tk
from tkinter import messagebox

from search import Search
from custom_text import CustomText
from replace import ReplaceDialog


class Controller(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._parent = parent

        self._text_widget = CustomText(self)
        self._search = Search(self)

        self._search.pack(side="top", fill="x")
        self._text_widget.pack(side="top", fill="both", expand=True)

        self._search.search_button.configure(command=self.highlight_text)
        self._search.find_next.configure(command=self.find_next)
        self._search._replace.configure(command=self.replace_text)


    def highlight_text(self):
        pattern = self._search.get_entry
        all_matches = self._text_widget.highlight_match(pattern)

        if len(all_matches) == 0:
            messagebox.showinfo("showinfo", f"There are no matches in the entire file.")
        elif len(all_matches) == 1:
            messagebox.showinfo("showinfo", f"There is 1 match in the entire file.")
        else:
            messagebox.showinfo("showinfo", f"There are {len(all_matches)} matches in the entire file.")

        self._text_widget.text_area.clean_all_tag("match")

    def replace_text(self):
        dialog = ReplaceDialog(self)
        find_text = dialog.find_text
        replace_text = dialog.replace_text
        if find_text and replace_text:
            self._text_widget.text_area.replace_all(find_text, replace_text)
        else:
            messagebox.showinfo("showinfo", f"Please fill the form first!!!")

    def find_next(self):
        pattern = self._search.get_entry

        if pattern is None or pattern == "":
            messagebox.showinfo("showinfo", f"There are no matches in the entire file.")

        cursor_pos = self._text_widget.text_area.index(tk.INSERT)

        next_match = self._text_widget.text_area.next_match(cursor_pos, pattern)

        if next_match is None:
            self._text_widget.text_area.clean_all_tag("match")
            messagebox.showinfo("showinfo", f"There are no matches in the entire file.")
            return

        match_start = next_match[0]
        match_end = next_match[1]

        self._text_widget.text_area.see(match_end)

        self._text_widget.text_area.focus_set()
        self._text_widget.text_area.tag_remove("match", match_start, match_end)

        self._text_widget.text_area.clean_all_tag("sel")
        self._text_widget.text_area.tag_add('sel', match_start, match_end)
        self._text_widget.text_area.mark_set(tk.INSERT, match_end)

        self._text_widget.highlight_match(pattern)

    @property
    def text_widget(self):
        return self._text_widget

    @property
    def search(self):
        return self._search

# if __name__ == "__main__":
#     root = tk.Tk()
#     Controller(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()
