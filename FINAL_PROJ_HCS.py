import rioxarray as rxr
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy
from shapely.geometry import mapping

def plotter(plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year, county):
    #plot = plt
    #fig = plot.figure()
    #xs = ['2009']
    #corn = []
    #soybeans = []
    #grassland = []
    fig.clear()
    developedcount = 0;
    for x in range(len(unique)):
        
        if unique[x] == 1:
            corn.append(counts[x])
        if unique[x] == 5:
            soybeans.append(counts[x])
        if unique[x] == 176:
            grassland.append(counts[x])
        if unique[x]== 121 or unique[x] == 122 or unique[x] == 123 or unique[x] == 124:
            developedcount += counts[x]
    developed.append(developedcount)
    print(developedcount)
        

    plot.plot(xs, corn, label="Corn")
    plot.plot(xs, soybeans, label="Soybeans")
    plot.plot(xs, grassland, label="Grassland")
    plot.plot(xs, developed, label="Developed")
    plot.title("Crops Over 16 Years in " + county)
    plot.xlabel("Year")
    plot.ylabel("Amount (millions)")
    plot.legend(loc=(1.04, 0.8))
    plot.subplots_adjust(right=0.75)
    plot.gcf().set_size_inches(10, 6)
    plot.draw()
    plt.show()
    year += 4
    xs.append(str(year))
    return plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year

filepath2020 = 'C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2020_clip_20211207232419_873250894.tif'
filepath2016 = 'C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2016_clip_20211207232419_873250894.tif'
filepath2012 = 'C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2012_clip_20211207232419_873250894.tif'
filepath2008 = 'C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2008_clip_20211207232419_873250894.tif'
filepath2004 ='C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\polygonclip\\CDL_2004_clip_20211207232419_873250894.tif'


data2020 = rxr.open_rasterio(filepath2020, masked=True).squeeze()
data2016 = rxr.open_rasterio(filepath2016, masked=True).squeeze()
data2012 = rxr.open_rasterio(filepath2012, masked=True).squeeze()
data2008 = rxr.open_rasterio(filepath2008, masked=True).squeeze()
data2004 = rxr.open_rasterio(filepath2004, masked=True).squeeze()

# PLOTTING ENTIRE TIF FILE

f, ax = plt.subplots(figsize=(10, 5))
data2020.plot.imshow()
ax.set(title="Original Tif File ")
ax.set_axis_off()
plt.show()

# GRABBING EACH COUNTY FROM ENTIRE SHAPE FILE

counties_gdf = gpd.read_file('C:\\Users\\kevin\\OneDrive\\Documents\\CSC_486_DataMiningMethods\\DataMiningProject3Folder\\cb_2018_us_county_5m\\cb_2018_us_county_5m.shp')
Iowacountiesgdf = counties_gdf[counties_gdf['STATEFP'] == '19']
BHgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Black Hawk']
Butlergdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Butler']
Frankgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Franklin']
Carrollgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Carroll']
Webgdf = Iowacountiesgdf[Iowacountiesgdf['NAME'] == 'Webster']

################CUTTING OUT EACH COUNTY FOR 2020######################


# CLIPPING BLACK HAWK COUNTY

BlackHawkclipped20 = data2020.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)
BlackHawkclipped16 = data2016.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)
BlackHawkclipped12 = data2012.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)
BlackHawkclipped8 = data2008.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)
BlackHawkclipped4 = data2004.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)

f, ax = plt.subplots(figsize=(10, 4))
BlackHawkclipped20.plot(ax=ax)
ax.set(title="County of BlackHawk TIF")
ax.set_axis_off()
plt.show()

# CLIPPING BUTLER COUNTY

Butlerclipped20 = data2020.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)
Butlerclipped16 = data2016.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)
Butlerclipped12 = data2012.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)
Butlerclipped8 = data2008.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)
Butlerclipped4 = data2004.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)

f, ax = plt.subplots(figsize=(10, 4))

Butlerclipped20.plot(ax=ax)

