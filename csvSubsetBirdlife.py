# -*- coding: utf-8 -*-
"""
Spyder Editor

This script pulls out birdlife files that match a CSV.
It also gets rid of ".shp_RASTER.tif" and changes it to ".tif"
"""

def main():
    import os
    import sys
    import glob
    from shutil import copyfile
    
    ## USAGE python ./csvSubsetBirdlife.py csvFile birdlifeDirectory

    #csvPath = os.getcwd() ## /Users/kprovost/Documents/PhylogeographyReview
    csvPath = "/Users/kprovost/Documents/PhylogeographyReview"
    print(csvPath)

    try:
        csvFile = sys.argv[1]
        print("\tSearching through ",csvFile)
    except:
        print("ERROR: CSV not given")
        csvFile = "/S2_Table_KLP_splitSpecies.csv" ## 
        #quit()
    try:
        rasterDir = sys.argv[2]
        print("\tDirectory name ",rasterDir)
    except:
        print("ERROR: Raster directory not given")
        rasterDir = "/WorkingMaps/NACorSACandCLEMandBIRD_YES/"
        #quit()    
    
    yesName = csvFile.split(".")[0]+"_YES"
    noName = csvFile.split(".")[0]+"_NO"

    if not os.path.isdir(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+yesName): 
        os.mkdir(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+yesName)
    if not os.path.isdir(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+noName):
        os.mkdir(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+noName)

    with open(csvPath+csvFile,"r") as csv:
        spp = csv.readlines()   
        
    sppDict = {}     
    for line in spp:
        line = line.strip().split(",")[0]
        sppDict[line] = 1
        
    #print(sppDict)
        
    #print("start")
    #print(csvPath+rasterDir+"*")
    for filename in glob.glob(csvPath+rasterDir+"*"):
        #print("\nfound")
        #print(filename[0:10])
        sppTemp = filename.split("/")[-1] ## working
        filetype = sppTemp.split(".")[-1] ## working
        prefix = sppTemp.split(".")[0]
        print("prefix\t",prefix)
        name = sppTemp.split("_")[0:2] ## working
        joinedName = "_".join(name) ## working
        #print("joined\t",joinedName)        
        species = prefix+"."+filetype ## working
        #print(prefix,yesName[1:],noName[1:])
        #print("spp\t",species)
        #if species != sppTemp:
            #print("\tmismatch")
        #print(csvPath+"/WorkingMaps"+yesName+"/"+species)
        
        #print("yesname\t",yesName)
        #print("noname\t",noName)
        
        if sppDict.get(joinedName,None) != None and prefix not in [yesName[1:],noName[1:]]:
            #print("###########YES")
            if not os.path.isfile(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+yesName+"/"+species):
                #print("copied")
                copyfile(filename,csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+yesName+"/"+sppTemp)
                pass
        elif prefix not in [yesName[1:],noName[1:]]:
            #print("NO")
            #pass
            if not os.path.isfile(csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+noName+"/"+species):
                copyfile(filename,csvPath+"/WorkingMaps/NACorSACandCLEMandBIRD_YES"+noName+"/"+sppTemp)
                #print("not copied")
                pass
            

if __name__ == "__main__":
    main()