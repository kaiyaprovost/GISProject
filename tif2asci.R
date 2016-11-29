## Creator: K. L. Provost
## 11 Nov 2016
## This script changes geoTIFF into ASCII files

## import libraries
library(sp)
library(maptools)
library(rgeos)
library(raster)
library(rworldmap)
library(RColorBrewer)
library(dismo)
library(rgdal)
library(rJava)

## get all the tif names to convert
## change the path as needed
path = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/tempTif/"
outpath = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/tempAscii/"
setwd(path)
file.names = dir(path, pattern =".tif$")

## this for loop runs through each filename matching ".tif" 
## and changes them to a raster with the extent you 
#for(i in 1:10){
for(i in 6240:length(file.names)){
  print(c(i,file.names[i]))
  if(!file.exists(paste(outpath,file.names[i],".asc",sep=""))){
  tif = raster(file.names[i])
  #print("1") # for debugging
  ## below: outputs your raster - ends up with the filename ".tif_ASCII.asc"
  
    writeRaster(tif, filename=paste(outpath,file.names[i],".asc",sep=""),format='ascii',overwrite=TRUE)
  }
}
