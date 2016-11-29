
# -*- coding: utf-8 -*-
"""
Spyder Editor

This script changes ASCII files so that they all match a -9999 value
And also changes it so that all values are 1 instead of 1 or 2
"""

def main():
    import glob
    #asciiDir = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/NACorSACandCLEMandBIRD_NO/"  
    asciiDir = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/tempAscii/"  
    #asciiDir = "/Users/kprovost/Documents/Classes/GIS/Session1/ne_50m_admin_0_countries/"
    #asciiDir = "/Users/kprovost/Documents/PhylogeographyReview/EnvironmentalLayers/ne_110m_land/"
    ## -339999999999999996123846586046231871488.000000000000000
    ## -3.4e+38   
    
    print("start")
    for filename in glob.glob(asciiDir+"*.asc"):
        print(filename)
        infile = open(filename,"r")
        line = infile.read()
        print(line[0:100])
        line = line.replace("-339999999999999996123846586046231871488.000000000000000","-9999")
        line = line.replace("-3.4e+38","-9999")
        line = line.replace("2","1")
        print(line[0:100])
        infile.close()
        outfile = open(filename,"w")
        outfile.write(line)
        outfile.close()

if __name__ == "__main__":
    main()