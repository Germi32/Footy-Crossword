from tkinter import *

# Constantes
BG_COLOR = "#343541"

# Main
if __name__ == '__main__':
    # Main window
    root = Tk()
    root.title("Footy Crossword")
    root.geometry("854x480")
    root.state("zoomed")
    root.configure(background=BG_COLOR)
    # TODO: Make custom title bar
    # Title
    title = Frame(root, border=1)
    title_text = Label(title,
                       text="Footy Crossword",
                       background=BG_COLOR,
                       foreground="white",
                       font=("Helvetica", 32),
                       pady=50,
                       padx=50)

    title.pack(pady=(100, 0))
    title_text.pack()
    # Play button
    play = Frame(root, border=1)
    play_button = Button(play,
                         text="Play",
                         font=("Helvetica", 14))

    play.pack(side="bottom", pady=(0, 225))
    play_button.pack()
    # Loop
    root.mainloop()
