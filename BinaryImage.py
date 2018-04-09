## Angelina McDonald, MSc IT T2CW2, Submission date: 9 April 2018


class BinaryImage:
    def __init__(self, binaryList):
        self._binaryList = binaryList

    def dataForDisplay(self):
        dataList = []
        for x, y, b in self._binaryList:
            dataList.append((x, y, self._determineColorValue(b)))
        return dataList

    def _determineColorValue(self, b):
        v = 255 * b
        return ("#%02x%02x%02x" % (v, v, v))


    def saveImage(self, filename):
        with open(filename, "w") as outFile:
            outFile.write("Binary Image\n")
            for x, y, b in self._binaryList:
                outFile.writelines((str(x), ",", str(y), ",", str(b),"\n"))
