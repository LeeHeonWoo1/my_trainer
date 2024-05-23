import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Application(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")
        self.title("My Trainer")
        self.geometry("1200x800")

        # Container to hold all frames
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="My Trainer")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="single class",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = ttk.Button(self, text="multi class",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="single class")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Go to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="multi class")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Go to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()