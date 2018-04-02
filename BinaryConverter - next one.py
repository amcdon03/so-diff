from tkinter import * #Tk, Frame, Canvas, Label, Button, Entry, Menu, Menubutton  #include more tkinter widgets here

from GUIconnect import GUIconnect

from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage
from BinaryImage import BinaryImage

from tkinter import filedialog

## GUI for binary image creator
class BinaryConverter(Frame, GUIconnect):
    
    CANVAS_SIZE = 500  # Square region size used to display images
    # constructor
    def __init__(self, master=None):
        super(BinaryConverter, self).__init__()

        Frame.__init__(self, master)
        self.grid()  # use the grid manager
        self._addMenu()
        self.text = ""
              
        self.master.title("Binary Image Creator")

        # Create canvas area
        self.canvasLeft=Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvasRight=Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE)

        self.canvasLeft.grid(row=3, column=0, columnspan=1)
        self.canvasRight.grid(row=3, column=1, columnspan=3)
        self._addProcessWidgets()

        self._imagedata = None     # Store here the loaded Image Data, i.e. an object of class GreyScaleImage or ColourImage. 
		                           # This will not change until a new data file is loaded.
        self._processedData = GUIconnect.BinaryImage() # Store here a BinaryImage object that is the result of binarising the loaded data.
        self._pixelSize = 2        # This is used to size the pixels in our display. See method _display()

    def _openFile(self):
        
        self.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
        self.label1.config(text=self.filename)  
         
        if self.filename != "":
            self.text = self.readFile(self.filename)
            #print(self.text)


    def readFile(self, filename):
        with open(filename, "r") as inFile:
            values = inFile.read()#should this be readlines to process one pixel at a time?
            #self.imagedata = values # then 
        return values


    def _chooseProcess(self):
        threshold = self.entry.get()
        if chosenProcess[0].upper() == "B":
            pass
        elif chosenProcess[0].upper() == "G":
            v=0
            GreyScaleImage._determineColorValue(self,v)
        elif chosenProcess[0].upper() == "C":
            self._showAsColour()
        else:
            print("invalid input; choices are binary, greyscale or colour")

    
    def _addMenu(self):
        self.menubar = Menu(self)
        self.master["menu"] = self.menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Load", command = self._openFile)
        self.filemenu.add_command(label="Save")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)



    def _addProcessWidgets(self):
        self.label1 = Label(text="No file selected yet")
        self.label2 = Label(text="Select Threshold (0-255)")
        self.entry = Entry(self, width=4)
        self.processBtn = Button(self.master, text="Process", command=GUIconnect.binariseImage(self, entry.get()))

        self.label1.grid(row=1, column=0)
        self.label2.grid(row=1, column=1)

        self.entry.grid(row=1, column=2)
        self.processBtn.grid(row=1, column=3)

               
    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt      # x and y are both integers.
                              # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)
              

  
if __name__ == "__main__":
    root = Tk()

    #testWindow = BinaryConverter(root)
    BinaryConverter().mainloop()
