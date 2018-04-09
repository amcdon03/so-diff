## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018

from tkinter import Frame, Canvas, Label, Button, Entry, Menu, IntVar, TclError
from tkinter import filedialog
from tkinter.messagebox import showerror

from GreyScaleImage import GreyScaleImage
from ColourImage import ColourImage


CANVAS_SIZE = 500  # Constant variable - value repeatedly used to identify canvas size

## GUI for binary image creator
class BinaryConverter(Frame):
    """An image binarisation program to simplify/reduce the size of image files"""

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self._addMenu()
        self._addProcessWidgets()

        # set the initial attibute values
        self.text = ""
        self._imagedata = None
        self._processedData = None
        self._pixelSize = 2

        # set up the container with size and title
        self.master.title("Binary Image Creator")
        self.master.minsize(width=CANVAS_SIZE*2, height=CANVAS_SIZE)

        # Create canvas area
        self.canvasLeft = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg="#FFAAFF")
        self.canvasLeft.grid(row=1, column=0, columnspan=3)
        self.canvasRight = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg="#AAAAFF")
        self.canvasRight.grid(row=1, column=3, columnspan=3)


    # Methods for widgets available

    ## Opens file. If file not present, raise error.
    def _openFile(self):
        try:
            values = []
            filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files","*.txt"),("All files","*.*")))
            self.file_label.config(text=filename)

            # Open appropriate text file as object for reading and transform into Python-ready list
            with open(filename, "r") as inFile:
                lines = inFile.readlines()

                for line in lines[1:]:
                    itemList = line.split(",")
                    for each_item in itemList:
                        values.append(int(each_item))

                if lines[0].strip() == "Greyscale Image":
                    self._imagedata = GreyScaleImage(values)
                elif lines[0].strip() == "Colour Image":
                    self._imagedata = ColourImage(values)

            # Call dataForDisplay and getThreshold methods on imagedata object
            # Display object and suggested transformation value
            self._display(self.canvasLeft, self._imagedata.dataForDisplay())
            self.threshValue.set(self._imagedata.getThreshold())
        except ValueError:
            showerror("Invalid input", "Please load comma deliminated document of the correct file type.")
        except:
            showerror("Ooops", "Oh fish! Something wasn't right! Please bear with us.")

    def _saveFile(self):
        try:
            filename = filedialog.asksaveasfilename(initialdir = "/", title="Please select a filename for saving:", filetypes=(("Text files", ".txt"),("All files", "*.*")), defaultextension=".txt")
            self._processedData.saveImage(filename)
        except:
            showerror("Ooops", "Oh fish! Something wasn't right! Please bear with us.")

    # Create menu bar with dropdown elements
    def _addMenu(self):
        self.menubar = Menu(self)
        self.master["menu"] = self.menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Load", command = self._openFile)
        self.filemenu.add_command(label="Save", command = self._saveFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=quit)

    # Create the event tools on the window
    def _addProcessWidgets(self):
        self.file_label = Label(text="No file selected yet")
        self.file_label.grid(row=0, column=0, columnspan=3)

        self.threshold_label = Label(text="Select Threshold (0-255)")
        self.threshold_label.grid(row=0, column=3, sticky="e")

        self.threshValue = IntVar()
        self.entry_area = Entry(self.master, width=5, textvariable=self.threshValue)
        self.entry_area.grid(row=0, column=4, sticky="e", padx=5)

        self.process_button = Button(self.master, text="Process", command=self._processImage)
        self.process_button.grid(row=0, column=5, sticky="w")

    def _processImage(self):
        try:
            self._processedData = self._imagedata.binariseImage(self.threshValue.get())
            self._display(self.canvasRight, self._processedData.dataForDisplay())
        except TclError:
            showerror("Invalid input", "Please enter a nunber (0-255) in the entry box")
        except AttributeError:
            showerror("Image not loaded", "Please load the image first.")
        except:
            showerror("Ooops", "Oh fish! Something wasn't right! Please bear with us.")


    def _display(self, canvas, inputPts): 
          s = self._pixelSize # renaming so that the last line of this method is shorter and easier to read
          for pt in inputPts:
              [x,y,v]=pt      # x and y are both integers.
                              # v is a string, which comes from the output of _determineColorValue
              canvas.create_rectangle(s*x, s*y, s*(x+1), s*(y+1), fill=v, width=0)
              

  
if __name__ == "__main__":
    BinaryConverter().mainloop()