ax.set(title="County of Butler TIF")

ax.set_axis_off()

plt.show()

# CLIPPING FRANK COUNTY

Frankclipped20 = data2020.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)
Frankclipped16 = data2016.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)
Frankclipped12 = data2012.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)
Frankclipped8 = data2008.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)
Frankclipped4 = data2004.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)


f, ax = plt.subplots(figsize=(10, 4))

Frankclipped20.plot(ax=ax)

ax.set(title="County of Frank TIF")

ax.set_axis_off()

plt.show()

# CLIPPING CARROLL COUNTY

Carrollclipped20 = data2020.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)
Carrollclipped16 = data2016.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)
Carrollclipped12 = data2012.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)
Carrollclipped8 = data2008.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)
Carrollclipped4 = data2004.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)

f, ax = plt.subplots(figsize=(10, 4))

Carrollclipped20.plot(ax=ax)

ax.set(title="County of Carroll TIF")

ax.set_axis_off()

plt.show()

# CLIPPING WEBSTER COUNTY
Websterclipped = data2020.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)
f, ax = plt.subplots(figsize=(10, 4))

Websterclipped.plot(ax=ax)

ax.set(title="County of Carroll TIF")

ax.set_axis_off()

plt.show()


################CUTTING OUT EACH COUNTY FOR 2020######################


# CLIPPING BLACK HAWK COUNTY
BlackHawkclipped = data2020.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)

# CLIPPING BUTLER COUNTY
Butlerclipped = data2020.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)

# CLIPPING FRANK COUNTY
Frankclipped = data2020.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)


# CLIPPING CARROLL COUNTY
Carrollclipped = data2020.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)



# CLIPPING WEBSTER COUNTY
Websterclipped = data2020.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)

######################## COMPUTING LAND USAGE FOR COUNTIES ####################

blackhawk = []
butler = []
frank = []
carroll = []
webster = []

# COMPUTING LANDUSAGE FOR BLACKHAWK COUNTY IN 2020

BlackHawkdf = BlackHawkclipped.to_numpy()

(unique, counts) = numpy.unique(BlackHawkdf, return_counts=True)
blackhawk.append((unique, counts))

count = numpy.asarray((unique, counts)).T

BHdf2020 = pd.DataFrame(data=count, columns=['value', 'Count'])

BHlandusage_df = BHdf2020[BHdf2020['Count'] > 10000]

# ax = BHlandusage_df.plot.bar(x = 'value', y = 'Count')


# COMPUTING LANDUSAGE FOR BUTLER COUNTY IN 2020

Butlerdf = Butlerclipped.to_numpy()

(unique, counts) = numpy.unique(Butlerdf, return_counts=True)
butler.append((unique, counts))



# ax = Butlerlandusage_df.plot.bar(x = 'value', y = 'Count')


# COMPUTING LANDUSAGE FOR FRANK COUNTY IN 2020

Frankdf = Frankclipped.to_numpy()
(unique, counts) = numpy.unique(Frankdf, return_counts=True)
frank.append((unique, counts))


# ax = Franklandusage_df.plot.bar(x = 'value', y = 'Count')


# COMPUTING LANDUSAGE FOR CARROLL COUNTY IN 2020

Carrolldf = Carrollclipped.to_numpy()
(unique, counts) = numpy.unique(Carrolldf, return_counts=True)
carroll.append((unique, counts))

# ax = Carrollandusage_df.plot.bar(x = 'value', y = 'Count')


# COMPUTING LANDUSAGE FOR WEBSTER COUNTY IN 2020
Websterdf = Websterclipped.to_numpy()
(unique, counts) = numpy.unique(Websterdf, return_counts=True)
webster.append((unique, counts))


###################### CLIPPING COUNTIES ON 2016 TIF #########################

# CLIPPING BLACK HAWK COUNTY
BlackHawkclipped2016 = data2016.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)

# CLIPPING BUTLER COUNTY
Butlerclipped2016 = data2016.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)

