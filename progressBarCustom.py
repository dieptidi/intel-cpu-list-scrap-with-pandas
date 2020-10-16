import sys

class ProgressBarCustom:
    
    toolbar_width = 50
    
    def start(self):
        sys.stdout.write("[%s]" % (" " * self.toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))

    def progressBarAnimation(self):
        sys.stdout.write("-")
        sys.stdout.flush()
        
    def progressBarEnd(self):
        sys.stdout.write("]\n") # this ends the progress bar