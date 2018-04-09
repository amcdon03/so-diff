## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018


class BinaryImage:
    """A binary image processing program"""

    def __init__(self, binaryList):
        ## Stores a list as an instance variable available throughout the class
        self._binaryList = binaryList

    def dataForDisplay(self):
        ## Converts list data into format that can be displayed
        # return data that will be passed as 'inputPts to the private _display() method
        #
        dataList = []
        for x, y, b in self._binaryList:
            dataList.append((x, y, self._determineColorValue(b)))
        return dataList

    def _determineColorValue(self, b):
        ## Creates a correctly formatted string for the dataForDisplay method
        # @param v - as pixel colour value
        # return - a hexadecimal string value
        #
        v = 255 * b
        return ("#%02x%02x%02x" % (v, v, v))


    def saveImage(self, filename):
        ## Creates a named image file object
        # @param filename - user defined filename from private _saveFile method
        #
        with open(filename, "w") as outFile:
            outFile.write("Binary Image\n")
            for x, y, b in self._binaryList:
                outFile.writelines((str(x), ",", str(y), ",", str(b), "\n"))
