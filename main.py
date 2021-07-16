import tkinter as tk
from PIL import Image,  ImageTk

#


# create an instance
window = tk.Tk()
window.title('Time BUMP!')
window.config(padx=20,
              pady=20)


canvas = tk.Canvas(width=640,
                   height=480,
                   highlightthickness=0)
my_image = Image.open('images/bomb.png')
logo = ImageTk.PhotoImage(my_image.resize((500, 500))) 
canvas.create_image(320, 240, image=logo)
canvas.grid(column=1,
            row=1)


start_button = tk.Button(text='Start')
start_button.grid(column=0,
                  row=3)

stop_button = tk.Button(text='Pause')
stop_button.grid(column=2,
                  row=3)


bump_button = tk.Button(text='BUMP!')
bump_button.grid(column=1,
                 row=4)

window.mainloop()