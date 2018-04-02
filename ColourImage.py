from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):

    def __init__(self, filename):
        self._data = int([])  ###convert to int() here??

        with open(filename, "r") as inFile:
            values = inFile.readlines() #Process here?
            if values[0].strip() != "ColourImage":
                raise NotImplementedError("invalid input; choices are binary, greyscale or colour")

            for items in values[1:]:
                new_line = values.split(",")
                for x in new_line:
                    self._data.append(x)

    def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))

    def getThreshold(self):
        pass
        # t = avg of all values (v) #intensity for the image
        ### convert to int() here??
        # return t

    def binariseImage(self, threshold):
        pass
        # Your "Process" Button should call this method.
        # the "threshold" argument is the value extracted from the entry box in your GUI.
        # This method must return an object of type BinaryImage
        # return ???

    def dataForDisplay(self):
        # This method returns the data in a form that can be displayed.
        # It will be passed as the parameter "inputPts" to the method _display() in the class BinaryConverter
        return self._data



 