# CLIPPING FRANK COUNTY
Frankclipped2016 = data2016.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)

# CLIPPING CARROLL COUNTY
Carrollclipped2016 = data2016.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)

# CLIPPING WEBSTER COUNTY
Websterclipped2016 = data2016.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)

###########GETTING LANDUSAGE FOR ALL COUNTIES 2016 ##########################

BlackHawkdf2016 = BlackHawkclipped2016.to_numpy()
(unique, counts) = numpy.unique(BlackHawkdf2016, return_counts=True)
blackhawk.append((unique, counts))

Butlerdf2016 = Butlerclipped2016.to_numpy()
(unique, counts) = numpy.unique(Butlerdf2016, return_counts=True)
butler.append((unique, counts))

Frankdf2016 = Frankclipped2016.to_numpy()
(unique, counts) = numpy.unique(Frankdf2016, return_counts=True)
frank.append((unique, counts))

Carrolldf2016 = Carrollclipped2016.to_numpy()
(unique, counts) = numpy.unique(Carrolldf2016, return_counts=True)
carroll.append((unique, counts))

Websterdf2016 = Websterclipped2016.to_numpy()
(unique, counts) = numpy.unique(Websterdf2016, return_counts=True)
webster.append((unique, counts))

###################### CLIPPING COUNTIES ON 2012 TIF #########################

# CLIPPING BLACK HAWK COUNTY
BlackHawkclipped2012 = data2012.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)

# CLIPPING BUTLER COUNTY
Butlerclipped2012 = data2012.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)

# CLIPPING FRANK COUNTY
Frankclipped2012 = data2012.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)

# CLIPPING CARROLL COUNTY
Carrollclipped2012 = data2012.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)

# CLIPPING WEBSTER COUNTY
Websterclipped2012 = data2012.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)

###########GETTING LANDUSAGE FOR ALL COUNTIES 2012 ##########################

BlackHawkdf2012 = BlackHawkclipped2012.to_numpy()
(unique, counts) = numpy.unique(BlackHawkdf2012, return_counts=True)
blackhawk.append((unique, counts))

Butlerdf2012 = Butlerclipped2012.to_numpy()
(unique, counts) = numpy.unique(Butlerdf2012, return_counts=True)
butler.append((unique, counts))

Frankdf2012 = Frankclipped2012.to_numpy()
(unique, counts) = numpy.unique(Frankdf2012, return_counts=True)
frank.append((unique, counts))

Carrolldf2012 = Carrollclipped2012.to_numpy()
(unique, counts) = numpy.unique(Carrolldf2012, return_counts=True)
carroll.append((unique, counts))

Websterdf2012 = Websterclipped2012.to_numpy()
(unique, counts) = numpy.unique(Websterdf2012, return_counts=True)
webster.append((unique, counts))

###################### CLIPPING COUNTIES ON 2008 TIF #########################

# CLIPPING BLACK HAWK COUNTY
BlackHawkclipped2008 = data2008.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)

# CLIPPING BUTLER COUNTY
Butlerclipped2008 = data2008.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)

# CLIPPING FRANK COUNTY
Frankclipped2008 = data2008.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)

# CLIPPING CARROLL COUNTY
Carrollclipped2008 = data2008.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)
# CLIPPING WEBSTER COUNTY
Websterclipped2008 = data2008.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)

###########GETTING LANDUSAGE FOR ALL COUNTIES 2008 ##########################

BlackHawkdf2008 = BlackHawkclipped2008.to_numpy()
(unique, counts) = numpy.unique(BlackHawkdf2008, return_counts=True)
blackhawk.append((unique, counts))

Butlerdf2008 = Butlerclipped2008.to_numpy()
(unique, counts) = numpy.unique(Butlerdf2008, return_counts=True)
butler.append((unique, counts))

Frankdf2008 = Frankclipped2008.to_numpy()
(unique, counts) = numpy.unique(Frankdf2008, return_counts=True)
frank.append((unique, counts))

