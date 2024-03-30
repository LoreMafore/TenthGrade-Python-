from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.button_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(photo = image)
        label.image = photo
        label.pack()
        self.button1 = Button(self)
        self.button1["text"] = "Click me!!!!"
        self.button1["command"] = self.update_count
        self.button1.grid()

        def update_count(self):
            self.button_clicks += 1
            self.button["text"] = "Total clicks: "

root = Tk()
root.title("CP101 click counter")
root.geometry("400x400")

app = Application(root)

root.mainloop()
