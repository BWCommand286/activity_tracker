
from threading import Thread
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow

LOGFILE = "./RM_log_class.txt"  # type: str


def currentTime():
    NOW = datetime.now()
    cTime = NOW.strftime("%Y:%m:%d:%H:%M:%S:%f")
    return cTime

def file_write(log):
    try:
        with open(LOGFILE, 'a') as f:
            log_text = currentTime() + "\t" + log
            #print(log_text)
            try:
                f.write(log_text+ "\n")
            except:
                log_text = currentTime() + "\t" + 'unknown'
                f.write(log_text+ "\n")
    except FileNotFoundError:
        print("File " + LOGFILE) 

def on_press(key):
    log = "Key pressed\t {0}".format(key)
    file_write(log)
    
        
def on_release(key):
    log = ("Key released\t {0}".format(key))
    file_write(log)

def on_move(x, y):
    log = ("Mouse moved to\t ({0}, {1})".format(x, y))
    file_write(log)

def on_click(x, y, button, pressed):
    if pressed:
        log = ('Mouse clicked at\t ({0}, {1}) with {2}'.format(x, y, button))
        file_write(log)
    else:
        log = ('Mouse released at\t ({0}, {1}) with {2}'.format(x, y, button))
        file_write(log)

def on_scroll(x, y, dx, dy):
    log = ('Mouse scrolled at\t ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    file_write(log)


def terminate_threads(*args):    
    for i in args:
        i.stop()
        
def start_threads(*args):
    for i in args:
        i.start()

class window_logger(Thread): 
      
    def __init__(self): 
        super().__init__()
        self._running = False
    
    def stop(self):
        if self._running:
            self._running = False

    def __enter__(self):
        self.start()
        self.wait()
        return self

    def __exit__(self, exc_type, value, traceback):
        self.stop()
            
    def run(self):
        self._running = True
        current_window = ''
        while self._running:
            if current_window  != GetWindowText(GetForegroundWindow()):
                #print(GetWindowText(GetForegroundWindow()))
                current_window  = GetWindowText(GetForegroundWindow())
                file_write('window'+'\t'+current_window)



