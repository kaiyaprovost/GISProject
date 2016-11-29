def main():
    import glob
    import os
    path = "/Users/kprovost/Documents/PhylogeographyReview/AllRangeMaps/All/"
    with open("birdlifeListRangeMaps_REDO.txt","w") as outfile:
        os.chdir(path)
        count = 0
        for filename in glob.glob("*.shp"):
            #print(filename)
            count += 1
            #filename = filename.replace("/","_")
            split = filename.replace("/","_").split("_")
            #print(split)
            #gen,spp = split[1],split[2]
            gen,spp = split[0],split[1]
            name = "_".join([gen,spp])
            outfile.write(str(name)+"\n")
        print(count," .shp files")

if __name__ == "__main__":
    main()