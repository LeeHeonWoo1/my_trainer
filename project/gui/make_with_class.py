import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk

class MainApplication(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")  # 원하는 테마를 선택합니다.
        self.title("Machine Learning GUI")
        self.geometry("1400x800+280+100")

        self.container = ttk.Frame(self)
        for i in range(16):
            self.container.grid_rowconfigure(i, weight=1)
            self.container.grid_columnconfigure(i, weight=1)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (MainFrame, SingleInstanceFrame): # , MultiInstanceFrame, BuildYourOwnFrame, TransferLearningFrame
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            
        self.show_frame("MainFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.pack(expand=True, fill="both")
        frame.tkraise()

class MainFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ttk.Label(self, text="Main Screen", font=('Helvetica', 18, "bold"))
        label.grid(column=0, row=0, columnspan=16, pady=20)

        single_instance_button = ttk.Button(self, text="Single Instance",
                                            command=lambda: controller.show_frame("SingleInstanceFrame"))
        single_instance_button.grid(row=1, column=0, padx=10, pady=10, columnspan=8)

        multi_instance_button = ttk.Button(self, text="Multi Instances",
                                           command=lambda: controller.show_frame("MultiInstanceFrame"))
        multi_instance_button.grid(row=1, column=8, padx=10, pady=10, columnspan=8)

class SingleInstanceFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Single Instance", font=('Helvetica', 18, "bold"))
        label.grid(pady=10, padx=10, row=0, columnspan=16, column=0)

        byo_button = ttk.Button(self, text="Build Your Own",
                                command=lambda: controller.show_frame("BuildYourOwnFrame"))
        byo_button.grid(row=1, column=0, padx=10, pady=10, columnspan=5)

        transfer_learning_button = ttk.Button(self, text="Transfer Learning",
                                              command=lambda: controller.show_frame("TransferLearningFrame"))
        transfer_learning_button.grid(row=1, column=5, padx=10, pady=10, columnspan=5)

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        home_button.grid(row=1, column=10, padx=10, pady=10, columnspan=5)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()