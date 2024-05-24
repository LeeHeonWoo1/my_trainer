import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk

class MainApplication(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, theme="arc")  # 원하는 테마를 선택합니다.
        self.title("Machine Learning GUI")
        self.geometry("1400x800+280+100")

        self.container = ttk.Frame(self)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainFrame, SingleInstanceFrame, MultiInstanceFrame, BuildYourOwnFrame, TransferLearningFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ttk.Label(self, text="Main Screen", font=('Helvetica', 18, "bold"))
        label.grid(column=0, row=0, columnspan=4, pady=20, sticky="EW")

        single_instance_button = ttk.Button(self, text="Single Instance",
                                            command=lambda: controller.show_frame("SingleInstanceFrame"))
        single_instance_button.grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        multi_instance_button = ttk.Button(self, text="Multi Instances",
                                           command=lambda: controller.show_frame("MultiInstanceFrame"))
        multi_instance_button.grid(row=1, column=2, padx=10, pady=10, sticky="EW")

class SingleInstanceFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Single Instance Frame", font=('Helvetica', 18, "bold"))
        label.grid(pady=10, padx=10)

        byo_button = ttk.Button(self, text="Build Your Own",
                                command=lambda: controller.show_frame("BuildYourOwnFrame"))
        byo_button.grid()

        transfer_learning_button = ttk.Button(self, text="Transfer Learning",
                                              command=lambda: controller.show_frame("TransferLearningFrame"))
        transfer_learning_button.grid()

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        home_button.grid()

class MultiInstanceFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Multi Instances", font=('Helvetica', 18, "bold"))
        label.grid(pady=10, padx=10)

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        home_button.grid()

class BuildYourOwnFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Build Your Own CNN", font=('Helvetica', 18, "bold"))
        label.grid(pady=10, padx=10)

        # Placeholder for CNN building functionality
        add_conv_block_button = ttk.Button(self, text="Add Convolutional Block")
        add_conv_block_button.grid()

        # Image folder selection
        self.image_folder_path = tk.StringVar()
        select_folder_button = ttk.Button(self, text="Select Image Folder",
                                          command=self.select_image_folder)
        select_folder_button.grid()
        folder_label = ttk.Label(self, textvariable=self.image_folder_path)
        folder_label.grid()

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        home_button.grid()

    def select_image_folder(self):
        folder_path = filedialog.askdirectory()
        self.image_folder_path.set(folder_path)

class TransferLearningFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Transfer Learning", font=('Helvetica', 18, "bold"))
        label.grid(pady=10, padx=10)

        # Placeholder for transfer learning functionality
        model_selection_label = ttk.Label(self, text="Select Transfer Learning Model")
        model_selection_label.grid()

        self.model_var = tk.StringVar()
        model_selection = ttk.Combobox(self, textvariable=self.model_var)
        model_selection['values'] = ('VGG16', 'ResNet50', 'InceptionV3')
        model_selection.grid()

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        home_button.grid()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()