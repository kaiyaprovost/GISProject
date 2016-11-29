#!/bin/sh

for n in *.shp_RASTER.tif; do
	echo mv $n $(echo $n | sed -e 's/.tif//')
done