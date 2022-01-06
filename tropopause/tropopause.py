import os
from pkg_resources import resource_filename
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

file_path = resource_filename(__name__, os.path.join("data", "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc"))

data = xr.open_dataset(file_path)


def calc_cpt(lat):
    t = np.datetime64('2020-12-01')
    # slice = xr.DataArray(np.linspace(lat[0], lat[1], 2))
    data_sel = data.sel(latitude = slice(lat[0], lat[1])).sel(time = t).mean(dim="longitude")
    data_sel = data_sel.mean(dim="latitude")

    cpt_temp = data_sel.temperature.min()
    cpt_alt = data_sel.temperature.idxmin()

    return data_sel, cpt_alt, cpt_temp

def cpt_fig(lat, data_sel, cpt_alt, cpt_temp):
    fig, axs = plt.subplots(2)
    fig.suptitle(f"latitude: {lat}, time {lat}")
    axs[0].plot(data_sel.altitude, data_sel.temperature)
    axs[0].set_ylabel("temperature")
    axs[0].set_xlabel("altitude")
    axs[0].annotate(f"CPT: \n ({cpt_alt.values:.0f}, {cpt_temp.values:.2f})", xy=(cpt_alt, cpt_temp),
                    xytext=(cpt_alt, cpt_temp + 15),
                    arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
                    horizontalalignment="center",
                    )
    fig.savefig("CPT.png")
