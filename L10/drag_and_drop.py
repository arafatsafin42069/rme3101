import tkinter as tk

class DragDropExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Drag and Drop Example")

        self.label = tk.Label(self, text="Drag me!")
        self.label.bind("<ButtonPress-1>", self.on_drag_start)
        self.label.bind("<B1-Motion>", self.on_drag_motion)
        self.label.bind("<ButtonRelease-1>", self.on_drag_release)
        self.label.pack()

    def on_drag_start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag_motion(self, event):
        x, y = self.label.winfo_x() + event.x - self.start_x, self.label.winfo_y() + event.y - self.start_y
        self.label.place(x=x, y=y)

    def on_drag_release(self, event):
        pass

if __name__ == "__main__":
    app = DragDropExample()
    app.mainloop()
