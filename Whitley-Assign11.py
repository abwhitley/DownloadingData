import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "MODIS_C6_1_GLobal_7d.csv"

try:
    f = open(filename)
except FileNotFoundError:
    print("File not found fix 'filename'")
    
with f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    lons = []
    lats = []
    brights = []
    
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

print(len(lons))


data = [{'type':'scattergeo','lon':lons,'lat':lats, 'marker': {'size':  [bright/50 for bright in brights]}}]
my_layout = Layout(title='Global Fires')


fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='global_fires.html')