## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018


from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):
    ## Creates a list of lists
    # @param values - a list variable from the private _openFile method
    #
    def __init__(self, values):
        self._newList = []

        for i in range(0, len(values), 5):
            self._newList.append(values[i: i + 5])


    def _determineColorValue(self, r, g, b):
        ## Creates a correctly formatted string for the dataForDisplay method
        # @param v - as pixel colour value
        # return - a hexadecimal string value
        #
        return ("#%02x%02x%02x" % (r, g, b))

    def getThreshold(self):
        ## Calculates a value for Entry widget
        # @return - a default value
        #
        vs = []

        for _,_,r,g,b in self._newList:
            vs+=[(r+g+b)/3]
        threshold = sum(vs)/len(vs)
        return int(threshold)

    def binariseImage(self, threshold):
        ## Converts each rgb colour value to a binary number
        # @param threshold - a suggested baseline value for threshold
        # @return - a BinaryImage object resulting from the threshold calculation
        binaryList = []
        for x, y, r, g, b in self._newList:
            binaryList.append((x, y, 0 if ((r+g+b)/3 < threshold) else 1))

        return BinaryImage(binaryList)

    def dataForDisplay(self):
        ## Converts list data into format that can be displayed
        # return data that will be passed as 'inputPts to the private _display() method
        #
        dataList = []
        for x, y, r, g, b in self._newList:
            dataList.append((x, y, self._determineColorValue(r, g, b)))
        return dataList