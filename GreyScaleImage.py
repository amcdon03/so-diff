from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

    def __init__(self, values):
        self._newList = []

        for i in range(0, len(values), 3):
            self._newList.append(values[i: i + 3])

        

    def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

    def getThreshold(self):
        vs = []

        for _,_,v in self._newList:
            vs+=[v]
        threshold = sum(vs)/len(vs)
        return int(threshold)

    def binariseImage(self, threshold):
        binaryList = []
        for x, y, v in self._newList:
            binaryList.append((x, y, 0 if (v < threshold) else 1))

        return
        # the "threshold" argument is the value extracted from the entry box in your GUI.
        # This method must return an object of type BinaryImage
        # return ???

    def dataForDisplay(self):
        dataList = []
        for x, y, v in self._newList:
            dataList.append((x, y, self._determineColorValue(v)))
        return dataList

        # This method returns the data in a form that can be displayed.
        # It will be passed as the parameter "inputPts" to the method _display() in the class BinaryConverter
        # return self._data ie: int(x), int(y), str(b)

