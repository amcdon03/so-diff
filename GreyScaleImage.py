from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

    def __init__(self, filename):
        self._values = []
        self._newList = []

        with open(filename, "r") as inFile:
            lines = inFile.readlines()
            if lines[0].strip() != "GreyscaleImage":
                raise NotImplementedError("invalid input; image is not grey scale")

            for line in lines[1:]:
                itemList = line.split(",")
                for each_item in itemList:
                    self._values.append(int(each_item))
        

    def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

    def _getThreshold(self):
        for i in range(0, len(self._values), 3):
            self._newList.append(self._values[i: i+3])
            for v in self._newList[_, _, v]:
                threshold = sum(self._newList[v]/len(self._newList))
        return threshold

    def _binariseImage(self, threshold):
        pass
        # Your "Process" Button should call this method.
        # the "threshold" argument is the value extracted from the entry box in your GUI.
        # This method must return an object of type BinaryImage
        # return ???

    def _dataForDisplay(self):
        for x, y, v in self.values:
            return x, y, self._determineColorValue(v)

        # This method returns the data in a form that can be displayed.
        # It will be passed as the parameter "inputPts" to the method _display() in the class BinaryConverter
        # return self._data ie: int(x), int(y), str(b)

