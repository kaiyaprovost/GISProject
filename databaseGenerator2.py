# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:31:26 2016

@author: kprovost
"""

def main():
    path = "/Users/kprovost/Dropbox/PhylogeographyReview/"
    dbDict = {}
    print("BEGIN ALL SPECIES READ")
    with open(path+"ALL_SPECIES_DATABASE.csv","r") as fullFile:
        for line in fullFile.readlines():
            dbDict[line.strip()] = ["0","0","0","0"]
    #print(dbDict)
    
    print("BEGIN CLEM READ")
    with open(path+"CLEMENTS_LISTONLY.csv","r") as clemfile:
        for clemLine in clemfile.readlines():
            get = dbDict.get(clemLine.strip())[0]
            if get == None:
                dbDict[clemLine.strip()][0] = "1"
            else:
                dbDict[clemLine.strip()][0] = "1"
    
    print("BEGIN NACC READ")            
    with open(path+"NACC_CSV_SHORTENED.csv","r") as naccfile:
        for naccLine in naccfile.readlines():
            get = dbDict.get(naccLine.strip())[1]
            if get == None:
                dbDict[naccLine.strip()][1] = "1"
            else:
                dbDict[naccLine.strip()][1] = "1"
     
    print("BEGIN SACC READ")           
    with open(path+"sac1sac2_MERGE_SHORTENED.csv","r") as saccfile:
        for saccLine in saccfile.readlines():
            get = dbDict.get(saccLine.strip())[2]
            if get == None:
                dbDict[saccLine.strip()][2] = "1"
            else:
                dbDict[saccLine.strip()][2] = "1"
 
    print("BEGIN BIRD READ")               
    with open(path+"birdlifeListRangeMaps.csv","r") as birdfile:
        for birdLine in birdfile.readlines():
            get = dbDict.get(birdLine.strip())[3]
            if get == None:
                dbDict[birdLine.strip()][3] = "1"
            else:
                dbDict[birdLine.strip()][3] = "1"

    print("BEGIN PRINTING DICT")
    with open(path+"SPECIES_ON_WHICH_LIST.csv","w") as outfile:
        outfile.write("SPECIES,CLEMENTS,NACC,SACC,BIRDLIFE\n")
        for i in dbDict:
            #outfile.write(str(i)+","+str(dbDict[i])+"\n")      
            temp = ",".join([i]+dbDict[i])
            outfile.write(str(temp)+"\n")
            ## 

    print("END")
if __name__ == "__main__":
    main()