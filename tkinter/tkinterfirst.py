import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("notepad")

label = tk.Label(root, text="Hello, world!", font=('Arial', 12))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, width=100, font=('Arial', 12)).pack(padx=10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1").grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonFrame, text="2").grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonFrame, text="3").grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonFrame, text="4").grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonFrame, text="5").grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonFrame, text="6").grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x', padx=10)

root.mainloop() #This will keep it running

