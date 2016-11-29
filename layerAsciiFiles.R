## this script takes a series of ascii (or tif) files
## which represent presence data for species, and 
## collapses them with ascii math, giving you a raster
## where each box is the number of species present at that
## grid cell

library(sp)
library(maptools)
library(rgeos)
library(raster)
library(rworldmap)
library(RColorBrewer)

## import the rasters you want to add
path = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/"
outpath = "/Users/kprovost/Documents/PhylogeographyReview/WorkingMaps/"
dir = "NACorSACandCLEMandBIRD_NO"
setwd(path)
rast.names = dir(paste(path,dir,sep=""), pattern =".asc$",full.names=TRUE)
length(rast.names)

#print(rast.names)

## begin adding the rasters together
#full.rast=c()
for(i in 2:length(rast.names)){
  print(i)
  #print(rast.names[i])
  #full.rast = append(full.rast,paste(path,rast.names[i],sep=""))
  if(i == 2){
    r1 = raster(rast.names[1])
  } 
  r2 = raster(rast.names[i])
  mosSum = mosaic(r1,r2,fun=sum)
  r1 = mosSum
}

brks <- seq(0,30,by=0.3)
nbrks <- length(brks)-1

setwd(outpath)
writeRaster(mosSum,paste("COMBINED_",dir,".asc","sep"=""),"ascii",overwrite=TRUE)
  ## you will have to make sure this ascii is correct

cols = colorRampPalette(brewer.pal(nbrks,"Reds"))
# display.brewer.all()

mosSum2 = raster(paste("COMBINED_",dir,".asc","sep"=""))
#plot(mosSum2,col=topo.colors((nbrks)))
plot(mosSum2,col=cols(nbrks))