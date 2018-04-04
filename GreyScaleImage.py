from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

    def __init__(self, filename):
        self._data = []
        self.new_data = []

        with open(filename, "r") as inFile:
            values = inFile.readlines()  # Process here?
            if values[0].strip() != "GreyscaleImage":
                raise NotImplementedError("invalid input; image is not grey scale")

            for line in values[1:]:
                new_line = line.split(",")
                for each_item in new_line:
                    self._data.append(int(each_item))
        

    def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

    def getThreshold(self):
        for i in range(0, len(self.data), 3):
            self.new_data.append(self.data[i: i + 3])
            for v in self.new_data[_,_,v]:
                t = sum(self.new_data[v]/len(self.new_data))
        return t

    def binariseImage(self, threshold):
        pass
        # Your "Process" Button should call this method.
        # the "threshold" argument is the value extracted from the entry box in your GUI.
        # This method must return an object of type BinaryImage
        # return ???

    def dataForDisplay(self):
        for x, y, v in self.new_data:
            return x, y, self._determineColorValue(v)

        # This method returns the data in a form that can be displayed.
        # It will be passed as the parameter "inputPts" to the method _display() in the class BinaryConverter
        # return self._data ie: int(x), int(y), str(b)

