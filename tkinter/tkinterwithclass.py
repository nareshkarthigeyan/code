import tkinter as tk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=("Roboto", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("monospace", 16)).pack(padx=10, pady=10)
        self.check_state = tk.IntVar()


        self.check = tk.Checkbutton(self.root, text="Show MessageBox", font=("Roboto", 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)



        self.root.mainloop

yGUI()