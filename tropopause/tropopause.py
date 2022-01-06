import os
from pkg_resources import resource_filename
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

file_path = resource_filename(__name__, os.path.join("data", "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc"))

data = xr.open_dataset(file_path)

# testvalues
lat = 5
t = np.datetime64('2020-12-01')

data_sel = data.sel(latitude = lat, time = t).mean(dim="longitude")

temp_min = data_sel.temperature.min()
alt_temp_min = data_sel.temperature.idxmin()

fig, axs = plt.subplots(2)
fig.suptitle(f"latitude: {lat}, time {t}")
axs[0].plot(data_sel.altitude, data_sel.temperature)
axs[0].set_ylabel("temperature")
axs[0].set_xlabel("altitude")
axs[0].annotate(f"CPT: \n ({alt_temp_min.values:.0f}, {temp_min.values:.2f})", xy=(alt_temp_min, temp_min), xytext=(alt_temp_min, temp_min + 15),
             arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
             horizontalalignment="center",
             )
fig.savefig("CPT.png")
