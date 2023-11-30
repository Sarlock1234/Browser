import tkinter
import url

WIDTH, HEIGHT = 800, 600 #Setting width and height of the window

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()
    
    def load(self, url):
        self.canvas.create_rectangle(10, 20, 400, 300)
        self.canvas.create_oval(100, 100, 150, 150)
        self.canvas.create_text(200, 150, text="Hi!")
    



if __name__ == "__main__":
    import sys
    Browser().load(url.URL(sys.argv[1]))
    tkinter.mainloop()