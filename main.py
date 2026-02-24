import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Panda Village')
        self.master.geometry('800x600')
        self.master.configure(bg='lightblue')

        # Initialize wallpaper or background
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Start the event loop
        self.run_app()

    def run_app(self):
        self.master.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)