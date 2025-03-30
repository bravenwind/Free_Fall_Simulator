import tkinter as tk
import e_welcome

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('운동 비교 시스템')
        self.geometry('500x600')
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        welcome_page_frame = e_welcome.WelcomePage(self)
        welcome_page_frame.pack()

if __name__ == '__main__':
    app = App()

    app.mainloop()
