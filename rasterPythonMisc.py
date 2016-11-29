# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:33:39 2016

@author: kprovost
"""

def main():
    import scipy
    import gdal
    import sys
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    from PIL import Image
    
    #img=mpimg.imread("/Users/kprovost/Dropbox/PhylogeographyReview/WorkingMaps/NACorSACandCLEMandBIRD_YES/Sturnus_vulgaris_22710886_ONLYBREED.tif")
    im = Image.open("/Users/kprovost/Dropbox/PhylogeographyReview/WorkingMaps/NACorSACandCLEMandBIRD_YES/Sturnus_vulgaris_22710886_ONLYBREED.tif")    
    im.show()
    
if __name__ == "__main__":
    main()