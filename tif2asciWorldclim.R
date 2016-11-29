## Creator: K. L. Provost
## 19 Nov 2016
## This script changes geoTIFF into ASCII files
## specifically for WorldClim/LandSat (etc) data

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
path = "/Users/kprovost/Documents/Classes/GIS/Session4/Worldclim/"
outpath = "/Users/kprovost/Documents/PhylogeographyReview/EnvironmentalLayers/"
setwd(path)
file.names = dir(path, pattern =".tif$")

## this sets up a layer for clipping to the desired extent
ext =  extent (-180, 0, -90, 90) ## This extent is the Western Hemisphere
xy = abs(apply(as.matrix(bbox(ext)), 1, diff))
n = 1 ## this is how many cells are across your extent, so here it is 1 lat/long
r = raster(ext, ncol=xy[1]*n, nrow=xy[2]*n)

## this for loop runs through each filename matching ".tif" 
## and changes them to a raster with the extent you gave it
#for(i in 1:10){
for(i in 1:length(file.names)){
  print(c(i,file.names[i]))
  tif = raster(file.names[i])
  print(res(tif))
  print(ncol(tif))
  print(nrow(tif))
  #asc = projectRaster(tif,r)
  #print("1") # for debugging
  ## below: outputs your raster - ends up with the filename ".tif.asc"
  #writeRaster(asc, filename=paste(outpath,file.names[i],".asc",sep=""),format='ascii',overwrite=TRUE)
}
