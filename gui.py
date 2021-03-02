import tkinter
import RM_log_functions as rm
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

APPNAME="ProdLogger"

# create window
window = tkinter.Tk()
window.geometry("250x200")
# set window title
window.title(APPNAME)

#create logging objects
KL = KeyboardListener(on_press=rm.on_press, on_release=rm.on_release)
ML = MouseListener(on_move=rm.on_move, on_click=rm.on_click, on_scroll=rm.on_scroll)
WL = rm.window_logger()

#define button commands
start_logging = lambda: rm.start_threads(ML,KL,WL)
stop_logging = lambda: rm.terminate_threads(ML,KL,WL)

#button names and functions
start_button = tkinter.Button(window, text="Start", command=start_logging)
exit_button = tkinter.Button(window, text="Stop", command=stop_logging)

#start_button = tkinter.Button(window, text="Start")
#exit_button = tkinter.Button(window, text="Stop")

#button captions
start_button_label = tkinter.Label(window, text="Start logging")
exit_button_label = tkinter.Label(window, text="exit")

# put the components inside the window
start_button_label.pack()
start_button.pack()
exit_button_label.pack()
exit_button.pack()

# event loop, wait for user interaction
window.mainloop()