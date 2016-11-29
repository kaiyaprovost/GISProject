library(maptools)
library(rgeos)

path = "/Users/kprovost/Documents/PhylogeographyReview/AllRangeMaps/All/"
outDir = "/Users/kprovost/Documents/PhylogeographyReview/AllRangeMaps/onlyBreeding/"
#setwd(path)
file.names = dir(path, pattern =".shp")
print(file.names[1])

## SKIPPED BECAUSE WEIRD OR NO BREEDING
  ## Acrosephalus sorghophilis 112
  ## Calidris ferruginea 1390 -- DID MANUALLY
  ## Caprimulgus centralasicus 1537
  ## Hirundo perdita 4363
  ## Setopagis maculosa 8839

#for (i in 1:10){
for (i in 8840:length(file.names)){
  print(i)
  nameOnly = substring(file.names[i],1,nchar(file.names[i])-4)
  print(nameOnly)
  stringShp = paste(path,file.names[i],sep="")
  newString = paste(outDir,nameOnly,"_ONLYBREED",sep="") ## leave off the filename for writeShapefile
  #print(stringShp)
  
  if(file.exists(paste(newString,".shp",sep=""))){
    print(">>>exists")
  } else {
    ## import the shapefile
    shp = readShapeSpatial(stringShp,repair=TRUE)
    print(summary(shp@data$SEASONAL))
    
    ## remove the data from the shapefile when its season is 3-5
    
    shp = shp[shp@data$SEASONAL!=3,]
    #print(summary(shp@data$SEASONAL))
    
    shp = shp[shp@data$SEASONAL!=4,]
    #print(summary(shp@data$SEASONAL))
    
    shp = shp[shp@data$SEASONAL!=5,]
    #print(summary(shp@data$SEASONAL))
    
    #print(shp@data$SEASONAL)
    #plot(shp)
    
    ## export the shapefile
    writeSpatialShape(shp,newString)
  }
}

## NOTES FROM PREV RUN ##


## 516 DID NOT WORK CANNOT FIGURE OUT WHY - DID MANUALLY IN Q
## 3376 IS KNOWN BY ONLY ONE SPECIMEN - EXCLUDED


## Ones with no breeding or resident ranges:
## 109: "Acrocephalus_sorghophilus_22714704", only "3" listed, skipped
## 262: "Aimophila_notosticta_pl", empty?
## 1635 "Caprimulgus_centralasicus_22689909" only 5
## 4610 subscript oob "Hirundo_perdita_22712390" only 5
## 7274 Periporphyrus_erythromelas_pl - empry?
## 9242 setopagis maculosa 5 only

## Other issues:
## 1483: Brian's conflicted copy, skipped
## 10177 - Todiramphus recurvirostris, no dbf file, skipped b/c Asian bird

