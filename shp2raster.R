## Creator: K. L. Provost
## 17 Nov 2016
## This script changes shapefiles into raster files

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

## get all the shapefile names to convert
## change the path as needed
path = "/Users/kprovost/Documents/PhylogeographyReview/AllRangeMaps/onlyBreeding/"
outpath = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/tempTif/"
setwd(path)
file.names = dir(path, pattern =".shp$")

## this sets up a layer for clipping to the desired extent
ext =  extent (-180, 0, -90, 90) ## This extent is the Western Hemisphere
xy = abs(apply(as.matrix(bbox(ext)), 1, diff))
n = 1 ## this is how many cells are across your extent, so here it is 1 lat/long
r = raster(ext, ncol=xy[1]*n, nrow=xy[2]*n)
  ## add ,resolution- ## not sure why this is here

## FOR DEBUGGING ONLY
# Sturnus_vulgaris_22710886_ONLYBREED.shp
#match("Sturnus_vulgaris_22710886_ONLYBREED.shp",file.names)

# res() ## not sure why this is here

## NOTES FOR KAIYA PROJECT ##
#1487 Calidris ferruginea is being weird - skipped, will come back later
#10157 Todiramphus chloris - extent out of bounds? not sure - clipped in Q
  ## Added clipped file, so this became 10158
  ## on the redo, this became 9652 and 9653

## this for loop runs through each filename matching ".shp" 
## and changes them to a raster with the extent you define
#for(i in 1:10){
for(i in 9653:length(file.names)){
  print(c(i,file.names[i]))
  name=substr(file.names[i],1,-4)
  if(!file.exists(paste(outpath,file.names[i],".tif",sep=""))){
  #print(name)
  shp = readShapeSpatial(file.names[i],repair=TRUE)
  #print("1") # for debugging
  proj4string(shp) <- "+proj=longlat +datum=WGS84" ## sets up the projection
  #print("2") # for debugging
  rst = rasterize(shp,r) # converts .shp to raster with extent set up above
  #print("3") # for debugging
  
  ## below: outputs your raster - ends up with the filename ".shp_RASTER.tif"
  ## can also output as asc format by changing "format" and the ending
  
  writeRaster(rst, filename=paste(outpath,file.names[i],".tif",sep=""),format='GTiff',overwrite=TRUE)
  #writeRaster(rst, filename=paste(outpath,file.names[i],".asc",sep=""),format='ascii',overwrite=TRUE)
}}
