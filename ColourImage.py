## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018


from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):

    def __init__(self, values):
        self._newList = []

        for i in range(0, len(values), 5):
            self._newList.append(values[i: i + 5])


    def _determineColorValue(self, r, g, b):
        return ("#%02x%02x%02x" % (r, g, b))

    def getThreshold(self):
        vs = []

        for _,_,r,g,b in self._newList:
            vs+=[(r+g+b)/3]
        threshold = sum(vs)/len(vs)
        return int(threshold)

    def binariseImage(self, threshold):
        binaryList = []
        for x, y, r, g, b in self._newList:
            binaryList.append((x, y, 0 if ((r+g+b)/3 < threshold) else 1))

        return BinaryImage(binaryList)

    def dataForDisplay(self):
        dataList = []
        for x, y, r, g, b in self._newList:
            dataList.append((x, y, self._determineColorValue(r, g, b)))
        return dataList