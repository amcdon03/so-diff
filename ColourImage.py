from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class ColourImage(GUIconnect):
    
   def _determineColorValue(self,r,g,b):
        return ("#%02x%02x%02x" % (r,g,b))

 