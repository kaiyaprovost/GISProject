# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:21:42 2016

@author: kprovost
"""

def main():  
    import copy
    workingDirectory = "/Users/kprovost/Documents/PhylogeographyReview/"
    with open(workingDirectory+"birdlifeListRangeMaps_REDO.txt","r",newline=None) as birdsFile,open(workingDirectory+"SPECIES_ON_WHICH_LIST_FORCHECK.csv","r",newline=None) as checkFile:
    #with open(workingDirectory+"birdsTEST.csv","r",newline=None) as birdsFile,open(workingDirectory+"checkTEST.csv","r",newline=None) as checkFile:
        
        birdsLines = birdsFile.readlines()
        checkLines = checkFile.readlines()
        print(birdsLines[1],checkLines[1])
        
    #print(birdsLines[112])
        
    checkDict = {}
    
    for i in range(len(checkLines)):
        spp,info = checkLines[i].split(",",1)
        checkDict[spp] = info.strip()
        
    print(len(checkDict))

    with open(workingDirectory+"both_birdscheck.csv","w") as onBoth, open(workingDirectory+"birds_birdscheck.csv","w") as onBird,open(workingDirectory+"check_birdscheck.csv","w") as onCheck:
        for j in range(len(birdsLines)):
            print(birdsLines[j])
            bird = birdsLines[j].strip()
            check = checkDict.get(bird,False)
            if check != False:
                print("onBoth")
                onBoth.write(bird+"\n")
                del checkDict[bird]
            elif check == False:
                print("onlyBird")
                onBird.write(bird+"\n")
            else:
                print("SOMETHING WENT WRONG")
            
        for key in checkDict:
            print(key,checkDict[key])
            print("onlyCheck")
            onCheck.write(key+"\n")
        
        
if __name__ == "__main__":
    main()