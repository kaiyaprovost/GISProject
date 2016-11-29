# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:21:11 2016

@author: kprovost
"""

def main():
    import os
    import glob
    import dbf

    folder = "/Users/kprovost/Dropbox/BirdlifeRangeMaps/"    
    dbfFolder = "/Users/kprovost/Downloads/Promeropidae/"
    
    count = 0    
    
    with open(folder+"/compileDBF.temp","a") as compDbf:        
        for filename in glob.glob(dbfFolder+"*.dbf"):
            #print(filename)
            print(filename)
            dBase = dbf.Table(filename)
            dbf.export(dBase,folder+"/compileDBF.temp",header=True)
            with open(folder+"/compileDBF.temp","w") as tempDbf:
                output = tempDbf.read()
                compDbf.write(output)
        
    print("done")
    
    
    
    
#        with open(filename,"r") as file:
#            with open(folder+"/compileDBF.txt","a") as compDbf:
#                output = file.read()                
#                compDbf.write(output)
#                count += 1
#                if count // 1000 == 0:
#                    print(count,sep=" ")
                    
if __name__ == "__main__":
    main()
    

        
        