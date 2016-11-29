# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:50:03 2016

@author: kprovost
"""
def main(): 
    import os
    import glob
    from shutil import copyfile
    
    matchClem = "/Users/kprovost/Dropbox/Clements NACSAC/noam_matchesClem_17oct2016.csv"
    birdlifeFolder = "/Users/kprovost/Dropbox/BirdlifeRangeMaps/All/"
    newdirectoryFolder = "/Users/kprovost/Dropbox/BirdlifeRangeMaps/"
    
    
    with open(matchClem,"r") as matchFile:
        matchDict = {}
        lines = matchFile.readlines()
        for i in lines:
            split = i.split(",")
            engName,sciName = split[0],split[1]
            matchDict[sciName] = engName
    
    filelist = []
    print("files: ")
    for filename in glob.glob("*.shp"):
        #print(filename)
        filelist.append(filename[0:-4])

    if not os.path.exists(newdirectoryFolder+"onClem"):
        os.makedirs(newdirectoryFolder+"onClem")
    if not os.path.exists(newdirectoryFolder+"notClem"):
        os.makedirs(newdirectoryFolder+"notClem")
        
    for j in filelist:
        split = j.split("_")
        sci = "_".join(split[0:2])
        filesCopied = glob.glob(j+"*")
        #print(sci)
        if matchDict.get(sci,None) == None:
            with open(newdirectoryFolder+"notClemSpecies.txt","a") as notfile:
                notfile.write(sci+"\n")
            #print("NOT ",end="")
            for i in filesCopied:
                if not os.path.exists(newdirectoryFolder+"notClem/"+i):
                    copyfile(birdlifeFolder+i,newdirectoryFolder+"notClem/"+i)
        else:
            #print("MATCH ",end="")
            with open(newdirectoryFolder+"onClemSpecies.txt","a") as onfile:
                onfile.write(sci+"\n")
            for i in filesCopied:
                if not os.path.exists(newdirectoryFolder+"onClem/"+i):
                    copyfile(birdlifeFolder+i,newdirectoryFolder+"onClem/"+i)
                    
if __name__ == "__main__":
    main()