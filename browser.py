import tkinter
import url


SCROLL_STEP = 100
WIDTH, HEIGHT = 800, 600 #Setting width and height of the window
HSTEP, VSTEP = 13, 18 #Setting the wrap text height and width

def layout(text):
    display_list = []
    cursor_x, cursor_y = HSTEP, VSTEP
    for c in text:
        if c == r"\r\n":
            cursor_y += 2*VSTEP
            display_list.append((15,cursor_y , c))
        else:
            display_list.append((cursor_x, cursor_y, c))
        cursor_x += HSTEP
        if cursor_x >= WIDTH - HSTEP:
            cursor_y += VSTEP
            cursor_x = HSTEP
    return display_list
class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<Up>", self.scrollup)
    

    def draw(self):
        self.canvas.delete("all")
        for x,y,c in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y-self.scroll, text=c)
    
    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()
    
    def scrollup(self, q):
        self.scroll -= SCROLL_STEP
        self.draw()
    
    def load(self, ur):
        body = ur.request()
        text = url.lex(body)
        self.display_list = layout(text)
        self.draw()


    



if __name__ == "__main__":
    import sys
    Browser().load(url.URL(sys.argv[1]))
    tkinter.mainloop()