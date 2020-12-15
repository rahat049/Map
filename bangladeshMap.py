from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon= 87.8,llcrnrlat=20.5,urcrnrlon=92.9,urcrnrlat=26.8,
             resolution='i', projection='tmerc', lat_0 = 23.6943117 , lon_0 = 90.344352)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#e1a95f',lake_color='aqua')
map.drawcoastlines()

map.readshapefile("BGD_ADM2", 'BGD_ADM2')
plt.show()
