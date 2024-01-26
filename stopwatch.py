import tkinter as tk

class Application(tk.Frame):
    """A class representing the stopwatch application."""

    def __init__(self, window=None):
        """Initialize the application with the main window."""
        super().__init__(window)
        self.window = window
        self.update_time = None
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """Create and pack the widgets."""
        self.stopwatch_label = tk.Label(self, text='00:00:00', font=('Arial', 80))
        self.stopwatch_label.pack()

        # Create buttons for start, pause, reset, and quit
        self.start_button = tk.Button(self, text='Start', height=2, width=6, font=('Arial', 20), command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self, text='Pause', height=2, width=6, font=('Arial', 20), command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self, text='Reset', height=2, width=6, font=('Arial', 20), command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(self, text='Quit', height=2, width=6, font=('Arial', 20), command=self.window.quit)
        self.quit_button.pack(side=tk.LEFT)

        self.window.title('Stopwatch')

    def start(self):
        """Start the stopwatch."""
        if not self.running:
            self.update()
            self.running = True

    def pause(self):
        """Pause the stopwatch."""
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False

    def reset(self):
        """Reset the stopwatch."""
        self.pause()
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.stopwatch_label.config(text='00:00:00')

    def update(self):
        """Update the stopwatch every second."""
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0

        time_string = f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
        self.stopwatch_label.config(text=time_string)
        self.update_time = self.stopwatch_label.after(1000, self.update)

# Create and run the application
root = tk.Tk()
app = Application(window=root)
app.mainloop()