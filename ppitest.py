import netCDF4 as ncdf
import os
import pyart
import numpy as np
import matplotlib.pyplot as plt
import cartopy
from pyart.io.common import make_time_unit_str
import datetime
from pyart.config import FileMetadata
from pyart.config import get_metadata, get_fillvalue
from pyart.core.radar import Radar


from load_mrms_ppi import load_mrms_ppi

fdict = [{'file': './20200302/KOHX/Velocity/00.50/20200303-060515.netcdf', 'ncvar': 'Velocity', 'pvar': 'corrected_velocity'},
         {'file': './20200302/KOHX/Reflectivity/00.50/20200303-060458.netcdf', 'ncvar': 'ReflectivityQC', 'pvar': "reflectivity"}]

fdict = [{'file': './20200302/KOHX/Velocity/04.00/20200303-060220.netcdf', 'ncvar': 'Velocity', 'pvar': 'corrected_velocity'},
         {'file': './20200302/KOHX/Reflectivity/04.00/20200303-060220.netcdf', 'ncvar': 'ReflectivityQC', 'pvar': "reflectivity"}]


myradar = load_mrms_ppi(fdict)
myradar.init_gate_altitude()
myradar.init_gate_longitude_latitude()

# Does not work
#pyart.io.write_cfradial("test.nc", myradar,  format='NETCDF4')

fig = plt.figure(figsize=(15,6))
display = pyart.graph.RadarMapDisplay(myradar)
plt.subplot(121)
display.plot_ppi('reflectivity')
plt.subplot(122)
display.plot_ppi('corrected_velocity')
plt.show()
