from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):
        
   def _determineColorValue(self,v):
            return ("#%02x%02x%02x" % (v, v, v))

        
