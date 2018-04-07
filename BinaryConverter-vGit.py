from tkinter import Frame, Canvas, Label, Button, Entry, Menu  #include more tkinter widgets here
from tkinter import filedialog

from GUIconnect import GUIconnect
from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage
from BinaryImage import BinaryImage


CANVAS_SIZE = 500  # Square region size used to display images

## GUI for binary image creator
class BinaryConverter(Frame, GUIconnect):
    """An image binarisation program to simplify/reduce the size of image files"""

    # constructor
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()  # use the grid manager
        self._addMenu()
        self._addProcessWidgets()

        # initialise variables
        self.text = ""
        self._imagedata = [GreyScaleImage, ColourImage]     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage.
                                                            # This will not change until a new data file is loaded.
        self._processedData = BinaryImage() # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

              
        self.master.title("Binary Image Creator")
        self.master.minsize(width=CANVAS_SIZE*2, height=CANVAS_SIZE)

        # Create canvas area
        self.canvasLeft = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg="#FFAAFF")
        self.canvasLeft.grid(row=1, column=0, columnspan=3)
        self.canvasRight = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg="#AAAAFF")
        self.canvasRight.grid(row=1, column=3, columnspan=3)







    # Methods for widgets available

    def _openFile(self):
        
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
        self.file_label.config(text=self.filename)

        """if self.filename != "":
            self.text = self._readFile(self.filename) 
            # Putting this here returns 'TypeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper'
            in the GreyScaleImage.py file  """
         

    def _readFile(self, filename):
        with open(filename, "r") as inFile:
            lines = inFile.readlines() #YES should this be readlines. Process here or in ??image.py file?
            if lines[0].strip() == "Greyscale Image":
                self._imagedata = GreyScaleImage(inFile)
                self._display(self.canvasLeft, self._imagedata.dataForDisplay())
            elif lines[0].strip() == "Colour Image":
                self._imagedata = ColourImage(inFile)
                self._display(self.canvasLeft, self._imagedata.dataForDisplay())
        self._display(self.canvasLeft, self._imagedata.dataForDisplay())


    def _addMenu(self):
        self.menubar = Menu(self)
        self.master["menu"] = self.menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Load", command = self._openFile)
        self.filemenu.add_command(label="Save")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=quit)


    def _addProcessWidgets(self):
        self.file_label = Label(text="No file selected yet")
        self.file_label.grid(row=0, column=0, columnspan=3)

        self.threshold_label = Label(text="Select Threshold (0-255)")
        self.threshold_label.grid(row=0, column=3, sticky="e")

        self.entry_area = Entry(self.master, width=5)
        self.entry_area.grid(row=0, column=4, sticky="e", padx=5)

        self.process_button = Button(self.master, text="Process", command=self.binariseImage)
        self.process_button.grid(row=0, column=5, sticky="w")

               
    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt      # x and y are both integers.
                              # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)
              

  
if __name__ == "__main__":
    BinaryConverter().mainloop()