Carrolldf2008 = Carrollclipped2008.to_numpy()
(unique, counts) = numpy.unique(Carrolldf2008, return_counts=True)
carroll.append((unique, counts))

Websterdf2008 = Websterclipped2008.to_numpy()
(unique, counts) = numpy.unique(Websterdf2008, return_counts=True)
webster.append((unique, counts))

###################### CLIPPING COUNTIES ON 2004 TIF #########################
# CLIPPING BLACK HAWK COUNTY
BlackHawkclipped2004 = data2004.rio.clip(BHgdf.geometry.apply(mapping), BHgdf.crs)
# CLIPPING BUTLER COUNTY
Butlerclipped2004 = data2004.rio.clip(Butlergdf.geometry.apply(mapping), Butlergdf.crs)
# CLIPPING FRANK COUNTY
Frankclipped2004 = data2004.rio.clip(Frankgdf.geometry.apply(mapping), Frankgdf.crs)
# CLIPPING CARROLL COUNTY
Carrollclipped2004 = data2004.rio.clip(Carrollgdf.geometry.apply(mapping), Carrollgdf.crs)

# CLIPPING WEBSTER COUNTY
Websterclipped2004 = data2004.rio.clip(Webgdf.geometry.apply(mapping), Webgdf.crs)

###########GETTING LANDUSAGE FOR ALL COUNTIES 2004 ##########################

BlackHawkdf2004 = BlackHawkclipped2004.to_numpy()
(unique, counts) = numpy.unique(BlackHawkdf2004, return_counts=True)
blackhawk.append((unique, counts))

Butlerdf2004 = Butlerclipped2004.to_numpy()
(unique, counts) = numpy.unique(Butlerdf2004, return_counts=True)
butler.append((unique, counts))

Frankdf2004 = Frankclipped2004.to_numpy()
(unique, counts) = numpy.unique(Frankdf2004, return_counts=True)
frank.append((unique, counts))

Carrolldf2004 = Carrollclipped2004.to_numpy()
(unique, counts) = numpy.unique(Carrolldf2004, return_counts=True)
carroll.append((unique, counts))

Websterdf2004 = Websterclipped2004.to_numpy()
webster.append((unique, counts))
(unique, counts) = numpy.unique(Websterdf2004, return_counts=True)

webster.reverse()
frank.reverse()
carroll.reverse()
blackhawk.reverse()
butler.reverse()

plot = plt
fig = plot.figure()
year = 2004
xs = [str(year)]
corn = []
soybeans = []
grassland = []
developed = []
for x in range(len(blackhawk)):
    plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year = plotter(plot, fig, blackhawk[x][0], blackhawk[x][1], corn, soybeans, grassland, developed, xs, year, "Blackhawk")

plot = plt
fig = plot.figure()
year = 2004
xs = [str(year)]
corn = []
soybeans = []
grassland = []
developed = []
for x in range(len(butler)):
    plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year = plotter(plot, fig, butler[x][0], butler[x][1], corn, soybeans, grassland, developed, xs, year, "Butler")

plot = plt
fig = plot.figure()
year = 2004
xs = [str(year)]
corn = []
soybeans = []
grassland = []
developed = []
for x in range(len(frank)):
    plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year = plotter(plot, fig, frank[x][0], frank[x][1], corn, soybeans, grassland, developed, xs, year, "Frank")

plot = plt
fig = plot.figure()
year = 2004
xs = [str(year)]
corn = []
soybeans = []
grassland = []
developed = []
for x in range(len(carroll)):
    plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year = plotter(plot, fig, carroll[x][0], carroll[x][1], corn, soybeans, grassland, developed, xs, year, "Carroll")

plot = plt
fig = plot.figure()
year = 2004
xs = [str(year)]
corn = []
soybeans = []
grassland = []
developed = []
for x in range(len(webster)):
    plot, fig, unique, counts, corn, soybeans, grassland, developed, xs, year = plotter(plot, fig, webster[x][0], webster[x][1], corn, soybeans, grassland, developed, xs, year, "Webster")

