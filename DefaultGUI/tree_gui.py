"""Module to visualize the TreeSet class using a Tkinter GUI."""

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox


class GUI(tk.Tk):
    """
    GUI class used to show a Tkinter window in order to
    visualize the TreeSet base Red - Black Tree.
    """

    def __tree_exists(function):
        def wrapper(self, *args, **kwargs):
            if self.__tree is None:
                self.__set_result("Tree not initialized!")
            else:
                return function(self, *args, **kwargs)

        return wrapper

    def __init__(self, tree=None):
        """
        Class constructor

        :param tree: The TreeSet object to be visualized.
        :type tree: TreeSet
        """
        super().__init__()
        self.title("TREESET")
        self.resizable(False, False)
        self.config(bg="#303030")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.__tree = tree
        self.fig, self.ax = plt.subplots()
        self.stop = True
        self.looked_size = 0
        self.type = None
        self.title_label = tk.Label(self, text="TREESET", bg="#303030",
                                    fg="white", font=('Arial', 16, 'bold'))
        self.title_label.pack(side="top", pady=10)

        style = ttk.Style()
        style.configure('TButton',
                        background='#f2f2f2',
                        foreground='#333',
                        font=('Arial', 10, 'bold'),
                        bordercolor="#333",
                        relief="solid",
                        borderwidth=1)

        style.map('TButton',
                  background=[('active', '#f2f2f2')],
                  foreground=[('active', '#333')],
                  relief=[('active', 'groove')],
                  bordercolor=[('active', '#333')],
                  borderwidth=[('active', 1)])

        main_frame = tk.Frame(self, bg="#303030")
        main_frame.pack(expand=True, fill="both")

        self.wait_time_slider = tk.Scale(self, from_=0.01, to=1,
                                         resolution=0.01, orient="horizontal",
                                         label="Wait Time (s)", bd=0)
        self.wait_time_slider.set(0.01)
        self.wait_time_slider.pack(side="top", fill="x")

        self.wait_time_slider.config(bg="#303030", fg="white",
                                     troughcolor="white", sliderlength=20,
                                     width=20, highlightbackground="#303030")

        self.value_label = tk.Label(main_frame, text="VALUE:", bg="#303030",
                                    fg="white", font=('Arial', 10, 'bold'))
        self.value_label.grid(row=0, column=0, padx=10, pady=10)

        self.result = tk.Label(main_frame, text="RESULT: ", bg="#303030",
                               fg="white", font=('Arial', 10, 'bold'))
        self.result.grid(row=3, column=0, padx=10, pady=10, columnspan=8,
                         sticky="ew")

        self.value_entry = tk.Entry(main_frame, width=15, font=('Arial', 10))
        self.value_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=5,
                              sticky="ew")

        self.type_label = tk.Label(main_frame, text="TREE-TYPE:", bg="#303030",
                                   fg="white", font=('Arial', 10, 'bold'))
        self.type_label.grid(row=0, column=6, padx=10, pady=10)

        self.objects = {"int": int, "str": str, "float": float}
        self.classes_combo = ttk.Combobox(
            main_frame, values=list(self.objects.keys()),
            state="readonly", width=10
        )
        self.classes_combo.grid(row=0, column=7, padx=10, pady=10)
        self.classes_combo.bind("<<ComboboxSelected>>", None)
        self.classes_combo.current(0)

        buttons = {"Add": None, "Remove": None,
                   "Clear": None, "Lower": None,
                   "Higher": None, "Ceiling": None,
                   "Floor": None,
                   "First": None, "Last": None,
                   "Poll First": None,
                   "Poll Last": None, "Size": None,
                   "Contains": None, "Test": None,
                   "Pause": None, "Stop": None,
                   "Show": None}

        self.button_widgets = dict()

        for i, text in enumerate(buttons):
            button = ttk.Button(main_frame, text=text, width=10,
                                command=lambda t=buttons[text]: t(),
                                style='TButton')
            button.grid(row=(i + 1) // 9 + 1, column=i % 8, padx=5, pady=5)
            self.button_widgets[text] = button

        self.button_widgets["Pause"].config(state="disabled")
        self.button_widgets["Stop"].config(state="disabled")
        self.update()

    def __on_close(self):
        if messagebox.askokcancel("Exit", "Do you want to close the window?"):
            print("The window is closing... executing cleaning labours.")
            self.test = False
            self.stop = True
            plt.close('all')
            self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
