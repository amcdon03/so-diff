## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018


from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):
    ## Creates a list of lists
    # @param values - a list variable from the private _openFile method
    #
    def __init__(self, values):
        self._newList = []  # instance variable available elsewhere within the class

        for i in range(0, len(values), 3):
            self._newList.append(values[i: i + 3])


    def _determineColorValue(self,v):
        ## Creates a correctly formatted string for dataForDisplay method
        # @param v - as pixel colour value
        # return - a hexadecimal string value
        #
            return ("#%02x%02x%02x" % (v, v, v))

    def getThreshold(self):
        ## Calculates a value for Entry widget
        # @return - a default value
        #
        vs = []   # local variable

        # Selects third item of each tuple in list
        for _,_,v in self._newList:
            vs += [v]
        threshold = sum(vs)/len(vs)
        return int(threshold)

    def binariseImage(self, threshold):
        ## Converts each colour tone value to a binary number
        # @param threshold - a suggested baseline value for threshold
        # @return - a BinaryImage object resulting from the threshold calculation
        binaryList = []
        for x, y, v in self._newList:
            binaryList.append((x, y, 0 if (v < threshold) else 1))  #if-else statement on one line
        return BinaryImage(binaryList)


    def dataForDisplay(self):
        ## Converts list data into format that can be displayed
        # return data that will be passed as 'inputPts to the private _display() method
        #
        dataList = []
        for x, y, v in self._newList:
            dataList.append((x, y, self._determineColorValue(v)))
        return dataList


